# Reference Files Manifest

## Workflow-Collect Skill Reference Library
Complete set of phase guides extracted from user-discover skill.

---

## New Phase Reference Files (Created)

### phase2-jtbd.md
- **Status**: ✅ CREATED
- **Size**: 22K (712 lines)
- **Purpose**: JTBD Document Organization & MVP Go/No-Go Decision
- **Coverage**:
  - JTBD document organization (conversational refinement)
  - 9-section JTBD structure
  - Question targeting (host vs guest)
  - Follow-up question organization
  - User List status updates
  - Go/No-Go decision criteria
  - Technical feasibility assessment
  - Reference links to templates
- **Source**: Lines 325-494 from user-discover/SKILL.md

### phase3-mvp-proposal.md
- **Status**: ✅ CREATED
- **Size**: 33K (1,098 lines)
- **Purpose**: MVP Ideation & MVP Proposal Creation
- **Coverage**:
  - MVP Ideation purpose and structure (7 sections)
  - Core problem synthesis
  - Key features identification (3-5 max)
  - Out of scope definition
  - Technical feasibility research & validation
  - MVP Proposal 9-section template
  - Writing best practices (DO/DON'T guidelines)
  - File structure and storage
  - Quality checklist
  - Reference links to templates
- **Source**: Lines 498-869 from user-discover/SKILL.md

### phase4-tracking.md
- **Status**: ✅ CREATED
- **Size**: 32K (1,090 lines)
- **Purpose**: Demo, Follow-up, MVP Tracking & Big Fan Management
- **Coverage**:
  - Demo execution (30 min structure)
  - Reaction assessment (Enthusiastic/Lukewarm/Negative)
  - 1-week follow-up process
  - User List management
  - MVP Solutions Registry (mvp-solutions.json)
  - P-S Tree file organization
  - Problem deduplication & matching (CRITICAL PROCESS)
  - Big Fan criteria assessment (3 requirements)
  - Iteration vs Pivot decision logic
  - User status updates
  - Iteration path (v1.1 development)
  - Pivot path (learning documentation)
  - Channel expansion strategy (Closed → Indirect → Public)
  - Big Fan tracking & learning loops
  - Folder structure and file management
  - Reference links to templates
- **Source**: Lines 883-1445 from user-discover/SKILL.md (Sections 8-11)

---

## Existing Template Files (Pre-existing)

These templates are referenced throughout the phase files:

### message-templates.md (8.2K)
- Recruitment message templates
- Closed/Indirect/Public network variations
- Channel-specific language patterns
- Referenced by: phase1

### interview-questions-tree.md (11K)
- Situation-based question trees
- Pain point exploration structures
- Deep-dive question patterns
- Referenced by: phase1

### interview-questions-framework.md (14K)
- JTBD framework-based questions
- Customization elements
- Referenced by: phase1

### jtbd-template.md (18K)
- Complete JTBD structure template
- 9-section breakdown
- Example content for each section
- Referenced by: phase2

### go-no-go-criteria.md (11K)
- AI Redesign Potential assessment
- Technical Feasibility checklist
- Decision tree reference
- Referenced by: phase2

### mvp-ideation-template.md (8.3K)
- Internal ideation structure
- Feature planning template
- Technical feasibility section
- Referenced by: phase3

### mvp-proposal-template.md (12K)
- User-facing proposal structure
- 9-section breakdown
- Writing examples
- Referenced by: phase3

### followup-guide.md (14K)
- Demo and follow-up processes
- Big Fan assessment
- Referenced by: phase4

---

## Supporting Documents

### README.md (12K)
- Quick reference guide
- File overview and usage
- Workflow overview
- Quick reference table
- Key concepts by phase
- Common error patterns
- File dependencies
- Integration guide

### MANIFEST.md (This file)
- Complete inventory of all files
- File purposes and relationships
- Organization structure
- Completeness verification

---

## Organization Structure

```
/Users/sanhalee/.claude/skills/workflow-collect/references/
├── README.md                          # Quick reference & overview
├── MANIFEST.md                        # This file - inventory
│
├── phase1-interview-prep.md           # (Pre-existing)
├── phase2-jtbd.md                     # ✅ NEW
├── phase3-mvp-proposal.md             # ✅ NEW
├── phase4-tracking.md                 # ✅ NEW
│
├── message-templates.md               # (Pre-existing)
├── interview-questions-tree.md        # (Pre-existing)
├── interview-questions-framework.md   # (Pre-existing)
├── jtbd-template.md                   # (Pre-existing)
├── go-no-go-criteria.md              # (Pre-existing)
├── mvp-ideation-template.md           # (Pre-existing)
├── mvp-proposal-template.md           # (Pre-existing)
└── followup-guide.md                  # (Pre-existing)
```

---

## Content Summary by Phase

### Phase 1: Interview Preparation
- Recruitment message templates
- User List registration
- Interview question generation
- Interview execution

### Phase 2: JTBD & Go/No-Go (✅ NEW)
- Interview data organization
- JTBD document creation (9 sections)
- Go/No-Go decision gates
- Technical feasibility assessment
- User status tracking

### Phase 3: MVP Design (✅ NEW)
- MVP Ideation (internal planning)
- Technical research & validation
- MVP Proposal (user-facing)
- Feature prioritization
- Feedback collection

### Phase 4: Demo, Tracking & Expansion (✅ NEW)
- Demo execution
- Follow-up process
- User status tracking
- Problem deduplication
- Big Fan assessment (3-part criteria)
- Iteration vs Pivot decisions
- Channel expansion strategy
- Learning documentation

---

## File Completeness Verification

### Phase 2 Coverage Verification
- [x] Section 3 (JTBD Document Organization) - lines 325-390
- [x] Section 4 (MVP Go/No-Go Decision) - lines 392-494
- [x] JTBD organization process
- [x] Conversational refinement approach
- [x] Question targeting (host vs guest)
- [x] User List status updates
- [x] Go/No-Go decision criteria and process
- [x] Reference links to templates

### Phase 3 Coverage Verification
- [x] Section 5 (MVP Ideation) - lines 498-707
- [x] Section 6 (MVP Proposal Creation) - lines 710-869
- [x] MVP Ideation purpose and process
- [x] Technical feasibility research
- [x] MVP Proposal writing process
- [x] DO/DON'T guidelines
- [x] File structure and storage
- [x] Reference links to templates

### Phase 4 Coverage Verification
- [x] Section 8 (Demo & Follow-up) - lines 883-1007
- [x] Section 9 (MVP Tracking & Management) - lines 1010-1385
- [x] Section 10 (Channel Expansion) - lines 1387-1407
- [x] Section 11 (Big Fan Tracking) - lines 1410-1444
- [x] Follow-up process and timing
- [x] Big Fan assessment criteria
- [x] Iteration vs Pivot decisions
- [x] User List status updates
- [x] Problem deduplication process
- [x] Folder structure and file management
- [x] Channel expansion strategy
- [x] Reference links to templates

---

## Document Statistics

| File | Lines | Status | Purpose |
|------|-------|--------|---------|
| phase1-interview-prep.md | 280 | Pre-existing | Interview preparation |
| **phase2-jtbd.md** | **712** | **✅ NEW** | **JTBD & Go/No-Go** |
| **phase3-mvp-proposal.md** | **1,098** | **✅ NEW** | **MVP Design** |
| **phase4-tracking.md** | **1,090** | **✅ NEW** | **Demo & Tracking** |
| README.md | ~200 | ✅ NEW | Overview & guide |
| MANIFEST.md | ~150 | ✅ NEW | This inventory |
| Templates (8 files) | ~8,400 | Pre-existing | Support files |

**Total New Content**: ~3,250 lines (phase2 + phase3 + phase4)
**Total Reference Library**: ~12,000+ lines across all files

---

## Cross-References Map

### Phase 2 References
- Templates: `jtbd-template.md`, `go-no-go-criteria.md`
- Artifacts: User List, JTBD documents
- Next: phase3 (if GO decision)

### Phase 3 References
- Input: JTBD from phase2
- Templates: `mvp-ideation-template.md`, `mvp-proposal-template.md`
- Artifacts: MVP Ideation, MVP Proposal
- Next: phase4 (if user approves)

### Phase 4 References
- Input: MVP Proposal from phase3
- Templates: `followup-guide.md`
- Artifacts: P-S Tree, mvp-solutions.json, User List
- Loops: Problem deduplication (back to phase2), Channel expansion (back to phase1)

---

## Critical Processes Documented

### JTBD Conversational Refinement
- Question targeting strategy (host vs guest)
- Follow-up question organization
- Interactive refinement process
- Located in: phase2-jtbd.md section 1-1

### Go/No-Go Decision Criteria
- AI Redesign Potential assessment
- Technical Feasibility validation
- Status updates and next steps
- Located in: phase2-jtbd.md section 2

### MVP Technical Validation
- Core technologies identification
- Data accessibility checks
- Feature feasibility assessment
- Timeline estimation
- Located in: phase3-mvp-proposal.md section 1-3

### Problem Deduplication
- Business Function matching
- Problem matching criteria (80%+ similarity)
- Consolidation vs separation decisions
- Universality signal detection
- Located in: phase4-tracking.md section 2-5

### Big Fan Identification
- 3-part criteria (usage + sharing + essential)
- Decision logic and pathways
- User status updates
- Located in: phase4-tracking.md section 3

### Channel Expansion Strategy
- Closed → Indirect → Public progression
- Validation checkpoints at each stage
- Exit criteria for progression
- Located in: phase4-tracking.md section 4

---

## Usage Guide

### For Implementation
1. Start with README.md for overview
2. Reference phase files as you move through workflow:
   - Phase 1: Interview preparation
   - Phase 2: JTBD & Go/No-Go (phase2-jtbd.md)
   - Phase 3: MVP Design (phase3-mvp-proposal.md)
   - Phase 4: Demo & Tracking (phase4-tracking.md)

### For Quick Lookup
- Use README.md "Quick Reference" table
- Search for task name
- Go to indicated section

### For Deep Learning
- Read phase files in order (1 → 2 → 3 → 4)
- Each phase builds on previous
- Cross-references link related content

---

## Quality Assurance

### Content Verification
- [x] All requested sections extracted
- [x] Section numbers and line ranges match source
- [x] All templates referenced
- [x] Cross-references included
- [x] Examples and scenarios included
- [x] Key processes documented
- [x] Decision criteria explained
- [x] File structures specified
- [x] Best practices included

### Consistency Checks
- [x] Terminology consistent across files
- [x] Process flows match original documentation
- [x] Section numbering logical
- [x] References link to actual templates
- [x] Examples are relevant and useful
- [x] No duplicate content between phases

### Completeness Verification
- [x] Phase 2: All 2 sections (3-4) covered
- [x] Phase 3: All 2 sections (5-6) covered
- [x] Phase 4: All 4 sections (8-11) covered
- [x] Supporting README created
- [x] Manifest inventory created

---

## Version Information

**Creation Date**: February 5, 2025
**Source**: user-discover skill SKILL.md
**Extraction Method**: Manual content extraction and reorganization
**Format**: Markdown

**Phase Files**:
- phase2-jtbd.md v1.0
- phase3-mvp-proposal.md v1.0
- phase4-tracking.md v1.0

**Supporting Files**:
- README.md v1.0
- MANIFEST.md v1.0

---

## File Locations

**Directory**: `/Users/sanhalee/.claude/skills/workflow-collect/references/`

All files are located in this single directory for easy access and reference.

---

## Completeness Status

✅ **ALL REQUESTED FILES CREATED**

- [x] phase2-jtbd.md (22K, 712 lines)
- [x] phase3-mvp-proposal.md (33K, 1,098 lines)
- [x] phase4-tracking.md (32K, 1,090 lines)
- [x] Comprehensive README.md guide
- [x] This MANIFEST.md inventory

**Total**: 3 comprehensive phase guides + 2 supporting documents

---

## Next Steps

1. **Review**: Check files in `/Users/sanhalee/.claude/skills/workflow-collect/references/`
2. **Test**: Use phase files in actual workflow-collect operations
3. **Iterate**: Refine based on actual usage
4. **Expand**: Add additional templates or guides as needed

---

Generated: February 5, 2025
Source: user-discover skill documentation
