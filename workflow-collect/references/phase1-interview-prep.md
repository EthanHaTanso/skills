# Phase 1: Interview Preparation

Complete guide for preparing user interviews to collect workflow pain points.

## Overview

Interview preparation has three main steps:
1. Write recruitment messages
2. Register user to User List
3. Generate customized interview questions

## 1-1. Write Recruitment Messages

### Purpose

Create channel-appropriate invitation messages for different networks.

### Usage Examples

- "Closed network 초대 메시지 작성해줘"
- "[직무] 대상 Public 모집 글 만들어줘"
- "Indirect 채널용 설문 포함 메시지 만들어줘"

### Process

1. **Identify target channel** (Closed/Indirect/Public)
2. **Identify target job function** (Marketing, Legal, Engineering, etc.)
3. **Generate message** using [message-templates.md](message-templates.md)
4. **Customize with user** through dialogue

### Key Points by Channel

**Closed Network**:
- Simple and friendly tone
- Mention portfolio building purpose
- Direct invitation
- Example: "Hi! I'm building a portfolio of workflow automation tools..."

**Indirect Network**:
- Include pre-interview survey
- Build trust with mutual connections
- Pre-collect workflow information
- Example: "Hello from [Community]! I'm researching workflow improvements for [Job]..."

**Public Network**:
- Emphasize portfolio + testimonial opportunity
- Job-specific targeting (r/marketing, r/sales, etc.)
- Professional but approachable
- Example: "Looking for [Job Function] professionals who want to improve their workflow..."

### Reference

See [message-templates.md](message-templates.md) for complete templates and examples.

---

## 1-2. Register User to User List

### Purpose

Track interviewee information before conducting the interview.

### Required Information

**Essential**:
- **Name**: Interviewee's name
- **Job Function**: Marketing Manager, Legal, Data Analyst, etc.
- **Company**: Company name
- **Company Type**: Startup / Enterprise / Foreign / Freelancer
- **Network Path**: closed / indirect / public
  - closed: "직접 아는 사이"
  - indirect: "[Referrer name] 소개" or "[Community name]에서 모집"
  - public: "X(Twitter)" / "Reddit r/[subreddit]" / "[Platform]"
- **Interview Scheduled Date**: YYYY-MM-DD

**Optional** (if known):
- **Years of Experience**: Career years in the job (e.g., "3년차", "신입")
- **Prior Hints**: Any pain points or interests known beforehand
- **Current Tools**: Tools they currently use (e.g., Notion, Slack, Excel)

### User List Management

**File Location**: `./User Discover/User List/users.json`

**Process**:
1. Check if `./User Discover/User List/users.json` exists
2. If not exists, create new file with empty array `[]`
3. If exists, read current content
4. Generate new User ID (e.g., USER_001, USER_002, ...)
   - Find highest existing ID and increment
5. Create user entry with collected information
6. Add to users.json and save
7. Confirm with user that information is correct

**User Entry Structure**:

```json
{
  "user_id": "USER_001",
  "name": "김철수",
  "business_function": "Marketing",
  "company": "ABC 스타트업",
  "company_type": "스타트업",
  "network_type": "closed",
  "referral": "직접 아는 사이",
  "interview_date": "2024-02-04",
  "status": "scheduled",
  "years_of_experience": "3년차",
  "prior_hints": "캠페인 리포트 작업이 힘들다고 함",
  "current_tools": ["Notion", "Google Analytics", "Excel"]
}
```

**Status Values**:
- `scheduled`: Interview scheduled but not yet conducted
- `interviewed`: Interview completed, JTBD in progress
- `mvp_delivered`: MVP demo completed
- `big_fan`: Identified as Big Fan
- `pivot`: Decided to pivot away from this workflow

### User Confirmation

After creating the entry:
- Show the user the created entry
- Ask if any corrections are needed
- Update if necessary

---

## 1-3. Generate Interview Questions

### Purpose

Create customized question guide based on interviewee's information.

### Usage Examples

- "인터뷰 질문지 만들어줘"
- "[직무] 대상 인터뷰 준비해줘"
- "[이름]님 인터뷰 준비해줘"

### Prerequisites

User must be registered in User List first (Section 1-2).

### Two Question Versions Available

**Version 1: Situational Question Tree**
- Follow-up questions based on user responses
- Flexible branching
- Good for exploratory interviews
- Reference: [interview-questions-tree.md](interview-questions-tree.md)

**Version 2: Framework + Examples**
- JTBD framework-based structure
- Concrete examples for each question
- Good for structured interviews
- Reference: [interview-questions-framework.md](interview-questions-framework.md)

### Customization Elements

**Based on User List information**:

1. **Job-specific pain points**
   - Marketing: Reporting, campaign management, data collection
   - Legal: Contract review, compliance tracking
   - Engineering: Code review, deployment, debugging
   - Finance: Reconciliation, reporting, forecasting

2. **Company type adjustments**
   - Startup: Ask about technical constraints, IT approval process
   - Enterprise: Ask about legacy systems, security policies
   - Freelancer: Ask about client communication, invoicing

3. **Prior hints integration**
   - If hints exist, add specific follow-up questions
   - Example: If hint is "캠페인 리포트 작업이 힘들다" → Add detailed questions about reporting workflow

### Key Interview Approach

**Pain Point-Centered**:
- "어제 가장 짜증났던 순간은?" (What frustrated you most yesterday?)
- Focus on concrete, recent experiences
- Not hypothetical scenarios

**Screen Sharing Recommended**:
- Watch actual work being done
- See real tools and workflows
- Observe pain points in real-time

**Specific Scenarios**:
- Base questions on "yesterday" or "last week"
- Ask for concrete examples, not generalizations
- "Walk me through what you did yesterday morning..."

**Deep Diving**:
- Ask "why?" at least 3 times
- Get to root causes
- Understand emotional impact

### User Choice

After generating both versions:
- Ask user which version they prefer
- Or provide both for flexibility
- User can mix and match questions

### Interview Duration Guide

**Total**: 30-40 minutes

**Time Allocation**:
- Opening: 5 minutes
- AS-IS Workflow understanding: 10-15 minutes
- Pain Point exploration: 5-10 minutes
- Desired State understanding: 5-10 minutes
- Technical Feasibility: 5 minutes
- Wrap-up: 2 minutes

### During Interview Tips

**Real-time Note-taking**:
- Take notes in JTBD structure during interview
- Easier to organize later
- Reduces post-interview work

**Clarify Immediately**:
- If something is unclear, ask right away
- Don't assume or fill in gaps
- Better to extend interview than have incomplete info

**Screen Sharing is Key**:
- Actually watch them work
- See their tools and files
- Observe their workarounds

### References

- [interview-questions-tree.md](interview-questions-tree.md): Situational question tree with branching
- [interview-questions-framework.md](interview-questions-framework.md): Framework-based questions with examples
- [message-templates.md](message-templates.md): For recruitment message creation

---

## Common Patterns

### Pattern 1: Closed Network First Interview

1. Send simple invitation message (1-2)
2. Register to User List (1-2)
3. Generate customized questions (1-3)
4. Conduct 30-40 min interview
5. Proceed to Phase 2 (JTBD Organization)

### Pattern 2: Public Channel Expansion

1. Write public recruitment post (1-1)
2. Collect responses
3. For each promising response:
   - Register to User List (1-2)
   - Generate questions (1-3)
   - Schedule interview

### Pattern 3: Indirect Network with Survey

1. Write indirect message with survey (1-1)
2. Collect survey responses
3. Review responses and select promising candidates
4. Register selected candidates to User List (1-2)
5. Generate customized questions based on survey (1-3)

---

## Next Phase

After completing interview preparation and conducting the interview:

→ **Phase 2: JTBD Organization** (See [phase2-jtbd.md](phase2-jtbd.md))
- Organize interview raw data into JTBD document
- Evaluate Go/No-Go decision
