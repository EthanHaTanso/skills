#!/usr/bin/env python3
"""
Slack Outreach Followup Checker

Checks if outreach threads have received followup screenshots
indicating funnel metric updates have been completed.
"""

import os
import sys
import argparse
from datetime import datetime, timedelta
from typing import Optional
import json

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
except ImportError:
    print("Error: slack_sdk not installed. Run: pip install slack-sdk")
    sys.exit(1)


# Proact channel ID
DEFAULT_CHANNEL_ID = "C09N1G89QDC"


def get_slack_client() -> WebClient:
    """Initialize Slack client with bot token."""
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        raise ValueError("SLACK_BOT_TOKEN environment variable not set")
    return WebClient(token=token)


def get_messages_in_timerange(
    client: WebClient,
    channel_id: str,
    days: int = 7,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> list:
    """
    Fetch messages from a channel within a time range.

    Args:
        client: Slack WebClient
        channel_id: Channel ID to fetch from
        days: Number of days to look back (default: 7)
        start_date: Optional start date (YYYY-MM-DD)
        end_date: Optional end date (YYYY-MM-DD)

    Returns:
        List of messages with thread_ts (thread parent messages)
    """
    if start_date and end_date:
        oldest = datetime.strptime(start_date, "%Y-%m-%d").timestamp()
        latest = datetime.strptime(end_date, "%Y-%m-%d").timestamp() + 86400  # End of day
    else:
        latest = datetime.now().timestamp()
        oldest = (datetime.now() - timedelta(days=days)).timestamp()

    messages = []
    cursor = None

    while True:
        try:
            result = client.conversations_history(
                channel=channel_id,
                oldest=str(oldest),
                latest=str(latest),
                limit=200,
                cursor=cursor,
            )

            # Filter for messages that have replies (threads)
            for msg in result.get("messages", []):
                if msg.get("reply_count", 0) > 0:
                    messages.append(msg)

            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break

        except SlackApiError as e:
            print(f"Error fetching messages: {e.response['error']}")
            break

    return messages


def get_thread_replies(client: WebClient, channel_id: str, thread_ts: str) -> list:
    """
    Fetch all replies in a thread.

    Args:
        client: Slack WebClient
        channel_id: Channel ID
        thread_ts: Thread timestamp

    Returns:
        List of reply messages (excluding parent)
    """
    replies = []
    cursor = None

    while True:
        try:
            result = client.conversations_replies(
                channel=channel_id,
                ts=thread_ts,
                limit=200,
                cursor=cursor,
            )

            # Skip the first message (thread parent)
            msgs = result.get("messages", [])
            if msgs:
                replies.extend(msgs[1:])  # Exclude parent message

            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break

        except SlackApiError as e:
            print(f"Error fetching replies: {e.response['error']}")
            break

    return replies


def has_image_attachment(message: dict) -> tuple[bool, Optional[str]]:
    """
    Check if a message contains an image attachment.

    Args:
        message: Slack message object

    Returns:
        Tuple of (has_image, uploader_user_id)
    """
    files = message.get("files", [])
    for file in files:
        mimetype = file.get("mimetype", "")
        if mimetype.startswith("image/"):
            return True, message.get("user")
    return False, None


def extract_company_name(message: dict) -> str:
    """
    Extract company name from outreach message text.

    Args:
        message: Slack message object

    Returns:
        Company name or "Unknown"
    """
    text = message.get("text", "")

    # Common patterns for outreach messages
    # Look for company names followed by target counts
    import re

    # Pattern: "Company Name | XX명" or "Company Name (XX명)"
    patterns = [
        r"[|｜]\s*([^|]+?)\s*[|｜]\s*[\d,]+\s*명",
        r"([A-Za-z][A-Za-z0-9\s&\-\.]+(?:LLC|Inc|Corp|Ltd|Company)?)\s*[|｜:]\s*[\d,]+",
        r"\*([^*]+)\*",  # Bold text often contains company names
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()

    # Fallback: first line truncated
    first_line = text.split("\n")[0][:50]
    return first_line if first_line else "Unknown"


def get_user_name(client: WebClient, user_id: str) -> str:
    """Get user display name from user ID."""
    try:
        result = client.users_info(user=user_id)
        user = result.get("user", {})
        return user.get("real_name") or user.get("name") or user_id
    except SlackApiError:
        return user_id


def format_timestamp(ts: str) -> str:
    """Convert Slack timestamp to readable date."""
    dt = datetime.fromtimestamp(float(ts))
    return dt.strftime("%Y-%m-%d %H:%M")


def check_outreach_followups(
    channel_id: str = DEFAULT_CHANNEL_ID,
    days: int = 7,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    output_format: str = "table",
) -> dict:
    """
    Main function to check outreach followup status.

    Args:
        channel_id: Slack channel ID
        days: Number of days to look back
        start_date: Optional start date
        end_date: Optional end date
        output_format: "table" or "json"

    Returns:
        Dictionary with results
    """
    client = get_slack_client()

    print(f"Fetching messages from channel {channel_id}...")
    messages = get_messages_in_timerange(
        client, channel_id, days, start_date, end_date
    )

    print(f"Found {len(messages)} threads. Checking for followup screenshots...")

    results = {
        "completed": [],
        "pending": [],
        "summary": {
            "total": 0,
            "completed": 0,
            "pending": 0,
        }
    }

    for msg in messages:
        thread_ts = msg.get("thread_ts") or msg.get("ts")
        company = extract_company_name(msg)
        outreach_date = format_timestamp(msg["ts"])

        # Get thread replies
        replies = get_thread_replies(client, channel_id, thread_ts)

        # Check for image attachments in replies
        has_screenshot = False
        screenshot_by = None
        screenshot_date = None

        for reply in replies:
            found, user_id = has_image_attachment(reply)
            if found:
                has_screenshot = True
                screenshot_by = get_user_name(client, user_id) if user_id else "Unknown"
                screenshot_date = format_timestamp(reply["ts"])
                break

        entry = {
            "company": company,
            "outreach_date": outreach_date,
            "thread_ts": thread_ts,
            "thread_url": f"https://slack.com/archives/{channel_id}/p{thread_ts.replace('.', '')}",
        }

        if has_screenshot:
            entry["status"] = "Completed"
            entry["screenshot_by"] = screenshot_by
            entry["screenshot_date"] = screenshot_date
            results["completed"].append(entry)
        else:
            # Calculate days since outreach
            outreach_dt = datetime.fromtimestamp(float(msg["ts"]))
            days_pending = (datetime.now() - outreach_dt).days
            entry["status"] = f"Pending ({days_pending} day{'s' if days_pending != 1 else ''})"
            entry["days_pending"] = days_pending
            results["pending"].append(entry)

    results["summary"]["total"] = len(messages)
    results["summary"]["completed"] = len(results["completed"])
    results["summary"]["pending"] = len(results["pending"])

    return results


def print_results(results: dict, output_format: str = "table"):
    """Print results in specified format."""
    if output_format == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    # Table format
    print("\n" + "=" * 80)
    print("OUTREACH FOLLOWUP STATUS REPORT")
    print("=" * 80)

    print(f"\nSummary: {results['summary']['completed']}/{results['summary']['total']} completed")
    print(f"         {results['summary']['pending']} pending followups\n")

    if results["completed"]:
        print("-" * 80)
        print("COMPLETED (Screenshot uploaded)")
        print("-" * 80)
        print(f"{'Company':<35} {'Outreach Date':<18} {'Screenshot By':<20}")
        print("-" * 80)
        for entry in results["completed"]:
            print(f"{entry['company'][:34]:<35} {entry['outreach_date']:<18} {entry.get('screenshot_by', '-'):<20}")

    if results["pending"]:
        print("\n" + "-" * 80)
        print("PENDING (No screenshot yet)")
        print("-" * 80)
        print(f"{'Company':<35} {'Outreach Date':<18} {'Status':<20}")
        print("-" * 80)
        for entry in results["pending"]:
            print(f"{entry['company'][:34]:<35} {entry['outreach_date']:<18} {entry['status']:<20}")

    print("\n" + "=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="Check Slack outreach thread followup status"
    )
    parser.add_argument(
        "--channel", "-c",
        default=DEFAULT_CHANNEL_ID,
        help=f"Slack channel ID (default: {DEFAULT_CHANNEL_ID})"
    )
    parser.add_argument(
        "--days", "-d",
        type=int,
        default=7,
        help="Number of days to look back (default: 7)"
    )
    parser.add_argument(
        "--start-date",
        help="Start date (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--end-date",
        help="End date (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["table", "json"],
        default="table",
        help="Output format (default: table)"
    )

    args = parser.parse_args()

    try:
        results = check_outreach_followups(
            channel_id=args.channel,
            days=args.days,
            start_date=args.start_date,
            end_date=args.end_date,
            output_format=args.format,
        )
        print_results(results, args.format)

        # Exit with non-zero if there are pending followups
        if results["summary"]["pending"] > 0:
            sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()
