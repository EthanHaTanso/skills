# Strategic Validation Guide

## Purpose

Validate strategic direction and feasibility of a GO-approved JTBD before investing in detailed MVP Ideation. This step stress-tests the idea to prevent wasted effort on poorly-scoped or strategically misaligned MVPs.

## When to Use

- After JTBD GO decision (Phase 2-2 complete)
- Before MVP Ideation (Phase 3-1)

## Input

- JTBD document (from Phase 2)
- Go/No-Go decision context
- Any available user interview data

## Process

### Step 1: Knowledge Structuring
**Invoke `Skill(skill: "clarify:unknown")` and follow its instructions.**

Input: the JTBD document and all available user context.

Output: Rumsfeld Matrix — existing knowledge categorized into 4 quadrants with action strategies per quadrant.

Present the matrix to the user for review before proceeding.

### Step 2: Strategic Deep Interview
Conduct a thorough interview using AskUserQuestion tool, guided by the Rumsfeld Matrix:

**Round 1: Known Unknowns** (highest priority — we know we don't know these)
- Questions that fill explicit gaps in the JTBD
- Technical feasibility, resource constraints, timeline realism
- User's actual frequency and severity of pain

**Round 2: Unknown Knowns** (implicit assumptions — surface what's unspoken)
- Challenge "obvious" decisions: "왜 이 접근이 당연한가요?"
- Probe assumptions about the user's workflow
- Identify domain knowledge that hasn't been documented

**Round 3: Unknown Unknowns** (blind spots — divergent exploration)
- Competitive landscape: "이걸 이미 하고 있는 곳이 있나요? 왜 안 됐나요?"
- Failure modes: "이게 실패한다면 가장 가능성 높은 원인은?"
- User behavior: "유저가 이걸 쓰다가 포기하는 시나리오는?"
- Market timing: "왜 지금이어야 하나요? 6개월 뒤면 늦나요?"

**Interview Rules:**
- Questions MUST NOT be generic or cliché — probe deeply, challenge assumptions
- Follow up on every ambiguity — do not accept surface-level answers
- Continue until ALL quadrants are sufficiently addressed
- After each round, update the Rumsfeld Matrix — move items between quadrants as knowledge evolves
- Maximum 3-5 rounds total

### Step 3: Strategic Fit Assessment
Explicitly evaluate against the project's core criteria:

1. **AI Redesign Potential**: Is this genuinely a new workflow enabled by AI, or just automation of an existing process?
2. **Big Fan Feasibility**: Can this create users who "can't go back"? What's the irreversibility mechanism?
3. **1-Week MVP Feasibility**: Can the core value be delivered in 1 week? If not, what's the minimal slice?
4. **Scalability Signal**: Is this problem specific to one user, or do multiple users in the same role share it?
5. **Strategic Fit**: Does this align with the broader strategy and current phase goals?

Present the assessment to the user with a clear **GO / PIVOT** recommendation.

### Step 4: Output

Produce a strategic validation summary to hand off to MVP Ideation (3-1):

```markdown
## Strategic Validation Summary

### Rumsfeld Matrix (Resolved)
| Quadrant | Items | Resolution |
|----------|-------|------------|
| Known Known | ... | Confirmed |
| Known Unknown | ... | Resolved via interview |
| Unknown Known | ... | Surfaced |
| Unknown Unknown | ... | Explored |

### Strategic Fit Assessment
1. AI Redesign: {GO/CAUTION} — {reasoning}
2. Big Fan Feasibility: {GO/CAUTION} — {reasoning}
3. 1-Week MVP: {GO/CAUTION} — {reasoning}
4. Scalability Signal: {GO/CAUTION} — {reasoning}
5. Strategic Fit: {GO/CAUTION} — {reasoning}

### Recommendation: {GO / PIVOT}
{1-2 sentence reasoning}

### Key Constraints for Ideation
- {constraint 1}
- {constraint 2}

### Remaining Risks
- {risk 1}
- {risk 2}
```

If **GO**: proceed to MVP Ideation (3-1) with this summary as context.
If **PIVOT**: document reasoning, suggest alternative direction, update JTBD status.

## Question Style Guidelines

### Good Questions
- **Specific & Evidence-Based**: "이 50% 절감 수치는 어떻게 측정했나요? 실제 데이터인가요?"
- **Trade-off Revealing**: "이 기능을 넣으면 1주 내 빌드가 가능한가요? 빼야 할 건 뭔가요?"
- **Assumption-Challenging**: "유저가 정말 매일 이걸 쓸까요? 주 1회 사용 시나리오는 고려했나요?"
- **Failure-Exploring**: "경쟁사가 내일 같은 걸 출시하면 우리 차별점은 뭔가요?"

### Avoid
- Leading questions that assume the answer
- Too many questions at once (max 2-3 per round)
- Generic questions applicable to any product
- Questions about implementation details (that's for Ideation/Dev phases)

## Key Principles

1. **Be the Devil's Advocate** — your job is to stress-test the idea, not validate it
2. **Evidence Over Intuition** — push for data, quotes, or concrete examples
3. **Strategic Lens** — always evaluate against the broader product/business context
4. **Respect the User's Time** — be thorough but efficient; don't repeat questions
5. **Clear Output** — the summary should give MVP Ideation clear direction without further clarification
