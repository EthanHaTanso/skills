# Workflow Collect - Phase Reference Files

This directory contains comprehensive phase reference guides for the workflow-collect skill, extracted and organized from the original user-discover skill documentation.

## Files Overview

### 1. phase1-interview-prep.md (280 lines)
**Purpose**: Guide for interview preparation and execution

**Key Sections**:
- Recruitment message templates (Closed/Indirect/Public networks)
- User List registration and management
- Interview question generation (2 versions)
- Interview execution guide
- Common recruitment patterns

**Use When**: Preparing for user interviews, creating recruitment messages, setting up question frameworks

---

### 2. phase2-jtbd.md (712 lines)
**Purpose**: JTBD document organization and MVP Go/No-Go decision criteria

**Key Sections**:

#### Part 1: JTBD Document Organization
- Conversational refinement approach
- 9-section JTBD structure (User Context → AI Redesign Opportunity)
- Question targeting strategy (host vs guest)
- Follow-up question organization
- Document storage and User List updates

#### Part 2: MVP Go/No-Go Decision
- Decision tree and gating criteria
- AI Redesign Potential assessment (CRITICAL)
  - Step compression capability
  - New possibilities creation
  - Value impact evaluation
- Technical Feasibility assessment
  - Implementation timeline estimation
  - Data accessibility verification
  - Technical constraint resolution
- Status updates and next steps

**Critical Decision Gate**: 
- Must pass BOTH AI Redesign Potential + Technical Feasibility
- Failing either = automatic NO-GO

**Use When**: Organizing interview data, assessing MVP viability, making go/no-go decisions

---

### 3. phase3-mvp-proposal.md (1,098 lines)
**Purpose**: MVP Ideation and user-facing MVP Proposal creation

**Key Sections**:

#### Part 1: MVP Ideation (Internal Document)
- Core problem synthesis
- Solution idea formulation
- Key features (3-5 max)
- Out of scope definition
- Expected impact quantification
- **CRITICAL: Technical feasibility research & validation**
  - Core technologies identification
  - Data accessibility checks
  - Feature feasibility assessment
  - Development timeline estimation
- Open questions tracking
- Status updates

#### Part 2: MVP Proposal (User-Facing Document)
- 9-section proposal structure:
  1. Your Current Situation (empathy + pain)
  2. Our Solution (simple, benefit-focused)
  3. How It Works (scenario-based walkthrough)
  4. Expected Impact (quantified + emotional)
  5. Out of Scope for v1.0 (transparent)
  6. Feedback Questions (5 specific questions)
  7. Technical Foundation (high-level only)
  8. Unconfirmed Items (transparency)
  9. Next Steps (clear commitment)

- Writing best practices
  - Language simplification rules
  - Before/after scenario structure
  - Emotion + data balance
  - DO's and DON'Ts
  - Quality checklist
- File storage and tracking updates

**Critical Principle**: MVP Proposal is user-friendly, not technical. Phase 1 content stays in JTBD.

**Use When**: Preparing MVP proposals, designing MVP features, gathering user feedback on scope

---

### 4. phase4-tracking.md (1,090 lines)
**Purpose**: Demo execution, follow-up processes, MVP tracking, and iteration/pivot decisions

**Key Sections**:

#### Part 1: Demo & Follow-up (Week 2)
- Demo execution structure (30 min)
- Reaction assessment (Enthusiastic / Lukewarm / Negative)
- 1-week usage period setup
- Follow-up call agenda (15 min)

#### Part 2: MVP Tracking & Management
- Folder structure organization
- User List management (status tracking, artifact links)
- MVP Solutions Registry (mvp-solutions.json structure)
- P-S Tree file organization
- **CRITICAL: Problem Deduplication & Matching**
  - Business Function matching
  - Problem matching criteria (80%+ similarity)
  - Consolidation vs separation decisions
  - Universality signal detection

#### Part 3: Iteration vs Pivot Decision (Week 3)
- Big Fan criteria (ALL THREE required):
  1. Regular reusability (daily use)
  2. Voluntary sharing (told colleagues)
  3. "Cannot-go-back" moment (essential)
- Decision logic and pathways
- Iteration path (feature request → v1.1)
- Pivot path (learning documentation)

#### Part 4: Channel Expansion Strategy
- Closed → Indirect → Public progression model
- Expansion validation checklist
- Exit criteria for each stage

#### Part 5: Big Fan Tracking & Learning
- Big Fan profile development
- Learning loop extraction
- Pattern recognition across interviews

**Critical Concepts**:
- Problem deduplication validates Global Scalability (same problem = multiple users)
- Big Fan requires all 3 criteria (usage + sharing + essential), not just one
- Learning from pivots is as important as iterations

**Use When**: 
- Running MVP demos
- Tracking user progress and MVP status
- Making iteration vs pivot decisions
- Planning channel expansion
- Documenting learnings and patterns

---

## Quick Reference: Which File to Use

| Task | Phase File | Section |
|------|-----------|---------|
| **Write recruitment message** | phase1 | 1-1 |
| **Register user to User List** | phase1 | 1-2 |
| **Create interview questions** | phase1 | 1-3 |
| **Organize interview data to JTBD** | phase2 | 1-1 to 1-4 |
| **Make Go/No-Go decision** | phase2 | 2-1 to 2-5 |
| **Create MVP Ideation** | phase3 | Part 1 |
| **Validate technical feasibility** | phase3 | 1-3 |
| **Write MVP Proposal** | phase3 | Part 2 |
| **Run MVP demo** | phase4 | 1-1 to 1-2 |
| **Conduct follow-up** | phase4 | 1-3 |
| **Track MVPs and users** | phase4 | 2-1 to 2-5 |
| **Deduplicate problems** | phase4 | 2-5 |
| **Decide iteration vs pivot** | phase4 | 3-1 to 3-4 |
| **Plan channel expansion** | phase4 | 4-1 to 4-2 |

---

## Workflow Overview

```
Phase 1 (Interview Prep)
├─ Recruit users (Closed/Indirect/Public)
├─ Register to User List
└─ Create interview questions

Phase 2 (JTBD + Go/No-Go)
├─ Conduct interview
├─ Organize to JTBD (9 sections)
├─ Assess Go/No-Go decision
│  ├─ Check: AI Redesign Potential (CRITICAL)
│  └─ Check: Technical Feasibility (CRITICAL)
├─ If NO-GO: Document and pivot
└─ If GO: Continue to Phase 3

Phase 3 (MVP Design)
├─ MVP Ideation (internal)
│  └─ Technical feasibility research
├─ MVP Proposal (user-facing)
└─ Get user feedback

Phase 4 (Demo, Iteration, Tracking)
├─ Demo (Day 7)
├─ Follow-up (Day 14)
│  ├─ If Big Fan (all 3 criteria) → Iterate (v1.1)
│  └─ If Not Big Fan → Pivot (document learning)
├─ Track in P-S Tree
├─ Check for problem deduplication
└─ Plan channel expansion (if Big Fan)
```

---

## Key Concepts by Phase

### Phase 1: Network Progression
- **Closed Network**: Learning phase (5-10 interviews)
- **Indirect Network**: Validation phase (3-5 new users per problem)
- **Public Network**: Scaling phase (big reach, once validated)

### Phase 2: AI Redesign Potential
- **NOT optimization** (speed up existing steps)
- **IS redesign** (compress steps, unlock new possibilities)
- **High Value Impact**: User can't go back to old way
- **Must pass both criteria** to advance to MVP

### Phase 3: User-Friendly Communication
- **JTBD** stays internal (details, specs, phase 1 content)
- **MVP Proposal** is for user (benefits, impact, no jargon)
- **Technical validation** happens during Ideation
- **Scope is ruthless** (5 features max)

### Phase 4: Three Critical Processes

#### Problem Deduplication
- Same problem across multiple users = strong scalability signal
- Consolidate related JTBD documents
- Increases MVP priority and expansion potential

#### Big Fan Identification
- Requires ALL THREE: daily usage + shared with colleagues + cannot-go-back
- Not just "satisfied" but "cannot imagine alternative"
- Foundation for iteration and expansion decisions

#### Iteration vs Pivot
- **Iterate**: Big Fan signals (invest v1.1)
- **Pivot**: Not Big Fan (learn and move on)
- Decision made on Day 14 call, not later

---

## Common Error Patterns

| Pattern | Risk | Mitigation |
|---------|------|-----------|
| **Confusing optimization with redesign** | Build features users don't need | Use Phase 2 criteria: step compression + new possibilities |
| **Vague JTBD** | MVP doesn't address real problems | Use 9-section structure; ask clarifying questions |
| **Over-scoped MVP** | Takes 4+ weeks; user loses interest | Phase 3: Max 5 features, ruthless prioritization |
| **Skipping technical research** | MVP can't be built in time | Phase 3.1-3: Do research before proposing |
| **No scope clarity in proposal** | User confused about what's being built | Phase 3 Part 2: Explicit "Out of Scope" section |
| **Premature Public launch** | Scaling narrow problems | Phase 4.4: Only expand after Indirect validation + Big Fan |
| **Wrong Big Fan criteria** | Iterate on products users don't love | Phase 4.3: Require ALL THREE criteria |
| **No problem deduplication** | Redundant MVPs, missed scalability signal | Phase 4.2-5: Check for matches before each MVP |

---

## File Dependencies

```
phase1-interview-prep.md
    ↓ (generates User List + JTBD raw data)
    
phase2-jtbd.md
    ├─ (outputs: JTBD document, Go/No-Go decision)
    ├─ If NO-GO: Stop
    └─ If GO: Continue to phase3
        ↓
phase3-mvp-proposal.md
    ├─ (reads: JTBD from phase2)
    ├─ (outputs: MVP Ideation, MVP Proposal)
    └─ If user approves: Continue to phase4
        ↓
phase4-tracking.md
    ├─ (reads: MVP Proposal from phase3)
    ├─ (outputs: Demo feedback, user status, MVP status)
    ├─ [Problem Deduplication Loop]
    │   └─ Can loop back to phase2 for new interview findings
    └─ [Channel Expansion]
        └─ May loop to phase1 for Indirect/Public recruitment
```

---

## Integration with Templates

These phase files work with the following template files (referenced throughout):

- `references/message-templates.md` - Recruitment message templates
- `references/interview-questions-tree.md` - Situation-based interview questions
- `references/interview-questions-framework.md` - JTBD framework-based questions
- `references/jtbd-template.md` - JTBD document structure
- `references/go-no-go-criteria.md` - Detailed evaluation framework
- `references/mvp-ideation-template.md` - Internal ideation structure
- `references/mvp-proposal-template.md` - User-facing proposal template
- `references/followup-guide.md` - Demo and follow-up process

---

## Version History

**Version 1.0** (Feb 2025)
- Extracted from user-discover skill SKILL.md
- Organized into 4 comprehensive phase files
- Added detailed processes for:
  - JTBD conversational refinement
  - Go/No-Go decision criteria
  - Technical feasibility validation
  - MVP proposal writing
  - Problem deduplication
  - Big Fan tracking
  - Channel expansion strategy

---

## Document Stats

| File | Lines | Words | Size |
|------|-------|-------|------|
| phase1-interview-prep.md | 280 | ~2,500 | 8.0K |
| phase2-jtbd.md | 712 | ~6,200 | 22K |
| phase3-mvp-proposal.md | 1,098 | ~9,500 | 33K |
| phase4-tracking.md | 1,090 | ~9,300 | 32K |
| **TOTAL** | **3,180** | **~27,500** | **95K** |

---

## How to Use This Documentation

### For Quick Reference
Use the "Quick Reference" table above to find which section covers your current task.

### For Learning the Full Workflow
Read phases in order: phase1 → phase2 → phase3 → phase4

### For Deep Dive on Specific Process
- **JTBD Creation**: phase2 section 1
- **Go/No-Go Decisions**: phase2 section 2
- **MVP Design**: phase3 parts 1-2
- **User Feedback & Iteration**: phase4 sections 1-3
- **Scalability & Expansion**: phase4 sections 4-5

### For Implementation
Keep these files open while:
1. Conducting interviews (reference phase1)
2. Organizing interview data (reference phase2)
3. Designing MVP (reference phase3)
4. Running demos and tracking progress (reference phase4)

---

Generated from user-discover skill documentation.
