#!/usr/bin/env python3
"""
Slack Outreach Followup Checker

Checks if outreach threads have received followup screenshots
indicating funnel metric updates have been completed.

Identifies outreach notifications by pattern:
- "X · Initial Outreach (M/DD)" - Sequence send notification
- Contains email address
- May have screenshot attachment showing "All set!" confirmation
"""

import os
import sys
import argparse
import re
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

# Pattern to identify Initial Outreach notifications
# Examples: "G · Initial Outreach (1/28)", "H · Initial Outreach (1/27)"
OUTREACH_PATTERN = re.compile(
    r"^([A-Z])\s*[·•]\s*Initial Outreach\s*\((\d{1,2}/\d{1,2})\)",
    re.MULTILINE
)


def get_slack_client() -> WebClient:
    """Initialize Slack client with bot token."""
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        raise ValueError("SLACK_BOT_TOKEN environment variable not set")
    return WebClient(token=token)


def is_outreach_notification(message: dict) -> Optional[dict]:
    """
    Check if a message is an Initial Outreach notification.

    Args:
        message: Slack message object

    Returns:
        Dict with parsed info if it's an outreach notification, None otherwise
    """
    text = message.get("text", "")

    # Match the outreach pattern: "X · Initial Outreach (M/DD)"
    match = OUTREACH_PATTERN.search(text)
    if not match:
        return None

    sequence_letter = match.group(1)
    date_str = match.group(2)

    # Extract email address if present
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    email = email_match.group(0) if email_match else None

    # Extract company/domain from email
    company = None
    if email:
        domain = email.split("@")[1] if "@" in email else None
        if domain:
            # Remove common TLDs and clean up
            company = domain.split(".")[0].replace("-", " ").title()

    return {
        "sequence_letter": sequence_letter,
        "outreach_date_str": date_str,
        "email": email,
        "company": company,
    }


def get_outreach_messages(
    client: WebClient,
    channel_id: str,
    days: int = 7,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> list:
    """
    Fetch Initial Outreach notification messages from a channel.

    Args:
        client: Slack WebClient
        channel_id: Channel ID to fetch from
        days: Number of days to look back (default: 7)
        start_date: Optional start date (YYYY-MM-DD)
        end_date: Optional end date (YYYY-MM-DD)

    Returns:
        List of outreach notification messages with parsed info
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

            # Filter for Initial Outreach notifications
            for msg in result.get("messages", []):
                outreach_info = is_outreach_notification(msg)
                if outreach_info:
                    msg["_outreach_info"] = outreach_info
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


def extract_company_info(message: dict) -> dict:
    """
    Extract company/target info from outreach message.

    Args:
        message: Slack message object with _outreach_info

    Returns:
        Dict with company name and other extracted info
    """
    outreach_info = message.get("_outreach_info", {})
    text = message.get("text", "")

    # Use parsed info from outreach pattern
    company = outreach_info.get("company")
    email = outreach_info.get("email")
    sequence = outreach_info.get("sequence_letter", "?")
    date_str = outreach_info.get("outreach_date_str", "")

    # If company not extracted from email, try other patterns
    if not company:
        # Look for domain in text
        domain_match = re.search(r"@([\w\.-]+\.\w+)", text)
        if domain_match:
            domain = domain_match.group(1)
            company = domain.split(".")[0].replace("-", " ").title()

    # Fallback to first line
    if not company:
        first_line = text.split("\n")[0][:40]
        company = first_line if first_line else "Unknown"

    return {
        "company": company,
        "email": email,
        "sequence": sequence,
        "date_str": date_str,
    }


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

    Identifies Initial Outreach notifications and checks if followup
    screenshots (funnel metric updates) have been posted in the thread.

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

    print(f"Fetching Initial Outreach notifications from channel {channel_id}...")
    messages = get_outreach_messages(
        client, channel_id, days, start_date, end_date
    )

    print(f"Found {len(messages)} outreach notifications. Checking for followup screenshots...")

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
        thread_ts = msg.get("ts")  # Use message ts as thread identifier
        company_info = extract_company_info(msg)
        outreach_date = format_timestamp(msg["ts"])
        poster_id = msg.get("user")
        poster_name = get_user_name(client, poster_id) if poster_id else "Unknown"

        # Get thread replies (if any)
        replies = get_thread_replies(client, channel_id, thread_ts)

        # Check for image attachments in replies (followup screenshots)
        has_followup_screenshot = False
        screenshot_by = None
        screenshot_date = None

        for reply in replies:
            found, user_id = has_image_attachment(reply)
            if found:
                has_followup_screenshot = True
                screenshot_by = get_user_name(client, user_id) if user_id else "Unknown"
                screenshot_date = format_timestamp(reply["ts"])
                break

        entry = {
            "company": company_info["company"],
            "email": company_info.get("email"),
            "sequence": company_info.get("sequence", "?"),
            "outreach_date": outreach_date,
            "posted_by": poster_name,
            "thread_ts": thread_ts,
            "thread_url": f"https://slack.com/archives/{channel_id}/p{thread_ts.replace('.', '')}",
        }

        if has_followup_screenshot:
            entry["status"] = "Completed"
            entry["followup_by"] = screenshot_by
            entry["followup_date"] = screenshot_date
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
    print("\n" + "=" * 90)
    print("OUTREACH FOLLOWUP STATUS REPORT")
    print("=" * 90)

    print(f"\nSummary: {results['summary']['completed']}/{results['summary']['total']} completed")
    print(f"         {results['summary']['pending']} pending followups\n")

    if results["completed"]:
        print("-" * 90)
        print("COMPLETED (Followup screenshot uploaded)")
        print("-" * 90)
        print(f"{'Seq':<4} {'Company':<25} {'Outreach':<18} {'Posted By':<12} {'Followup By':<15}")
        print("-" * 90)
        for entry in results["completed"]:
            seq = entry.get("sequence", "?")
            company = entry["company"][:24] if entry["company"] else "Unknown"
            outreach = entry["outreach_date"]
            posted = entry.get("posted_by", "-")[:11]
            followup = entry.get("followup_by", "-")[:14]
            print(f"{seq:<4} {company:<25} {outreach:<18} {posted:<12} {followup:<15}")

    if results["pending"]:
        print("\n" + "-" * 90)
        print("PENDING (No followup screenshot yet)")
        print("-" * 90)
        print(f"{'Seq':<4} {'Company':<25} {'Outreach':<18} {'Posted By':<12} {'Status':<20}")
        print("-" * 90)
        for entry in results["pending"]:
            seq = entry.get("sequence", "?")
            company = entry["company"][:24] if entry["company"] else "Unknown"
            outreach = entry["outreach_date"]
            posted = entry.get("posted_by", "-")[:11]
            status = entry["status"]
            print(f"{seq:<4} {company:<25} {outreach:<18} {posted:<12} {status:<20}")

    print("\n" + "=" * 90)


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
