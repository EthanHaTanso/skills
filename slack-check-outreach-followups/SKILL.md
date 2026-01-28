---
name: slack-check-outreach-followups
description: This skill should be used when the user asks to "check outreach followups", "outreach 후속작업 확인", "메트릭 업데이트 여부 확인", or mentions "outreach thread screenshot check". Checks if outreach threads have followup screenshots uploaded indicating funnel metric updates.
version: 0.1.0
---

# Slack Outreach Followup Checker

Check outreach thread followup status by detecting screenshot uploads in thread replies.

## Overview

When team members complete outreach activities, they post initial outreach notifications to the Proact channel. After updating funnel metrics, they upload screenshots to the same thread as confirmation. This skill checks which outreach threads have received followup screenshots.

## Workflow

### 1. Identify Initial Outreach Notifications

Search the Proact channel for Sequence send notifications matching pattern:
```
X · Initial Outreach (M/DD)
email@domain.com
[Screenshot: "All set!" confirmation]
```

Where:
- `X` = Sequence letter (A, B, C, ... G, H, etc.)
- `M/DD` = Month/Day of outreach
- Email address identifies the target company/contact

### 2. Check for Followup Screenshots

For each identified outreach notification:
- Retrieve all replies in the thread
- Check if any reply contains an image attachment (files with `mimetype` starting with `image/`)
- Image in reply indicates followup completion (funnel metric update confirmed)

### 3. Generate Report

Output a table showing:
- Company name
- Outreach date/time
- Followup status (completed with screenshot / pending)
- Days since outreach (for pending items)

## Usage

To check outreach followups for the past week:

```
Check outreach followups for the last 7 days
```

To check specific date range:

```
Check outreach followups from 2026-01-20 to 2026-01-28
```

## Script Execution

Run the Python script with Slack API credentials:

```bash
export SLACK_BOT_TOKEN="xoxb-your-token"
python scripts/check_followups.py --channel C09N1G89QDC --days 7
```

## Output Format

```
| Company | Outreach Date | Followup Status | Screenshot By |
|---------|---------------|-----------------|---------------|
| Company A | 2026-01-28 10:34 | Completed | @user1 |
| Company B | 2026-01-27 14:22 | Pending (1 day) | - |
```

## Integration Notes

- Channel ID for Proact: `C09N1G89QDC`
- Screenshot detection: Any image file attachment in thread replies
- Time range: Default is 7 days, configurable via parameters
