# Phase 4: Demo, Follow-up, and MVP Tracking & Management

## Overview

This phase covers the critical post-development activities:

1. **Demo & Follow-up** (Week 2): Present MVP, gather immediate feedback
2. **MVP Tracking & Management** (Ongoing): Organize and track all MVPs, users, and problems
3. **Iteration vs Pivot Decision** (Week 3): Determine next action based on user feedback
4. **Channel Expansion Strategy**: Plan scaling from Closed → Indirect → Public networks
5. **Big Fan Tracking**: Identify and nurture high-potential users

**Duration**: Continuous (demo 30min, follow-up calls 15min, tracking ongoing)
**Output**: Updated project records, iteration plans, learning notes
**Next Phase**: Phase 5 (Public Channel Expansion) if Big Fan identified

---

## Section 1: Demo & Follow-up (Week 2)

### 1-1. Demo Execution (Day 7)

**Timing**: Schedule for 1 week after proposal approval

**Duration**: 30 minutes

**Structure**:

```
[5 min] Opening & Context Refresh
  - Remind user of original pain points
  - Show MVP Proposal recap

[5 min] Before Scenario Walkthrough
  - Describe how they currently do the task (from JTBD)
  - Time/pain points involved

[10 min] Live Demo
  - Show MVP working with their real (or realistic) data
  - Go through main features
  - Demonstrate time savings

[5 min] Q&A & First Reactions
  - "What's your first impression?"
  - "Anything surprising?"
  - Gauge enthusiasm level

[5 min] Next Steps
  - Explain 1-week usage period
  - Follow-up call schedule
  - Clarify any support needed
```

---

### 1-2. Demo Reaction Assessment

**Immediately after demo**, evaluate emotional response on 3-level scale:

#### 🔥 Enthusiastic (Big Fan Signal)

**Indicators**:
- "Wow, this is exactly what I needed"
- "I can't believe this is ready in one week"
- "Can we add [feature] next?"
- Eyes light up during key moments
- Asks follow-up questions about capabilities
- Offers to try immediately

**Action**: Mark for **Iteration** path (1-week additional investment)

**User List Update**:
```json
{
  "user_id": "USER_001",
  "status": "mvp_delivered",
  "demo_date": "2024-02-11",
  "demo_reaction": "enthusiastic",
  "followup_scheduled": "2024-02-18"
}
```

#### 😐 Lukewarm (Pivot Signal)

**Indicators**:
- "This is nice" (but not excited)
- "I could use this, I guess"
- "Hmm, not quite what I expected"
- Takes time to warm up (requires explaining features)
- Asks clarifying questions but not enthusiastic ones
- "Interesting" (neutral word choice)

**Action**: Plan for **Pivot** (don't invest further, document learning)

**User List Update**:
```json
{
  "user_id": "USER_001",
  "status": "mvp_delivered",
  "demo_date": "2024-02-11",
  "demo_reaction": "lukewarm",
  "followup_scheduled": "2024-02-18"
}
```

#### 😞 Negative (Fast Pivot)

**Indicators**:
- "This isn't what I hoped for"
- "I'm not sure I'd actually use this"
- "It's missing the main thing I needed"
- Quiet, doesn't engage with questions
- Non-verbal cues: closed body language, minimal eye contact

**Action**: **Pivot immediately**, gather learning quickly

**User List Update**:
```json
{
  "user_id": "USER_001",
  "status": "mvp_delivered",
  "demo_date": "2024-02-11",
  "demo_reaction": "negative",
  "followup_scheduled": "urgent_debrief"
}
```

---

### 1-3. Demo Follow-up & Usage Period (Days 7-14)

**Goal**: Assess real-world impact over 1 week of actual use

**Process**:

#### Day 7 (Day After Demo)

Send follow-up email:

```markdown
Subject: Thanks for the demo! Some quick next steps...

Hi [User],

Thanks for the great feedback on the [MVP Name] demo yesterday. We loved seeing
your enthusiasm about [specific moment/feature].

Over the next week, we'd like you to **use the MVP for your actual workflow**
(replacing your current process). This helps us understand:

1. Does it work for real-world use (not just demo scenarios)?
2. What's missing after using it daily?
3. Would you recommend it to a colleague?

**Your mission**: Use [MVP] for your normal [TASK] this week instead of [OLD PROCESS].

### Usage Tips
- [Feature 1]: Best for [scenario]
- [Feature 2]: Try when you have [condition]
- [Support]: Reach out via Slack if you hit issues

### Next Check-in
**Follow-up call**: [DATE] at [TIME] (15 min)
- You share real-world experience
- We discuss what's working / what's missing
- We decide next steps together

Looking forward to learning from your experience!
```

---

#### Days 8-13

**Minimal involvement** (user's usage period):
- Monitor for critical issues
- Be available for quick questions
- Don't interrupt their workflow

---

#### Day 14 (Follow-up Call)

**Duration**: 15 minutes

**Agenda**:

```
[2 min] Opening & Recap
  - Thanks for trying it
  - Remind of original pain

[5 min] Usage Reality Check
  - "How often did you use it this week?"
  - "Did it replace your old process?"
  - "Any blocking issues?"

[3 min] Impact Assessment
  - "Has it saved you time?"
  - "Would you recommend to a colleague?"
  - "What's still missing?"

[3 min] Decision
  - Should we iterate (v1.1)?
  - Or pivot to different workflow?
  - What would make it essential?

[2 min] Next Steps
  - If iterate: Scope v1.1
  - If pivot: Learning debrief
```

---

## Section 2: MVP Tracking & Management

### 2-1. Folder Structure

**Organize all outputs in clear hierarchies**:

```
./
├── User Discover/                          # User management
│   ├── User List/
│   │   └── users.csv                      # User registry
│   └── User Interview/
│       ├── USER_001_2024-02-04.md          # JTBD
│       ├── USER_001_2024-02-04_ideation.md # Ideation
│       ├── USER_002_2024-02-05.md
│       └── ...
│
├── P-S Tree/                               # Problem-Solution Tree
│   ├── mvp-solutions.json                  # Central registry
│   └── [Business Function]/
│       └── [Problem]/
│           ├── [Solution].md               # MVP Proposal
│           ├── [Solution]_v1.0.md          # v1.0 changelog
│           ├── [Solution]_v1.1.md          # v1.1 changelog (if iterated)
│           └── ...
│
└── Learnings/                              # Documented insights
    ├── big-fans.md                         # Big Fan profiles
    ├── pivoted-projects.md                 # What failed & why
    └── workflow-patterns.md                # Patterns across interviews
```

---

### 2-2. User List Management

**File**: `./User Discover/User List/users.csv`

**Purpose**: Single source of truth for all users

**Structure**:

```json
[
  {
    "user_id": "USER_001",
    "name": "김철수",
    "business_function": "Marketing",
    "company": "ABC 스타트업",
    "company_type": "스타트업",
    "network_type": "closed",
    "referral": "직접 아는 사이",
    "interview_date": "2024-02-04",
    "status": "big_fan",  // scheduled → interviewed → go_approved → mvp_delivered → big_fan/pivot
    "years_of_experience": "3년차",
    "current_tools": ["Notion", "Google Analytics", "Excel"],

    // Interview Artifacts
    "jtbd_document": "./User Interview/USER_001_2024-02-04.md",
    "jtbd_status": "complete",

    // MVP Tracking
    "mvp_id": "MVP_001",
    "mvp_status": "delivered",
    "proposal_sent_date": "2024-02-05",
    "demo_date": "2024-02-11",
    "demo_reaction": "enthusiastic",  // enthusiastic / lukewarm / negative

    // Follow-up Tracking
    "followup_date": "2024-02-18",
    "usage_frequency": "daily",  // daily / several-times / once / never
    "shared_with_count": 2,  // How many colleagues did they mention to?
    "big_fan": true,

    // Iteration Planning (if Big Fan)
    "iteration_planned": true,
    "next_iteration_scope": "자동 리포트 발송",
    "testimonial": "이제 이거 없으면 일 못할 것 같아요",

    // Or Pivot Planning
    "pivot_reason": null,  // If pivoted, record why

    // Learning Notes
    "learning_notes": "마케터들은 시간 절약보다 분석 품질을 더 중요하게 생각함"
  }
]
```

**Status Values**:
- `scheduled`: Interview scheduled
- `interviewed`: JTBD complete
- `no_go`: Rejected at Go/No-Go decision
- `go_approved`: Approved for MVP
- `mvp_proposal_pending`: Waiting for proposal feedback
- `mvp_delivered`: Demo complete
- `big_fan`: Using regularly, shared with others (Iteration candidate)
- `pivot`: Not using or using minimally (Pivot decided)

---

### 2-3. MVP Solutions Registry

**File**: `./P-S Tree/mvp-solutions.json`

**Purpose**: Track all problems and solutions in one system

**Structure** (detailed):

```json
{
  "business_functions": [
    {
      "function_id": "BF_001",
      "function_name": "Marketing",
      "description": "Marketing teams planning, executing, and measuring campaigns",
      "industry_applicability": "All industries",
      "problems": [
        {
          "problem_id": "PROB_001",
          "problem_name": "Campaign Reporting",
          "problem_description": "Marketers spend 2 hours/week manually compiling campaign performance data",

          // AS-IS Workflow
          "as_is_workflow": [
            "Data extraction from GA, Facebook Ads, LinkedIn (30 min)",
            "Manual reconciliation of discrepancies (20-30 min)",
            "Analysis and report writing (30 min)"
          ],
          "workflow_frequency": "weekly",
          "workflow_pain_level": "high",

          // Problem-Level Metadata
          "related_users": ["USER_001", "USER_003"],
          "jtbd_documents": [
            "./User Interview/USER_001_2024-02-04.md",
            "./User Interview/USER_003_2024-02-10.md"
          ],

          // Deduplication & Universality
          "universality_signal": {
            "unique_users_with_problem": 2,
            "network_types": ["closed"],
            "universality_assessment": "high"  // Does problem appear across users?
          },

          "solutions": [
            {
              "mvp_id": "MVP_001",
              "solution_name": "AI Campaign Reporter",
              "solution_description": "Natural language interface for instant campaign analysis",

              // Proposal Tracking
              "proposal_document": "./P-S Tree/Marketing/Campaign_Reporting/AI_Campaign_Reporter.md",
              "proposal_status": "published",  // draft / published / revised
              "proposal_created_date": "2024-02-05",
              "proposal_sent_to_users": ["USER_001", "USER_003"],

              // MVP Status & Dates
              "status": "active",  // active / iteration / pivoted
              "created_date": "2024-02-04",
              "demo_date": "2024-02-11",
              "github_repo": "https://github.com/user/ai-campaign-reporter",
              "demo_url": "https://ai-campaign-reporter.vercel.app",

              // Technology Stack
              "tech_stack": {
                "frontend": ["Next.js", "React"],
                "backend": ["Python", "FastAPI"],
                "ai_model": "Claude API",
                "database": "Supabase PostgreSQL",
                "deployment": "Vercel + GCP"
              },

              // Feature Tracking
              "features_v1_0": [
                {
                  "feature_id": "FEAT_001",
                  "feature_name": "Unified Dashboard",
                  "status": "complete",
                  "user_feedback": "Essential, not missing anything"
                },
                {
                  "feature_id": "FEAT_002",
                  "feature_name": "Auto-Reconciliation",
                  "status": "complete",
                  "user_feedback": "Saves so much time on manual fixes"
                }
              ],

              // Impact & Performance
              "impact": {
                "time_saved_estimate": "2 hours → 15 minutes per use",
                "time_saved_annual": "~84 hours/year",
                "big_fan_users": ["USER_001"],
                "big_fan_count": 1,
                "usage_stats": {
                  "daily_active_users": 1,
                  "weekly_usage_rate": "100%",
                  "feature_adoption": {
                    "dashboard": "100%",
                    "auto_reconciliation": "85%",
                    "ai_insights": "95%"
                  }
                },
                "testimonials": [
                  {
                    "user": "USER_001",
                    "quote": "I can't imagine going back to the old way",
                    "context": "Post-demo, 1-week trial"
                  }
                ]
              },

              // Scalability Assessment
              "scalability": {
                "job_universality": "high",  // Do many people have this problem?
                "global_potential": "high",  // Can this be sold globally?
                "expansion_priority": "high", // Should we expand to other channels?
                "target_market": "All marketing teams with multi-platform campaigns",
                "estimated_market_size": "Large (100K+ potential users)"
              },

              // Iteration Log
              "iteration_log": [
                {
                  "version": "v1.0",
                  "date": "2024-02-11",
                  "status": "live",
                  "changes": "Initial MVP - Core features",
                  "key_metrics": {
                    "demo_reaction": "enthusiastic",
                    "usage_week_1": "daily"
                  }
                },
                {
                  "version": "v1.1",
                  "date": "2024-02-18",
                  "status": "planned",
                  "changes": "Automated report distribution, LinkedIn Ads integration",
                  "user_requests": [
                    "Save favorite report templates",
                    "Email reports on schedule"
                  ]
                }
              ],

              // Learning & Notes
              "learning": {
                "what_worked": [
                  "Natural language interface resonates with users",
                  "Time savings are immediately tangible",
                  "AI-generated insights are more useful than expected"
                ],
                "what_surprised_us": [
                  "Users wanted anomaly alerts, not requested originally",
                  "Data reconciliation explanation mattered more than perfect accuracy"
                ],
                "what_needs_improvement": [
                  "LinkedIn Ads API setup is complex for non-tech users",
                  "Mobile view needs work"
                ]
              }
            }
          ]
        },
        {
          "problem_id": "PROB_002",
          "problem_name": "Social Media Scheduling",
          "problem_description": "Marketers spend 30 min/day scheduling posts across platforms",
          "as_is_workflow": ["Write content", "Format for each platform", "Schedule manually"],
          "related_users": [],
          "solutions": []  // No MVP yet
        }
      ]
    }
  ],

  "summary": {
    "total_business_functions": 2,
    "total_problems": 3,
    "total_mvps": 2,
    "mvp_status_breakdown": {
      "active": 1,
      "iteration": 0,
      "pivoted": 1
    },
    "total_big_fans": 3,
    "high_priority_expansions": ["Marketing - Campaign Reporting"]
  }
}
```

---

### 2-4. P-S Tree File Organization

**Physical file structure**:

```
P-S Tree/
├── mvp-solutions.json
├── Marketing/
│   ├── Campaign_Reporting/
│   │   ├── AI_Campaign_Reporter.md        # Proposal
│   │   ├── AI_Campaign_Reporter_v1.1.md   # Feature additions (if iterated)
│   │   └── CHANGELOG.md                   # Version history
│   └── Social_Media_Scheduling/
│       └── [Future MVP]
└── Legal/
    └── Contract_Review/
        ├── AI_Contract_Reviewer.md
        └── CHANGELOG.md
```

**File Naming Conventions**:
- MVP Proposal: `[CamelCase_Solution_Name].md`
- Versions: `[SolutionName]_v1.1.md` or `[SolutionName]_v1.1_[FeatureName].md`
- Changelogs: `CHANGELOG.md` in each problem folder

---

### 2-5. Problem Deduplication & Matching

**Critical Process**: When JTBD is complete, check for existing similar problems

**Why This Matters**:
- Same problem in multiple users = strong Global Scalability signal
- Consolidates learning
- Prioritizes which workflows to build

#### Deduplication Steps

##### Step 1: Business Function Matching

Check if Business Function already exists in mvp-solutions.json:

```
New JTBD: USER_003 (Marketing, Campaign Reporting)
  ↓
Check: Does "Marketing" exist in P-S Tree?
  ↓
  ├─ YES: Go to Step 2
  └─ NO: Create new "Marketing" folder in P-S Tree
```

##### Step 2: Problem Matching

Within the Business Function, check for similar problems:

**Matching Criteria** (all should be ~80%+ match):
- Problem Name similarity: "Campaign Reporting" vs "캠페인 성과 분석"
- AS-IS Workflow similarity: Are main steps same?
- Pain Point similarity: Are root causes same?

**Example - MATCH**:
```json
// Existing Problem
{
  "problem_name": "Campaign Reporting",
  "as_is_workflow": ["Data extraction", "Reconciliation", "Analysis"]
}

// New JTBD
{
  "problem_name": "캠페인 성과 분석",
  "as_is_workflow": ["GA 데이터 추출", "엑셀 정리", "주간 리포트"]
}

→ These are the same underlying problem (different words, same workflow)
```

**Example - NO MATCH**:
```json
// Existing Problem
{
  "problem_name": "Campaign Reporting",
  "pain_points": ["Time-consuming data collection"]
}

// New JTBD
{
  "problem_name": "Campaign Strategy Planning",
  "pain_points": ["Lack of historical trend data"]
}

→ Different problems (reporting vs planning)
```

##### Step 3: User Confirmation

If potential match found, ask user:

```markdown
## 🔍 Problem Matching Check

We found a similar problem in our records:

**Existing**: Marketing - Campaign Reporting (USER_001)
- Pain: 2 hours/week on data compilation and analysis
- Workflow: GA → FB Ads → Excel → Report writing

**Your JTBD**: Marketing - 캠페인 성과 분석 (USER_003)
- Pain: Weekly campaign performance analysis and reporting
- Workflow: GA 추출 → 엑셀 정리 → 주간 리포트

**Question**: Are these the same problem, or different?

**Options**:
A) ✅ Same problem - consolidate (strengthen Global Scalability signal)
   - USER_001 and USER_003 both face this problem
   - Indicates "high universality"
   - MVP opportunity just increased in priority

B) ❌ Different problem - keep separate
   - One is about reporting, one is about analysis
   - Different solutions might be needed
```

##### Step 4: Update P-S Tree

**If CONSOLIDATE** (Option A):

```json
{
  "problem_id": "PROB_001",
  "problem_name": "Campaign Reporting",
  "related_users": ["USER_001", "USER_003"],  // ← Added USER_003
  "jtbd_documents": [
    "./User Interview/USER_001_2024-02-04.md",
    "./User Interview/USER_003_2024-02-10.md"  // ← Added
  ],
  "universality_signal": {
    "unique_users_with_problem": 2,  // ← Increased
    "universality_assessment": "high"  // ← Stronger signal
  }
}
```

**If SEPARATE** (Option B):

```json
{
  "problem_id": "PROB_004",
  "problem_name": "Campaign Performance Analysis (GA-Focused)",
  "related_users": ["USER_003"],
  "jtbd_documents": ["./User Interview/USER_003_2024-02-10.md"]
}
```

#### Deduplication Checklist

```markdown
## Problem Deduplication Checklist

For every new JTBD, verify:

- [ ] Is the Business Function new or existing?
- [ ] Do any Problems have >80% AS-IS Workflow similarity?
- [ ] Do Pain Points address the same root cause?
- [ ] Have you confirmed with user (consolidate vs separate)?
- [ ] Updated mvp-solutions.json with decision?
- [ ] If consolidated: Updated "related_users" and "universality_signal"?
```

---

## Section 3: Iteration vs Pivot Decision (Day 14)

### 3-1. Big Fan Criteria

**Big Fan Definition** (All three should be true):

#### 1. Reusability: Using the MVP Regularly

**Question**: "How often did you use the MVP this week?"

| Frequency | Signal | Decision |
|-----------|--------|----------|
| Daily (5+ uses/week) | 🔥 Strong | Big Fan candidate |
| Several times (2-4 uses/week) | ✅ Acceptable | Mild positive |
| Once per week | ⚠️ Minimal | Maybe not essential |
| Not at all | ❌ FAIL | Clear pivot |

**What to listen for**:
- "I used it every day"
- "I switched to using this instead of [old tool]"
- "Couldn't work without it now"

#### 2. Voluntary Sharing: Told Colleagues About It

**Question**: "Did you mention this to anyone on your team?"

| Behavior | Signal | Decision |
|----------|--------|----------|
| Proactively showed colleague | 🔥 Strong | Scalability indicator |
| Sent to teammate who has same problem | 🔥 Strong | Job universality confirmed |
| Talked about it casually | ✅ Good | Positive signal |
| Mentioned it when asked | ⚠️ Mild | Positive but not enthusiastic |
| Didn't mention to anyone | ❌ FAIL | Not valuable enough to share |

**What to listen for**:
- "I showed it to [colleague name]"
- "Our whole team is dealing with this"
- "I'm going to send them the link"

#### 3. "Cannot-Go-Back" Moment: Essential to Workflow

**Question**: "Could you go back to your old process now?"

| Response | Signal | Decision |
|----------|--------|----------|
| "No way, this is essential" | 🔥 Strong | Clear Big Fan |
| "I prefer this, but could manage" | ✅ Good | Positive but not critical |
| "It's fine, but not a must-have" | ⚠️ Mild | Utility question |
| "Honestly, I could go back" | ❌ FAIL | Not essential |

**What to listen for**:
- "I can't imagine going back"
- "This changed how I work"
- "Takes all the pain out of [task]"
- Emotional language: excited, relieved, grateful

---

### 3-2. Iteration vs Pivot Decision Logic

```
[Follow-up Call Complete]
    ↓
[Check All 3 Big Fan Criteria]
    ↓
    ├─ All 3 met (🔥🔥🔥) → ITERATION
    │   (Daily use + Shared + Cannot-go-back)
    │
    ├─ 2/3 met (✅✅) → ITERATION (with observation)
    │   (Almost Big Fan, slight concern but worth iterating)
    │
    ├─ 1/3 met (⚠️) → PIVOT
    │   (Usage ok but not enthusiastic; not reshaping their work)
    │
    └─ 0/3 met (❌) → FAST PIVOT
        (Clear miss; learn and move on)
```

---

### 3-3. Iteration Path (If Big Fan)

**Goal**: Enhance MVP based on real-world learnings

**Process**:

#### Week 1 (Follow-up Week)

1. **Gather Feature Requests**
   - "What would make v1.1 amazing?"
   - "Any pain points even with the MVP?"
   - "What are you still doing manually?"

2. **Prioritize v1.1 Features**
   - Pick 2-3 most-requested features
   - Estimate build time (should be 5-7 days)
   - Confirm feasibility

3. **Commit to Timeline**
   - "Let's add [Feature A] and [Feature B]"
   - "1-week build, demo Week 3"
   - Get user commitment

#### Week 2 (Build v1.1)

- Implement prioritized features
- Test with user (quick feedback loop)
- Prepare v1.1 demo

#### Week 3 (Demo v1.1)

- Show new features
- Measure additional impact
- Decide on next iteration or stabilization

---

### 3-4. Pivot Path (If Not Big Fan)

**Goal**: Document learning and move to next interview

**Process**:

#### Immediate (Day 14 Call)

1. **Understand Disconnect**
   - "What didn't work as expected?"
   - "What would have made it essential?"
   - "Was it a misunderstanding or genuinely not useful?"

2. **Categorize Pivot Reason**

| Category | What to Do |
|----------|-----------|
| **Wrong Problem Identified** | Go back to JTBD; reassess AI redesign potential |
| **Right Problem, Wrong Solution** | Brainstorm alternative approaches |
| **Solution OK, But Execution Issues** | Could be UX, not concept |
| **Low Job Universality** | This problem might not be common enough |

3. **Learning Documentation**
   - Record specific feedback in User List
   - Note what we got wrong
   - Identify patterns

#### Next Steps

- Close this MVP
- Move to next interview
- Revisit pivot reason when looking at related problems

**User List Update**:
```json
{
  "user_id": "USER_001",
  "status": "pivot",
  "followup_date": "2024-02-18",
  "usage_frequency": "1-2 times",
  "shared_with_count": 0,
  "pivot_reason": "Lukewarm reception - felt solution was on right track but implementation felt clunky",
  "specific_feedback": "Loved the concept but UI was too complex for quick access",
  "learning": "MVP UX matters as much as concept; this problem might need simpler interface",
  "recommend_retry": true,  // If we redesign UX
  "next_steps": "Revisit with improved UI in future"
}
```

---

## Section 4: Channel Expansion Strategy

### 4-1. Closed → Indirect → Public Progression

**Strategy**: Only expand to next channel once you have validation

#### Closed Network (Learning Phase)

**Purpose**: Build portfolio, understand workflows deeply

**Characteristics**:
- Target: People you know directly
- Scope: 5-10 interviews
- Success: Iterate to find product-market fit

**Metrics**:
- "Do we have Big Fans in this workflow?"
- "Can we articulate the universal problem?"

**Exit Criteria**:
- At least 1 Big Fan (validates product idea)
- Clear problem statement (validated across 2+ users)
- Repeatable solution (not one-off custom work)

---

#### Indirect Network (Validation Phase)

**Purpose**: Validate generalization beyond closed network

**Characteristics**:
- Target: Via communities, alumni networks, referrals
- Scope: 3-5 new interviews per problem domain
- Success: Scale insights from Closed

**Launch Strategy**:
- "I've been interviewing [your role] on [pain point]"
- "Found interesting patterns; want to validate?"
- Leverage testimonials from Closed (with permission)

**Metrics**:
- "Do we see the same problem in different companies?"
- "Do users from different backgrounds show Big Fan signal?"

**Exit Criteria**:
- Same problem confirmed in 2-3 different contexts
- Evidence of job universality (problem is domain-wide, not company-specific)
- MVP ready to expand to Public

---

#### Public Network (Scaling Phase)

**Purpose**: Reach global audience for validated problems

**Channels**:
- Twitter/X: Direct outreach to target job titles
- Reddit: Subreddits focused on role/industry
- ProductHunt: Launch MVP (if sophisticated enough)
- Industry communities: Slack groups, forums
- LinkedIn: B2B outreach

**Launch Criteria** (Must verify first):
- Clear problem statement validated across multiple users
- At least 1-2 Big Fans from Closed/Indirect
- MVP is polished enough for public demo
- Public testimonials ready (with permission)

---

### 4-2. Public Channel Expansion Rules

**Before expanding to Public, verify**:

```markdown
## Public Expansion Checklist

- [ ] Problem validated with ≥3 users across different contexts
- [ ] Big Fan signals detected (at least 1 user)
- [ ] Can clearly explain: "This problem is X, solution is Y"
- [ ] Job universality confirmed: "All [Role] face this problem"
- [ ] MVP is demo-ready (not rough prototype)
- [ ] Have testimonials from satisfied users
- [ ] Can handle influx of interviews (scaling team size?)

If any unchecked: NOT READY for Public expansion yet.
```

---

## Section 5: Big Fan Tracking & Learning

### 5-1. Big Fan Profile Development

**For each Big Fan, build detailed profile**:

**File**: `./Learnings/big-fans.md`

```markdown
# Big Fan Profiles

## User: USER_001 (김철수)
- **Role**: Marketing Manager
- **Company**: ABC Startup (Series A)
- **Problem**: Campaign Reporting (2 hours/week)
- **MVP**: AI Campaign Reporter

### Big Fan Signal
- ✅ Daily usage (analyzed campaigns 5+ times this week)
- ✅ Shared with team: Showed to 2 teammates
- ✅ Cannot-go-back: "Can't imagine manual process anymore"

### Usage Insights
- **Most-used feature**: Auto-reconciliation (uses daily)
- **Least-used feature**: Trend comparison (used once)
- **Feature requests**: Email scheduling, anomaly alerts
- **Workflow change**: Now analyzes mid-week (was Monday-only before)

### Iteration Input
- "Biggest pain now is export format"
- "Can we integrate with Slack?"
- "Would pay for this honestly"

### Scalability Potential
- **Similar roles in company**: 3 other marketers → product-market fit signal
- **Industry generalizability**: Campaign reporting universal in all marketing
- **Expansion channel**: Recommend public channel expansion
- **Timeline**: Ready to scale after v1.1

### Testimonial (with permission)
> "I can't imagine going back to the old way. AI Campaign Reporter is essential to my workflow now. Every marketer dealing with multi-platform campaigns needs this."
```

---

### 5-2. Learning Loop

```
[Complete Interview + JTBD]
          ↓
[Make MVP + Demo]
          ↓
[Follow-up + Big Fan Assessment]
          ↓
[Document Learning]
     ↙         ↘
[Big Fan]    [Pivot]
    ↓            ↓
[Iterate]    [Analyze Failure]
    ↓            ↓
[Expand?]    [Pattern Recognition]
             (Why did this fail?)
```

---

### 5-3. Extracting Patterns

**Every few interviews, pause and ask**:

1. **Problem Patterns**:
   - "What problems keep appearing?"
   - "Which job functions are most in pain?"
   - "Are there 2-3 universal problems?"

2. **Solution Patterns**:
   - "What kind of AI redesign works best?"
   - "Do users prefer automation or augmentation?"
   - "What features do Big Fans actually use?"

3. **Big Fan Patterns**:
   - "What characteristics do Big Fans share?"
   - "Do certain company types produce more Big Fans?"
   - "What's the minimum viable feature set for Big Fan status?"

4. **Scaling Patterns**:
   - "Which problems generalize to Public?"
   - "What's the conversion rate (Closed → Indirect → Public)?"

**Document in**: `./Learnings/workflow-patterns.md`

---

## Key Success Principles

### For Demo & Follow-up

1. **Manage Expectations**: Demo shows MVP, not final product
2. **Real Data**: Use their actual data in demo (if possible)
3. **Time Savings Tangible**: Show before/after side-by-side
4. **Genuine Feedback**: Ask what you actually want to know
5. **1-week Trial is Real**: Don't handhold; let them use it in real workflow

### For MVP Tracking

1. **Single Source of Truth**: mvp-solutions.json is the record
2. **User List is Living**: Update after every touchpoint
3. **Problem Deduplication**: Catch duplicates early (before building MVP)
4. **Folder Structure Mirrors Logic**: Easy to navigate and find things

### For Iteration vs Pivot

1. **Big Fan is the Goal**: Not "satisfied user" but "can't go back" user
2. **3 Criteria Matter**: All three (usage, sharing, essential) should be true
3. **Speed**: Decide quickly (same call, not days later)
4. **Learn from Pivots**: Every pivot teaches something about the problem space

### For Channel Expansion

1. **Earned Expansion**: Only move to next channel if you've earned it (Big Fans)
2. **Repeat Pattern**: Same methodology (interview → JTBD → MVP) at each stage
3. **Validation First**: Don't go public until problem is validated across contexts

---

## Common Pitfalls to Avoid

| Pitfall | What Goes Wrong |
|---------|-----------------|
| **Ignoring negative demo reaction** | Build v1.1 for user who doesn't care |
| **Premature Public launch** | Scaling too early; wasting effort on narrow problems |
| **No follow-up process** | Never learn if MVP actually works (vs demo hype) |
| **Unclear Big Fan criteria** | Subjective decisions; inconsistent approach |
| **Not tracking learnings** | Each project is isolated; no pattern recognition |
| **Keeping failed MVPs active** | Clutter in system; hard to see what works |
| **Wrong channel for problem** | Public launch before Indirect validation |

---

## Cross-Phase References

- **Phase 2**: Go/No-Go decision → which MVPs get built
- **Phase 3**: MVP Proposal questions → shape product design
- **Phase 4**: Demo reactions → determine iteration vs pivot
- **Tracking**: P-S Tree organizes all problems and solutions
- **Expansion**: Big Fans → prioritize problems for Public expansion

## Detailed References

- [references/followup-guide.md](references/followup-guide.md) - Demo & follow-up process
- P-S Tree structure - Organize problems and solutions
- User List (users.csv) - Track individual user journeys
