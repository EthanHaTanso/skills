---
name: product-development-workflow
description: End-to-end product development workflow from ideation to documentation. Use when user requests product planning, feature specification, prototyping, or wants to create/update product documentation in Korean. Supports React codebase integration with specialized agents for ideation (정책서), design (기능정의서), specification, coding, and documentation. Trigger for requests like "기획안 작성해줘", "프로토타입 만들어줘", "정책서 작성", "기능 정의서 업데이트", or Silicon Valley PM-style planning.
---

# Product Development Workflow

This skill provides a structured workflow for product development from initial ideation to final documentation, designed to maintain context across your codebase and product documents.

## Workflow Overview

The workflow follows these sequential stages:

1. **Ideation** → Policy Document (정책서)
2. **Design** → Feature Specification (기능정의서)
3. **Specification** → Technical Spec
4. **Coding** → Prototype Implementation
5. **Documentation** → Update all documents

## Agents

Each stage uses a specialized agent with specific expertise:

### 1. Ideation Agent
**Purpose**: Refine rough ideas into complete policy document (정책서) through interactive dialogue  
**Reference**: `references/ideation-agent.md`  
**Output**: Policy document defining Why/What/How

**When to use**:
- User has a rough idea or initial concept
- User requests "정책서 작성해줘"
- User wants help clarifying and structuring their thinking
- User asks for Silicon Valley PM-style planning

**Approach**:
Ideation Agent doesn't immediately write a document. Instead, it:
1. Asks thoughtful questions to understand the rough idea
2. Probes deeper into user problems and business value
3. Challenges assumptions and uncovers hidden aspects
4. Builds shared understanding through back-and-forth dialogue
5. Only creates the policy document once the idea is well-formed

**Usage**:
```
Read the Ideation Agent reference, then:
1. Start by asking 1-2 clarifying questions about the user's idea
2. Based on responses, ask follow-up questions to explore:
   - The real user problem and current workarounds
   - Business value and strategic rationale
   - Why now, and what success looks like
3. Progressively build understanding through conversation
4. Synthesize insights and create policy document when ready
```

**Expected Flow**:
- User shares rough idea → Agent asks questions
- User answers → Agent asks deeper questions
- Continue 2-5 exchanges until clarity is achieved
- Agent summarizes understanding for confirmation
- Agent creates complete policy document

### 2. Design Agent
**Purpose**: Transform policy into two detailed documents: UX-focused detailed policy + implementation-ready feature spec
**Reference**: `references/design-agent.md`
**Output**:
- Detailed Policy Document (상세 정책서) - UX principles and detailed flows
- Feature Specification (기능정의서) - User Stories and Acceptance Criteria
- UI Mockups/Prototypes (via frontend-design skill)

**When to use**:
- After policy document is approved
- User requests "기능정의서 작성해줘" or "상세 기획해줘"
- User wants detailed user flows and implementation specs

**Usage**:
```
Read the Design Agent reference, then follow this process:

STEP 1: Deep Dive Interview (심층 인터뷰)
Before writing any documents, conduct a thorough interview:

- Read the PRD file (@prd.md, README.md, or policy document)
- Use AskUserQuestion tool to conduct detailed interview covering:
  * Technical implementation details and feasibility
  * UI/UX decisions and interaction patterns
  * Edge cases and error handling scenarios
  * Design trade-offs and alternative approaches
  * Performance, scalability, and security concerns
  * Data structures and API requirements

- Questions must be:
  * NOT generic or clichéd (avoid "사용자 친화적", "좋은 UX" type questions)
  * Deep and specific (e.g., "이 화면에서 사용자가 뒤로가기를 누르면 작성 중인 데이터는 어떻게 처리되나요?")
  * Probing real uncertainties and assumptions
  * Revealing potential problems early

- Interview Examples:
  * ❌ Bad: "사용자가 편하게 사용할 수 있나요?"
  * ✅ Good: "10개 항목을 선택해야 하는데, 사용자가 5개만 선택하고 다른 페이지로 이동하면 선택 상태는 유지되나요?"
  * ❌ Bad: "에러 처리는 어떻게 하나요?"
  * ✅ Good: "API 호출이 실패했을 때 사용자가 이미 입력한 폼 데이터는 보존되나요, 아니면 다시 입력해야 하나요?"

- Continue interviewing until you have complete clarity on all aspects
- DO NOT start writing documents until the interview is complete

STEP 2: Create TWO documents based on interview insights

1. Detailed Policy Document (상세 정책서):
   - User psychology and expectations
   - UX principles (Output-First, Progressive Disclosure, etc.)
   - Detailed user flows with system responses
   - Edge cases and metrics

2. Feature Specification (기능 정의서):
   - User Stories (US-XXX format)
   - Acceptance Criteria (AC-XXX-XX format)
   - Data structures and field specifications
   - Detailed UI/UX specifications

STEP 3: (Optional) UI Mockups via frontend-design skill
   - After creating spec documents, use /frontend-design skill
   - Create high-fidelity UI mockups based on the feature spec
   - Generate production-ready component code with animations
```

**Output Structure**:
- Use `assets/detailed-policy-template.md` for detailed policy
- Use `assets/feature-spec-template.md` for feature specification
- Both documents work together: Policy explains "WHY/HOW", Spec defines "WHAT"

**IMPORTANT - frontend-design Skill Integration**:
When the user wants visual UI mockups or prototypes, invoke the `/frontend-design` skill after completing the spec documents. This skill:
- Creates distinctive, production-grade frontend interfaces
- Generates creative, polished React components
- Follows the Visual-First design principles
- Can be used to validate the feature spec visually before implementation

### 3. Specification Agent
**Purpose**: Create technical specification aligned with codebase  
**Reference**: `references/specification-agent.md`  
**Output**: Technical spec with component designs, APIs, and data models

**When to use**:
- After feature specification is complete
- User requests "스펙 문서 작성해줘"
- Before starting implementation

**Usage**:
```
Read the Specification Agent reference, then create a technical spec that:
1. Defines component structure following codebase patterns
2. Specifies TypeScript types and interfaces
3. Details data flow and state management
4. Identifies integration points with existing code
```

### 4. Coding Agent
**Purpose**: Implement full-stack features based on technical spec
**Reference**: `references/coding-agent.md`
**Output**: Production-ready full-stack code (React frontend + Python/Node.js backend)

**When to use**:
- After technical spec is complete
- User requests "프로토타입 만들어줘" or "코드 구현해줘"
- User wants to create actual implementation

**Usage**:
```
Read the Coding Agent reference, then implement:
1. Frontend: React components with TypeScript, proper error handling, accessibility
2. Backend: FastAPI/Express APIs with validation, database schema, service layer
3. Integration: API client setup, state synchronization, error handling consistency
4. Full-stack code that can be directly used in production
```

### 5. Documentation Agent
**Purpose**: Update all documentation to reflect final implementation  
**Reference**: `references/documentation-agent.md`  
**Output**: Updated policy docs, feature specs, and parent docs

**When to use**:
- After prototype is complete
- User requests "문서 업데이트해줘"
- Need to sync docs with actual implementation

**Usage**:
```
Read the Documentation Agent reference, then update:
1. Policy document with actual outcomes
2. Feature specification with final flows
3. Parent documents if needed (target customer, value proposition)
4. Add changelog entries and learnings
```

## Document Templates & Project Assets

The `assets/` folder contains both templates and actual project documents:

### Templates
- **Policy Document (PRD)**: `assets/policy-template.md` - Initial strategic document from Ideation Agent
- **Detailed Policy**: `assets/detailed-policy-template.md` - UX-focused detailed flows from Design Agent
- **Feature Specification**: `assets/feature-spec-template.md` - Implementation specs from Design Agent

### Project Folders
Project-specific folders store actual documents created using these templates:
- Example: `assets/Proact/` - Contains knowledge base, PRDs, and ideation logs for the Proact project
  - `README.md` - Folder structure and update workflow guide
  - `proact-knowledge-base.md` - Comprehensive product knowledge base
  - `prds/` - Completed PRD documents (organized by feature)
  - `raw/` - Session-specific ideation logs

### PRD Folder Structure (Feature-based)
PRD documents are organized by **feature folder**, not flat files:

```
prds/
├── opportunity-rating-tutorial/
│   ├── README.md           # 정책서 (Why/What/How)
│   ├── detailed-policy.md  # 상세 정책서 (UX flows)
│   └── feature-spec.md     # 기능정의서 (User Stories/AC)
├── opportunity-relevance-indicator/
│   ├── README.md
│   ├── detailed-policy.md
│   └── feature-spec.md
└── weekly-picks-outreach/
    ├── README.md
    ├── detailed-policy.md
    ├── feature-spec.md
    └── tech-spec.md        # (optional) 기술 스펙
```

**Naming Convention:**
- `README.md` - Main policy document (정책서)
- `detailed-policy.md` - Detailed UX policy (상세 정책서)
- `feature-spec.md` - Feature specification (기능정의서)
- `tech-spec.md` - Technical specification (기술 스펙, optional)

**When creating new features:**
1. Create a new folder with the feature name (kebab-case)
2. Add documents following the naming convention above
3. Also copy to the project's `docs/` folder for codebase integration

## Usage Patterns

### Pattern 1: Full Workflow (Ideation → Implementation → Documentation)

```
1. User provides product context and feature idea
2. Use Ideation Agent → Create policy document
3. Use Design Agent → Create feature specification  
4. Use Specification Agent → Create technical spec
5. Use Coding Agent → Implement prototype
6. Use Documentation Agent → Update all docs
```

### Pattern 2: Iterative Design Changes

```
1. User requests UX improvements on existing feature
2. Use Design Agent → Propose 3 improvement options
3. User selects option
4. Use Specification Agent → Update technical spec
5. Use Coding Agent → Implement changes
```

### Pattern 3: Documentation Sync

```
1. User has completed external changes (e.g., in Lovable)
2. Use Documentation Agent → Sync docs with current state
3. Update policy and feature specs to reflect reality
```

## Key Principles

### Context Preservation
- Always reference existing product documents (target customer, value proposition, core values)
- Check `assets/[project-name]/` for existing knowledge base and PRDs before starting new work
- Build on previous work rather than starting fresh each time
- Maintain document relationships and cross-references
- Update knowledge base after each ideation session to preserve learnings

### Codebase Integration  
- Follow existing React patterns and conventions
- Reuse existing components and utilities
- Match current file structure and naming
- Generate production-ready code that integrates smoothly

### User-Driven Design
- Start with user problems and JTBD
- Focus on user flows over isolated features
- Consider edge cases and error states
- Think like a Silicon Valley PM: business value + user experience

### Landing Page Design Principles
**Critical Rule: Visual-First, Text-Last**

When designing or implementing landing pages:

**❌ Avoid:**
- Text-heavy descriptions and long paragraphs
- Multiple bullet points explaining features
- Asking users to read before taking action
- "Enterprise brochure" style with walls of text
- Hiding CTAs at the bottom after long content

**✅ Instead:**
- **Show, Don't Tell**: Use interactive visualizations, animated data, live examples
- **CTA First**: Place actionable elements at the top, immediately visible
- **Visual Hierarchy**: Big icons/graphics → Short labels → Single metric/stat
- **Minimal Text**: 1-2 sentences max, use bullet separators (•) for keywords
- **Interactive Elements**: Hover effects, animations, clickable examples
- **Before/After Comparisons**: Visual contrasts instead of feature lists
- **Real Data Visualization**: Actual numbers, graphs, network diagrams over descriptions

**Example Transformation:**
```
❌ Bad:
"New to Government Contracting?
Government agencies are actively seeking the innovation
you've already delivered in the market. Validate your
market fit with real contract data and connect with B2G
veterans to navigate your entry."

✅ Good:
🚀 [Large Icon]
"New to GovCon"
"Find your first opportunities"
Validate • Meet guides • Start in 30 sec
[Explore →]
```

**Design Reference:**
- Stripe/Linear/Notion style: Minimal, interactive, visual-first
- Airbnb/Figma style: Social proof through visual examples
- Every screen should answer: "What can I DO right now?"

**Implementation:**
- Prefer animated graphs over text explanations
- Use interactive cards over static descriptions
- Show real examples (blurred if needed) over feature lists
- Visualize processes with diagrams, not step-by-step text

### Progressive Disclosure
- Read only the agent reference needed for current task
- Don't load all references at once
- Use templates as starting points
- Keep documents focused and modular

## Before Using This Skill

Ensure you have access to:
1. **Product context documents**: Target customer, value proposition, core values
   - For existing projects, check `assets/[project-name]/` folder for knowledge base and previous PRDs
2. **Codebase information**: File structure, patterns, existing components (if implementing)
3. **User research**: Feedback, insights, or problem statements (if available)

## Language Notes

- Policy documents and feature specs are written in **Korean**
- Code and technical specs use **English** for code/types with Korean comments/documentation
- Agent references are in **English** for consistency
