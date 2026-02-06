# Phase 2: JTBD Document Organization & MVP Go/No-Go Decision

## Overview

This phase focuses on organizing raw interview data into a structured JTBD (Jobs to be Done) document and making the critical Go/No-Go decision on whether to proceed with MVP development.

**Duration**: After each interview (same day or next day)
**Output**: JTBD document + Go/No-Go decision
**Next Phase**: Phase 3 (MVP Ideation) if GO decision

---

## Section 1: JTBD Document Organization

### Purpose

Transform raw interview notes/transcripts into a comprehensive JTBD document that:
- Captures user context and workflow deeply
- Identifies pain points with specificity
- Clarifies desired outcomes
- Enables technical feasibility assessment
- Provides foundation for MVP ideation

### 1-1. Interview Content Organization (Conversational Refinement)

**Usage**:
- "인터뷰 녹취록을 JTBD로 정리해줘"
- "인터뷰 raw data를 구조화해줘"

**Process** (Interactive Approach):

#### Step 1: Auto-Draft Generation

From raw data (transcript, notes), generate initial JTBD draft using [references/jtbd-template.md](references/jtbd-template.md) structure:

**Sections to populate**:
1. User Context
2. Job (Core Task)
3. AS-IS Workflow (Current Process)
4. Context (When task occurs)
5. Pain Points (Specific problems)
6. Desired Outcome (Ideal state)
7. Technical Constraints
8. AI Redesign Opportunity
9. MVP Scope

---

#### Step 2: Clarifying Unclear Sections

Identify ambiguous areas and determine appropriate question targets:

**Target Questioning Strategy**:

##### For Interview Host (Ask Immediately):
- **Non-verbal context**: Body language, tone, emphasis
- **Observational insights**: What you noticed while interviewing
- **Priority assessment**: Which pain points matter most to the user
- **Workflow nuances**: Timing, frequency, dependencies
- **Success signals**: What would make them excited

**Why ask immediately**: Host was present and can provide context and interpretation immediately

##### For Interview Guest (Async Follow-up):
- **AS-IS Workflow clarity**: If steps are unclear or incomplete
  - "Can you walk through the exact sequence one more time?"
  - "Are there any intermediate steps we missed?"

- **Pain Point specificity**: If described too abstractly
  - "Can you give a concrete example of [pain point]?"
  - "How often does this happen?"
  - "What's the impact when it happens?"

- **Desired Outcome precision**: If vague
  - "What would 'ideal' look like for you?"
  - "If we could fix one thing, what would it be?"

- **Technical Constraints gaps**: If not fully covered
  - "What systems do you currently use?"
  - "Are there any security/compliance constraints?"

**Organize as "Follow-up Questions for Guest"** section in JTBD doc

---

#### Step 3: Interactive Refinement

**Process**:
1. Show draft JTBD document to user
2. Ask clarifying questions immediately (host perspective)
3. Collect guest follow-up items to send later
4. Update JTBD with host's responses immediately
5. Create "Follow-up Questions for Guest" list

**Conversation Pattern**:

```markdown
## 🔍 Clarifying Questions (for you as host)

1. **AS-IS Workflow**: When [guest] described the process, did they seem...
   - [Option A description]
   - [Option B description]

   What was your impression?

2. **Pain Point Impact**: [Guest] mentioned "[pain point]" quite emotionally.
   How frequently does this happen in your observation?

3. **Context**: Is [workflow] always triggered by [event], or are there other scenarios?

4. **Priority**: Which pain point seems most critical to solve first?
```

---

### 1-2. JTBD Structure (9 Sections)

#### Section 1: User Context
- **Name & Role**: Who is this person
- **Company & Type**: Organization context
- **Seniority**: Years of experience
- **Key Information**: What shapes their workflow

#### Section 2: Job (핵심 작업)
- **Primary Job**: What is the core work?
- **Frequency**: How often?
- **Scope**: Scale/volume

**Example**:
```markdown
## Job: Weekly Campaign Performance Reporting

- **Primary Task**: Analyze campaign metrics and write weekly performance report
- **Frequency**: Once per week (typically Mondays)
- **Scope**: 3-5 campaigns, 10-15 metrics per campaign
- **Context**: Required for leadership visibility and next-week planning
```

#### Section 3: AS-IS Workflow (Current Process)
- **Step-by-step process**: Exact sequence with timing
- **Tools used**: Current software/systems
- **Decision points**: Where choices are made
- **Handoffs**: Points where work passes to someone else

**Must be concrete and specific**, not abstract

**Example**:
```markdown
## AS-IS Workflow: Campaign Reporting (2 hours total)

1. **Data Extraction** (30 min)
   - Login to Google Analytics
   - Filter by campaign (manual selection)
   - Export metrics as CSV
   - Check against other platforms (Facebook Ads Manager, LinkedIn)

2. **Data Reconciliation** (1 hour)
   - Open Excel (existing template)
   - Copy-paste data from multiple CSVs
   - Fix formatting inconsistencies
   - Manual calculation for derived metrics (ROI, conversion rate)

3. **Report Writing** (30 min)
   - Write narrative analysis of results
   - Create charts/visualizations (manual)
   - Compare to previous week
   - Publish to internal wiki
```

#### Section 4: Context (When Task Occurs)
- **Trigger**: What initiates the task?
- **Constraints**: Time pressure, dependencies
- **Environment**: Where/how is work done?

**Example**:
```markdown
## Context

- **Trigger**: Monday morning, 9 AM team standup
- **Time Constraint**: Must be ready before 2 PM all-hands meeting
- **Dependencies**: Relies on campaign data from marketing ops team
- **Environment**: Remote, done at desk with multiple monitors
- **Frequency Pressure**: Non-negotiable weekly deadline
```

#### Section 5: Pain Points (Specific Problems)
- **3-5 top pain points** (prioritized)
- **For each pain point**:
  - Description (what goes wrong)
  - Frequency (how often)
  - Impact (time, frustration, business consequence)
  - Ideal alternative

**Example**:
```markdown
## Pain Points

### 1. Manual Data Collection (HIGH IMPACT)
- **What**: Data scattered across 5 different platforms, no unified view
- **Frequency**: Happens every Monday
- **Impact**: 30 minutes lost each week to manual copying; high error rate
- **Frustration**: "It's busywork, not real work"
- **Ideal**: Data automatically aggregated from all sources

### 2. Reconciliation Complexity (HIGH IMPACT)
- **What**: Numbers don't match between platforms; must manually verify
- **Frequency**: Happens 50% of weeks
- **Impact**: Adds 20-30 min to already tight timeline
- **Frustration**: "I spend time fixing numbers instead of analyzing trends"
- **Ideal**: Automatic reconciliation with clear explanations for discrepancies

### 3. Repetitive Analysis (MEDIUM IMPACT)
- **What**: Writing same analysis patterns each week (trend descriptions, comparisons)
- **Frequency**: Every Monday
- **Impact**: 30 min of report writing feels mechanical
- **Frustration**: "I'm not adding value, just rewriting the same narrative"
- **Ideal**: AI suggests analysis; she refines with nuance/context
```

#### Section 6: Desired Outcome (원하는 결과)
- **Ideal state**: What success looks like
- **Timeframe**: How much time could be saved
- **Quality**: Should output be better, same, or just faster?
- **Confidence**: What level of trust is needed?

**Example**:
```markdown
## Desired Outcome

- **Time Target**: 15-20 minutes (from 2 hours)
- **Workflow Change**: Monday morning, upload data once → System does everything
- **Output Quality**: Same or better than manual (clear, actionable insights)
- **Trust Level**: Can't publish reports without spot-checking ("AI is helpful but not final authority")
- **Nice-to-Have**: Automatic alerts for unusual anomalies
```

#### Section 7: Technical Constraints
- **Data Access**: Where is data? How accessible?
- **System Integration**: What systems must connect?
- **Security/Compliance**: Any restrictions?
- **Manual Workarounds**: Current hacks in place?

**Example**:
```markdown
## Technical Constraints

- **Data Sources**:
  - Google Analytics (API available, OAuth setup possible)
  - Facebook Ads (API available, but requires new credential setup)
  - LinkedIn Ads (API available, less documented)
  - Internal CRM (older system, CSV export only, no API)

- **Current Stack**: Excel, Google Sheets, Google Analytics
- **Cloud Policy**: Company allows AWS/GCP/Azure
- **Data Sensitivity**: Marketing data only (not sensitive)
- **Manual Workaround**: Maintains "master export script" in Python (rarely updated)
```

#### Section 8: AI Redesign Opportunity
- **Core Problem Statement**: What is the essence of the workflow problem?
- **Redesign Possibility**: How could AI fundamentally change the approach?
- **Value Impact**: High/Medium/Low
- **User Confidence**: Do they believe this is solvable?

**Example**:
```markdown
## AI Redesign Opportunity

### Core Problem
Current process treats "campaign reporting" as three separate tasks (collect, reconcile, analyze).
They're actually one task: "understand campaign performance at a glance."

### Redesign Approach
Instead of step-by-step manual workflow, natural language interface:
- "What did we learn from this week's campaigns?"
- AI automatically: collects data, reconciles discrepancies, generates analysis

### Value Impact
- **High**: Eliminates 1.5 hours of weekly busywork
- **High**: Improves data accuracy (automatic reconciliation)
- **High**: Enables faster decision-making (analysis in seconds, not minutes)
- **Cannot-go-back potential**: Once she experiences automated analysis, manual reporting will feel painful

### Why It's Redesign, Not Just Automation
- Not just "speed up existing steps"
- Fundamentally changes interaction model: from "do these 3 steps" to "ask a question"
- Unlocks new possibilities: "compare campaigns", "identify anomalies", etc.
```

#### Section 9: MVP Scope (Go/No-Go Assessment)
- **MVP Scope**: What would v1.0 include?
- **Exclusions**: What's intentionally out of scope?
- **Success Criteria**: How to measure if MVP works?

**Example**:
```markdown
## MVP Scope (v1.0)

### In Scope
- [ ] Single interface for viewing weekly campaign data
- [ ] Automated data collection from GA + Facebook Ads
- [ ] AI-generated narrative insights
- [ ] Comparison to previous week

### Out of Scope (v1.1)
- LinkedIn Ads integration (more complex API)
- Internal CRM data (no API, complex)
- Predictive analytics
- Automated report distribution

### Go/No-Go Criteria
- [ ] AI redesign potential: YES
- [ ] Technical feasibility (1-2 weeks): YES
- [ ] User enthusiasm: YES
```

---

### 1-3. Follow-up Questions Organization

If guest follow-ups are needed, organize clearly:

```markdown
## Follow-up Questions for Guest

These questions need clarification from [USER_NAME]:

### Critical (Affects MVP Scope)
1. **Data Reconciliation Rules**
   - When FB Ads and GA report different numbers, which source of truth do you use?
   - Are there known discrepancies you account for manually?
   - *Why this matters*: Affects whether MVP can auto-reconcile or just flag discrepancies

2. **Report Distribution**
   - Do you email reports, post to wiki, or both?
   - Who consumes the report? (leadership, campaign managers, stakeholders)
   - *Why this matters*: Affects distribution mechanism in MVP

### Important (Enhances MVP)
3. **Trend Analysis Depth**
   - When you write trends, what comparisons matter most?
     - Week-over-week, month-over-month, year-over-year?
   - Any specific metrics you focus on?

### Nice-to-Have
4. **Anomaly Sensitivity**
   - How do you currently spot unusual trends?
   - Should MVP alert you to anomalies automatically?
```

**Sending Follow-up Questions**:
- Send within 1 day of interview
- Use conversational tone
- Number questions (easy to reply to)
- Group by priority
- Explain why each matters

---

### 1-4. Document Storage & User List Update

#### File Storage

Save JTBD document to:
```
./User Discover/User Interview/[USER_ID]_[YYYY-MM-DD].md
```

**Example**: `./User Interview/USER_001_2024-02-04.md`

#### User List Update

Update `./User Discover/User List/users.csv`:

**Before**:
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

**After**:
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
  "status": "interviewed",  // ← CHANGED
  "years_of_experience": "3년차",
  "prior_hints": "캠페인 리포트 작업이 힘들다고 함",
  "current_tools": ["Notion", "Google Analytics", "Excel"],
  "jtbd_document": "./User Interview/USER_001_2024-02-04.md",  // ← ADDED
  "jtbd_status": "complete"  // ← ADDED
}
```

---

## Section 2: MVP Go/No-Go Decision

### Purpose

Evaluate whether the JTBD warrants MVP development based on:
1. **AI Redesign Potential** (Must-have): Can AI fundamentally improve this workflow?
2. **Technical Feasibility** (Must-have): Can it be built in 1-2 weeks?
3. **Global Scalability** (Nice-to-have for Closed network): Does it have broad appeal?

---

### 2-1. Decision Tree

```
[1. AI Redesign Potential Check]
   ├─ Can compress multiple steps into one?
   ├─ Does it create new possibilities?
   └─ High/Medium value impact?
        ↓
     YES → Continue
     NO  → ❌ NO-GO
        ↓
[2. Technical Feasibility Check]
   ├─ 1-2 weeks to build?
   ├─ Data accessible?
   └─ Constraints solvable?
        ↓
     YES → ✅ GO!
     NO  → ❌ NO-GO
```

---

### 2-2. Criterion 1: AI Redesign Potential (CRITICAL)

**This is the gatekeeper criterion. Fail here = automatic NO-GO.**

#### A. Step Compression Capability

**Question**: Can multiple manual steps be consolidated into one?

**PASS Examples**:
- Data collection + reconciliation + formatting + analysis (4 steps) → AI auto-analysis (1 step)
- Manual categorization + sorting + reporting (3 steps) → AI-powered dashboard (1 step)

**FAIL Examples**:
- Simple copy-paste automation (steps are same, just faster)
- Tool switching automation (steps are same, just easier)
- "Making Excel more user-friendly" (not redesign)

**Test**: Ask "Does this eliminate entire steps, or just speed them up?"

---

#### B. New Possibilities Creation

**Question**: Does AI enable something previously impossible?

**PASS Examples**:
- Natural language query for data analysis (previously: SQL-only or manual)
- Automatic pattern detection across complex datasets (previously: human observation only)
- Batch processing with AI validation (previously: can't batch risky tasks)

**FAIL Examples**:
- Existing tool replacement (Tool A → Tool B, same capability)
- UI improvement to existing process (faster, not different)

**Test**: Ask "What was impossible before that's now possible?"

---

#### C. Value Impact Assessment

**Question**: Would the improvement be so valuable they can't go back to old way?

**Scale**:
- ✅ **High**: "I could never go back to the old way"
  - Eliminates 50%+ of time
  - Fundamentally changes capability
  - Examples: Campaign reporting (2h → 15m), Code review (1h → 5m)

- ⚠️ **Medium**: "This is nice but I could manage without it"
  - Eliminates 20-50% of time
  - Improves quality but not workflow
  - Examples: Formatting automation, UI improvements
  - **Only PASS if other factors are exceptional**

- ❌ **Low**: "This is a minor convenience"
  - Eliminates <20% of time
  - Peripheral to main task
  - Examples: Notification settings, data export improvements
  - **Automatic NO-GO**

**Test**: Would they pay for this? Would they recommend to colleagues?

---

### 2-3. Criterion 2: Technical Feasibility (CRITICAL)

**This criterion validates that Criterion 1 can be realized.**

#### A. Implementation Timeline

**Estimation Framework** (1-2 weeks = 10-14 days available):

| Component | Typical Duration |
|-----------|------------------|
| Simple frontend | 1-2 days |
| AI API integration | 1 day |
| Data processing logic | 1-2 days |
| External API integration | 1-2 days |
| Database setup | 0.5-1 day |
| Deployment | 0.5 day |
| Testing | 1-2 days |
| **Total for simple MVP** | **5-9 days** |

**PASS**: Total < 14 days
**FAIL**: Total > 14 days or depends on uncontrolled factors

**Breakdown Questions**:
- What are the 3-5 core technical tasks?
- How long does each typically take?
- Are there any unknowns that could extend timeline?

---

#### B. Data Accessibility

**Categories**:

✅ **PASS** (Data easily accessible):
- CSV/Excel exports
- Public APIs (well-documented)
- OAuth SaaS platforms (Slack, Google Workspace)
- Open data sources

❌ **FAIL** (Data difficult/impossible to access):
- Legacy internal databases (no API, no export)
- Proprietary closed systems (no API, company controls access)
- Data with strict compliance restrictions (can't move externally)

**Clarify with User**:
- "Where does the data live?"
- "Can you export it?"
- "Does IT need to approve?"

---

#### C. Technical Constraint Resolution

**Categories**:

| Constraint Type | Solution |
|-----------------|----------|
| Can't use external cloud | Build local app (add 2-3 days) |
| Can't send data externally | Process locally, not via API (feasible) |
| IT approval needed | User handles (not blocker if willing) |
| Security scanning required | Plan 1-2 days (acceptable) |

**Blocking Constraints** (automatic FAIL):
- Data not accessible at all
- Requires months of IT review
- Technical approach doesn't exist yet

---

### 2-4. Document Go/No-Go Decision

Record decision clearly in JTBD:

#### PASS Example (GO)

```markdown
## MVP Go/No-Go Decision: ✅ GO

### 1. AI Redesign Potential
- ✅ Step Compression: 3 steps (collect, reconcile, analyze) → 1 (AI auto-analysis)
- ✅ New Possibilities: Natural language queries, auto-anomaly detection
- ✅ Value Impact: **HIGH** (2h → 15m, "can't go back")

### 2. Technical Feasibility
- ✅ Timeline: 10-12 days (within 2-week window)
  - GA API integration: 2 days
  - AI analysis engine: 3 days
  - Frontend: 2 days
  - Testing: 2-3 days
- ✅ Data Access: GA + Facebook Ads APIs both available
- ✅ Constraints: Cloud provider OK, no security blockers

### Decision
Proceed to MVP Ideation (Section 5)
```

#### FAIL Example (NO-GO)

```markdown
## MVP Go/No-Go Decision: ❌ NO-GO

### Reason
While workflow is painful (pain points: HIGH), AI redesign potential is LOW.

### Analysis
- ❌ Step Compression: Task is single-step (contract review); automation would speed it up but not compress steps
- ❌ New Possibilities: AI can't enable anything truly new here; legal review still requires human judgment
- ❌ Value Impact: MEDIUM (1h → 40m); user said "helpful but not must-have"

### Why No-Go
This is optimization (AI helps with current step), not redesign (changing the workflow).
Better suited for legal tech tools; not Global Scalable product opportunity.

### Learning
Legal domain needs redesign opportunity that goes deeper than "faster review."
Look for: "enable non-lawyers to review", "automatic risk categorization", etc.
```

---

### 2-5. Status Update & Next Steps

#### If GO

Update User List:
```json
{
  "user_id": "USER_001",
  "status": "go_approved",  // interviewed → go_approved
  "go_date": "2024-02-05",
  "go_decision": "yes",
  "jtbd_status": "complete",
  "next_phase": "mvp_ideation"
}
```

**Next Step**: Section 3 (MVP Ideation)

#### If NO-GO

Update User List:
```json
{
  "user_id": "USER_001",
  "status": "no_go",  // interviewed → no_go
  "no_go_date": "2024-02-05",
  "no_go_reason": "AI redesign potential LOW - optimization not redesign",
  "learning": "Legal review domain needs deeper redesign opportunity"
}
```

**Next Step**:
- Document learning in project notes
- Move to next interview
- Revisit if future opportunity arises

---

## Key Success Principles

### For JTBD Creation

1. **Be Specific**: "User struggles with reporting" → "Spends 2 hours every Monday manually combining data from 5 systems"
2. **Understand Context**: Why does this task exist? What depends on it?
3. **Capture Emotional Responses**: "Frustrated", "energized", "bored" indicate importance
4. **Don't Oversimplify**: Capture nuance; different people do same job differently
5. **Conversational Refinement is OK**: It's fine to iteratively fill in JTBD with user input

### For Go/No-Go Decision

1. **AI Redesign First**: Not "Can we automate?" but "Can AI fundamentally change the approach?"
2. **Feasibility Matters**: Great idea that takes 4 weeks = NO-GO
3. **No Sacred Cows**: Even painful workflows can be NO-GO if redesign potential is low
4. **Document Reasoning**: Future learning depends on clear rationale
5. **Closed Network = Learning Phase**: Don't expect high global scalability yet; focus on AI redesign quality

---

## Common Pitfalls to Avoid

| Pitfall | What Goes Wrong |
|---------|-----------------|
| **Accepting vague JTBD** | Leads to vague MVP; wastes development time |
| **Confusing automation with redesign** | Builds features users don't truly need |
| **Ignoring technical constraints** | MVP fails to launch or takes too long |
| **Yes bias in Go/No-Go** | Wastes time on low-potential ideas |
| **Not recording reasoning** | Can't learn why decisions succeeded/failed |

---

## Cross-Phase References

- **Phase 1**: Interview preparation → generates raw data for JTBD
- **Phase 3**: MVP Ideation (if GO) → starts with completed JTBD
- **Phase 4**: Demo & Follow-up → validates JTBD assumptions
- **Tracking**: P-S Tree structure informed by JTBD deduplication

## Template References

- [references/jtbd-template.md](references/jtbd-template.md) - Complete JTBD structure
- [references/go-no-go-criteria.md](references/go-no-go-criteria.md) - Detailed evaluation framework
