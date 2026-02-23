---
name: workflow-collect
description: |
  User workflow collection and MVP development pipeline for discovering Global Scalable product opportunities.

  Menu-driven workflow for collecting user pain points through interviews, organizing into JTBD documents,
  creating MVP proposals, and tracking Big Fan potential.

  Use when: User says "/collect", "워크플로우 수집", "인터뷰 준비", "JTBD 정리", "MVP 제안", or wants to
  work on any phase of the workflow collection process.

  Triggers: "/collect", "workflow collect", "워크플로우 수집", "인터뷰 준비", "JTBD 정리", "MVP 제안"
---

# Workflow Collection

User workflow collection system for discovering Global Scalable product opportunities through interviews,
JTBD documentation, and MVP validation.

## Core Philosophy

**Goal**: Build Global Scalable products
- **Global**: Not limited to specific regions
- **Scalable**: Products users want to share with others

**Strategy**: Fast execution with maximum meaningful attempts

**Principles**:
- Real workflow-based (not hypothetical)
- AI-powered redesign (workflow transformation, not just automation)
- Job-specific focus (create Big Fans who will share with colleagues)

## How to Use This Skill

This skill uses a **menu-based approach**. When you invoke `/collect`, you'll be presented with a menu
to select which phase you want to work on. No context analysis needed - just pick your phase and action.

### Phase Menu

When you use this skill, select the phase you're currently working on:

**1. 인터뷰 준비 (Interview Preparation)**
- Write recruitment messages (Closed/Indirect/Public networks)
- Register user to User List
- Generate interview question guide

**2. JTBD 정리 (JTBD Organization)**
- Organize interview raw data into JTBD document
- Evaluate Go/No-Go decision

**3. MVP 제안 (MVP Proposal)**
- Strategic validation (clarify:unknown + Rumsfeld Matrix)
- Create MVP Ideation document
- Write MVP Proposal for user

**4. 트래킹 & 폴로업 (Tracking & Follow-up)**
- Follow-up after demo
- Assess Big Fan potential
- View current status and analytics

---

## Phase 1: Interview Preparation

### 1-1. Write Recruitment Messages

**Purpose**: Create channel-appropriate invitation messages

**Process**:
1. Identify target channel (Closed/Indirect/Public)
2. Identify target job function
3. Generate message using [references/message-templates.md](references/message-templates.md)
4. Customize with user

**Key Differences by Channel**:
- **Closed**: Simple and friendly, mention portfolio building
- **Indirect**: Include survey, build trust, pre-collect workflow info
- **Public**: Emphasize portfolio + testimonial, job-specific targeting

**Reference**: [references/message-templates.md](references/message-templates.md)

---

### 1-2. Register User to User List

**Purpose**: Track interviewee information before interview

**Required Info**:
- Name, Job function, Company, Company type
- Network path (closed/indirect/public)
- Interview scheduled date

**Optional Info**:
- Years of experience, Prior hints, Current tools

**File**: `./User Discover/User List/users.json`

**Reference**: [references/phase1-interview-prep.md](references/phase1-interview-prep.md)

---

### 1-3. Generate Interview Questions

**Purpose**: Create customized question guide based on interviewee info

**Two Versions Available**:
- Situational question tree: [references/interview-questions-tree.md](references/interview-questions-tree.md)
- Framework + examples: [references/interview-questions-framework.md](references/interview-questions-framework.md)

**Customization**:
- Reflect job-specific pain points
- Adjust for company type (startup/enterprise)
- Add questions based on prior hints

**Reference**: [references/phase1-interview-prep.md](references/phase1-interview-prep.md)

---

## Phase 2: JTBD Organization

### 2-1. Organize Interview into JTBD

**Purpose**: Transform raw interview data into structured JTBD document

**Process** (conversational refinement):
1. Auto-generate draft from raw data
2. Ask clarifying questions for unclear parts
   - **Ask interview host immediately**: Non-verbal context, observations, priorities
   - **Ask interview guest asynchronously**: Add to "Follow-up Questions" section
3. Refine through dialogue
4. Save to `./User Discover/User Interview/[USER_ID]_[YYYY-MM-DD].md`
5. Update User List status: `scheduled` → `interviewed`

**JTBD Structure**:
1. User Context
2. Job (core task)
3. AS-IS Workflow
4. Context (when task occurs)
5. Pain Points
6. Desired Outcome
7. Technical Constraints
8. AI Redesign Opportunity
9. MVP Scope

**Template**: [references/jtbd-template.md](references/jtbd-template.md)
**Detailed Guide**: [references/phase2-jtbd.md](references/phase2-jtbd.md)

---

### 2-2. Evaluate Go/No-Go Decision

**Purpose**: Decide if workflow is worth MVP development

**Decision Criteria**:

**Must Pass: AI Redesign Potential**
- Can compress multiple steps into one?
- Enables new possibilities?
- "Can't go back" level value impact?

**Supporting: Technical Feasibility**
- Implementable in 1-2 weeks?
- Data accessible?
- Constraints solvable?

**Result**:
- ✅ **GO**: High AI redesign potential + feasible → Proceed to MVP Ideation
- ❌ **NO-GO**: Low redesign potential or not feasible → Pivot

**Criteria Details**: [references/go-no-go-criteria.md](references/go-no-go-criteria.md)

---

## Phase 3: MVP Proposal

### 3-0. Strategic Validation

**Purpose**: Validate strategic direction and feasibility before investing in detailed ideation

**When**: After JTBD GO decision, before MVP Ideation

**Process**:
1. **Invoke `Skill(skill: "clarify:unknown")`** with JTBD document as input
2. Categorize existing knowledge into Rumsfeld Matrix (Known Known / Known Unknown / Unknown Known / Unknown Unknown)
3. Present matrix to user for review
4. Conduct deep interview (3-5 rounds) guided by the matrix:
   - Round 1: Known Unknowns — fill explicit gaps
   - Round 2: Unknown Knowns — surface implicit assumptions
   - Round 3: Unknown Unknowns — explore blind spots (failure modes, competition, timing)
5. Evaluate strategic fit:
   - AI Redesign potential (workflow transformation, not just automation)
   - Big Fan feasibility ("can't go back" mechanism)
   - 1-week MVP feasibility (can core value be delivered?)
   - Scalability signal (multiple users with same problem?)
6. Present GO/PIVOT recommendation with reasoning

**Output**: Strategic validation summary (appended to JTBD or saved separately)
- Rumsfeld Matrix (resolved)
- Strategic fit assessment
- GO/PIVOT recommendation
- Key constraints and risks for Ideation to address

**Guide**: [references/strategy-guide.md](references/strategy-guide.md)

---

### 3-1. Create MVP Ideation

**Purpose**: Quickly organize core ideas before writing detailed proposal (internal doc)

**Content** (30-45 min total):
1. Core Problem (top 3 pain points)
2. Core Solution Idea (1-2 sentences)
3. Key Features (3-5 features for v1.0)
4. Out of Scope (v1.1+ features)
5. Expected Impact (quantitative + qualitative)
6. Open Questions (if any)
7. **Technical Feasibility** (15-20 min research)
   - Core technologies identified
   - Development timeline estimated
   - Risks and mitigation plans

**File**: `./User Discover/User Interview/[USER_ID]_[DATE]_ideation.md`

**Template**: [references/mvp-ideation-template.md](references/mvp-ideation-template.md)
**Detailed Guide**: [references/phase3-mvp-proposal.md](references/phase3-mvp-proposal.md)

---

### 3-2. Write MVP Proposal

**Purpose**: User-friendly proposal to build excitement and align on scope

**Main Goals**:
- Build excitement about MVP impact
- Increase AS-IS vs TO-BE clarity
- Define clear scope

**Sub Goals**:
- Scope out unimportant flows
- Get feedback on unconsidered aspects

**Content Sections**:
1. Current Situation (pain points with concrete examples)
2. Our Solution (core idea + key features)
3. How It Works (usage scenario)
4. Expected Impact (time saved, Big Fan potential)
5. Out of Scope (v1.0 limitations + feedback questions)
6. Technical Feasibility (validated tech stack)
7. Next Steps (demo timeline)
8. Unconfirmed Items (follow-up questions from JTBD)
9. One-line Summary

**File**: `./P-S Tree/[Business Function]/[Problem]/[Solution].md`

**Template**: [references/mvp-proposal-template.md](references/mvp-proposal-template.md)
**Detailed Guide**: [references/phase3-mvp-proposal.md](references/phase3-mvp-proposal.md)

---

## Phase 4: Tracking & Follow-up

### 4-1. Follow-up After Demo

**Timing**: 1 week after demo (Day 14)

**Purpose**:
1. Check if actually using MVP
2. Check if shared with others (Big Fan validation)
3. Decide: Iteration vs Pivot

**Reactions**:
- 🔥 **Enthusiastic** (Big Fan) → Invest 1 more week for iteration
- 😐 **Lukewarm** → Pivot to next interviewee
- 😞 **Negative** → Fast pivot, record learning

**Update User List**: Status → `big_fan` or `pivot`

**Guide**: [references/followup-guide.md](references/followup-guide.md)
**Detailed Guide**: [references/phase4-tracking.md](references/phase4-tracking.md)

---

### 4-2. Assess Big Fan Potential

**Big Fan Signals**:
- Daily usage (4-5 times/week)
- Voluntary sharing with colleagues (1+ times)
- "Can't go back" level dependency

**Value**:
- Indicates scalability within job function
- Priority for Public channel expansion
- Source of testimonials

**Detailed Guide**: [references/phase4-tracking.md](references/phase4-tracking.md)

---

### 4-3. View Current Status

**Available Views**:
- Current interviews in progress
- Jobs with Big Fans identified
- Public channel expansion priorities
- Problem deduplication (multiple users with same workflow)

**Files**:
- `./User Discover/User List/users.json` - All users and status
- `./P-S Tree/mvp-solutions.json` - Problems, solutions, and analytics

**Detailed Guide**: [references/phase4-tracking.md](references/phase4-tracking.md)

---

## Folder Structure

```
./
├── User Discover/
│   ├── User List/
│   │   └── users.json                    # User tracking
│   └── User Interview/
│       ├── USER_001_2026-02-04.md        # JTBD docs
│       ├── USER_001_2026-02-04_ideation.md  # MVP Ideation (internal)
│       └── ...
│
└── P-S Tree/                             # Problem-Solution Tree
    ├── mvp-solutions.json                # Analytics & tracking
    └── [Business Function]/
        └── [Problem]/
            └── [Solution].md             # MVP Proposals (user-facing)
```

---

## Reference Files Index

**Phase 1: Interview Preparation**
- [phase1-interview-prep.md](references/phase1-interview-prep.md) - Complete Phase 1 guide
- [message-templates.md](references/message-templates.md) - Recruitment message templates
- [interview-questions-tree.md](references/interview-questions-tree.md) - Situational questions
- [interview-questions-framework.md](references/interview-questions-framework.md) - Framework-based questions

**Phase 2: JTBD Organization**
- [phase2-jtbd.md](references/phase2-jtbd.md) - Complete Phase 2 guide
- [jtbd-template.md](references/jtbd-template.md) - JTBD document template
- [go-no-go-criteria.md](references/go-no-go-criteria.md) - Decision criteria

**Phase 3: MVP Proposal**
- [strategy-guide.md](references/strategy-guide.md) - Strategic validation guide (clarify:unknown + Rumsfeld Matrix)
- [phase3-mvp-proposal.md](references/phase3-mvp-proposal.md) - Complete Phase 3 guide
- [mvp-ideation-template.md](references/mvp-ideation-template.md) - Ideation template
- [mvp-proposal-template.md](references/mvp-proposal-template.md) - Proposal template

**Phase 4: Tracking & Follow-up**
- [phase4-tracking.md](references/phase4-tracking.md) - Complete Phase 4 guide
- [followup-guide.md](references/followup-guide.md) - Follow-up and Big Fan assessment

---

## Key Principles

### Critical Success Factors

1. **Deep Understanding**: Interview to deeply understand user's situation/context
2. **AI Redesign First**: Focus on AI-powered workflow transformation, not simple automation
3. **Big Fan Focus**: Goal is creating 1 Big Fan who will share with colleagues
4. **Fast Iteration**: Quick attempts and learning

### Common Pitfalls to Avoid

- ❌ Confusing simple automation with AI redesign
- ❌ Skipping unclear parts during JTBD organization
- ❌ Investing in iteration despite lukewarm response
- ❌ Expanding to Public channels without Big Fans
- ❌ Documentation overhead slowing down execution

---

## Channel Expansion Strategy

**Closed Network** (Learning):
- Target: People you know directly
- Purpose: Build portfolio + learn workflows

**Indirect Network** (Validation):
- Target: Communities, referrals
- Purpose: Build trust + pre-collect workflow info
- Leverage: Portfolio from Closed

**Public Network** (Scaling):
- Target: X, Reddit (job-specific targeting)
- Purpose: Acquire global users
- Leverage: Portfolio + Testimonials
- Priority: Jobs where Big Fans were found in Closed

---

## Balanced Automation

This skill balances automation and conversation:

**Automated** (core tasks):
- Template-based document generation
- Checklist auto-evaluation
- Data structuring

**Conversational** (thinking required):
- Customized question guide generation
- JTBD refinement through dialogue
- Big Fan assessment and iteration decisions
