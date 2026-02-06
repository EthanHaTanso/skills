# JTBD Document Template

이 문서는 인터뷰 후 워크플로우를 정리하는 JTBD (Jobs-to-be-Done) 문서 템플릿입니다.

## 템플릿 사용 방법

1. 인터뷰 raw data (녹취록, 메모)를 읽습니다
2. 이 템플릿 구조에 맞춰 1차 초안을 자동 생성합니다
3. 불분명한 부분은 사용자에게 질문하며 대화형으로 보완합니다
4. 완성된 JTBD 문서를 User Interview 폴더에 저장합니다

---

## JTBD Document Structure

```markdown
# Interview: [User ID] - [Date]

## 1. User Context

### Basic Info
- **Name**: [인터뷰이 이름]
- **User ID**: [고유 식별자, 예: USER_001]
- **Business Function**: [직무/역할, P-S Tree 그룹핑 키]
- **Company**: [회사명]
- **Company Type**: [스타트업/대기업/외국계/프리랜서]
- **Network Type**: [closed / indirect / public]
- **Referral**: [소개자 또는 모집 채널]
- **Interview Date**: [YYYY-MM-DD]
- **Interview Duration**: [30분]

### Background
- **Years of Experience**: [경력]
- **Team Size**: [팀 규모]
- **Tools Used**: [현재 사용 도구들]
- **Prior Hints**: [사전에 알고 있던 pain point나 관심사]

---

## 2. Job (핵심 작업)

### Job Statement
When [상황/조건], I want to [수행하려는 작업], so that [최종 목적/결과].

**예시**:
- When 주간 캠페인이 종료되면, I want to 성과 데이터를 수집하고 분석해서, so that 경영진에게 리포트를 제출할 수 있다.

### Job Details
- **빈도**: [매일/매주/매월/ad-hoc]
- **소요 시간**: [하루/주/월 기준 총 시간]
- **중요도**: [High/Medium/Low]
- **최종 산출물**: [리포트, 대시보드, 문서 등]
- **산출물 사용자**: [경영진, 고객, 팀원 등]

---

## 3. AS-IS Workflow (현재 프로세스)

### Workflow Overview
[전체 플로우를 간단히 요약]

### Detailed Steps

#### Step 1: [단계 이름]
- **Description**: [이 단계에서 무엇을 하는지]
- **Input**: [필요한 입력 데이터/정보]
- **Tools**: [사용하는 도구]
- **Duration**: [소요 시간]
- **Output**: [산출물]
- **Pain Points**: [이 단계에서의 문제점]

#### Step 2: [단계 이름]
- **Description**:
- **Input**:
- **Tools**:
- **Duration**:
- **Output**:
- **Pain Points**:

[... 추가 단계들 ...]

### Workflow Diagram (Optional)
```
[Step 1] → [Step 2] → [Step 3] → [Step 4]
    ↓                      ↓
[Branch A]            [Branch B]
```

---

## 4. Context (작업 발생 조건)

### Triggers
- **What triggers this job?**: [이 작업을 시작하게 하는 계기]
- **예시**: "상사가 요청하면", "시스템 알림이 오면", "매주 월요일 오전"

### Prerequisites
- **What needs to be ready before starting?**: [작업 시작 전 필요한 것들]
- **예시**: "이전 주의 데이터가 모두 수집되어 있어야 함"

### Collaboration
- **Solo or Team work?**: [혼자/협업]
- **Dependencies**: [다른 사람이나 시스템에 의존하는 부분]

---

## 5. Pain Points (문제점)

### Primary Pain Points

#### Pain Point 1: [문제 이름]
- **Type**: [시간 소모 / 오류 발생 / 지루함 / 복잡함 / 대기 / 협업 문제]
- **Description**: [구체적 설명]
- **Impact**: [High / Medium / Low]
- **Frequency**: [얼마나 자주 발생하는지]
- **Current Workaround**: [현재 어떻게 대응하고 있는지]

#### Pain Point 2: [문제 이름]
- **Type**:
- **Description**:
- **Impact**:
- **Frequency**:
- **Current Workaround**:

[... 추가 Pain Points ...]

### Pain Point Priority
1. [가장 심각한 Pain Point]
2. [두 번째]
3. [세 번째]

---

## 6. Desired Outcome (원하는 결과)

### Ideal State
[이상적으로 이 작업이 어떻게 되면 좋겠는지]

**예시**:
- "버튼 클릭 한 번으로 자동 생성된 리포트를 받고 싶다"
- "데이터 수집 시간이 30분에서 5분으로 줄어들면 좋겠다"

### Expected Benefits
- **Time Savings**: [절약하고 싶은 시간]
- **Error Reduction**: [줄이고 싶은 오류]
- **Quality Improvement**: [개선하고 싶은 품질]
- **Other**: [기타 기대 효과]

### Success Criteria
[이 문제가 해결되었다고 판단할 수 있는 기준]

**예시**:
- "리포트 작성 시간이 절반으로 줄어든다"
- "오류율이 0%가 된다"
- "이 도구를 매일 사용하게 된다"

---

## 7. Technical Constraints (기술적 제약)

### Security & Policy
- **External Tools Allowed?**: [외부 도구 사용 가능 여부]
- **Data Export Restrictions**: [데이터 외부 전송 제약]
- **IT Approval Required?**: [IT 부서 승인 필요 여부]

### Data Access
- **Data Sources**: [데이터 위치 - DB, Excel, API 등]
- **Access Permissions**: [접근 권한]
- **API Available?**: [API 제공 여부]

### Technical Stack
- **Current Tools**: [현재 사용 중인 도구 스택]
- **Preferred Format**: [선호하는 형태 - 웹앱, 스크립트, No-code 등]
- **User Technical Level**: [사용자 기술 수준 - 코딩 가능 여부 등]

### Budget
- **Paid Tools Allowed?**: [유료 도구 사용 가능 여부]
- **Budget Approval Process**: [예산 승인 프로세스]

---

## 8. AI Redesign Opportunity (AI 재설계 기회)

### AI Redesign Potential
- **Can steps be compressed?**: [단계 압축 가능성]
  - **현재 단계 수**: [N개]
  - **압축 후 예상 단계 수**: [M개]
  - **어떻게 압축 가능한지**: [구체적 설명]

- **New possibilities enabled by AI?**: [AI로 가능해지는 새로운 것]
  - **예시**: "자연어로 질문하면 자동으로 분석 결과 제공"
  - **예시**: "이미지를 업로드하면 자동으로 데이터 추출"

- **"Can't go back" value impact**: [한 번 써보면 못 돌아가는 수준인가?]
  - **High**: 이전 방식으로 돌아갈 수 없을 정도로 혁신적
  - **Medium**: 훨씬 편하지만 이전 방식도 가능
  - **Low**: 약간의 개선 수준

### Workflow To-Be (AI 재설계 후)

#### 새로운 Workflow
```
[New Step 1] → [New Step 2] → [Done]
```

[AI가 어떻게 워크플로우를 개선하는지 구체적으로 설명]

---

## 9. MVP Scope (Go/No-Go 판단)

### Go/No-Go Decision
- [ ] **GO** - MVP 개발 진행
- [ ] **NO-GO** - MVP 개발 안 함

### 판단 기준 체크리스트

#### AI 재설계 가능성 (필수)
- [ ] 단계 압축 가능
- [ ] AI로 새로운 가능성 제공
- [ ] "못 돌아가는" Value Impact: High/Medium

#### 기술적 실현 가능성
- [ ] 1-2주 내 구현 가능
- [ ] 필요한 데이터 접근 가능
- [ ] 기술적 제약 해결 가능

#### 비즈니스 임팩트 (초기는 무시)
- Note: closed network는 학습용이므로 Global Scale은 고려하지 않음
- 직무 보편성은 나중에 indirect/public 확장 시 평가

### 판단 근거
[왜 GO 또는 NO-GO로 판단했는지 구체적 이유]

---

## 10. MVP Specification (GO인 경우)

### MVP Scope
[1-2주 내 구현할 범위]

**In Scope**:
- [포함할 기능 1]
- [포함할 기능 2]
- [포함할 기능 3]

**Out of Scope**:
- [제외할 기능 1 - 이유]
- [제외할 기능 2 - 이유]

### Delivery Format
- [ ] Web App (Vercel/Netlify)
- [ ] Script (Python/Node)
- [ ] Local App
- [ ] No-code (Zapier/Make)
- [ ] SDK/Library
- [ ] Claude Skill

[선택 이유]:

### Technical Approach
[간단한 기술 스택 및 접근 방식]

**Tech Stack**:
- Frontend:
- Backend:
- AI/ML:
- Deployment:

**Data Flow**:
```
[User Input] → [Processing] → [Output]
```

### Timeline
- **Interview Date**: [YYYY-MM-DD]
- **Target Demo Date**: [YYYY-MM-DD] (1주일 후)
- **Actual Demo Date**: [TBD]

---

## 11. Notes & Learnings

### Key Insights
[인터뷰에서 얻은 중요한 인사이트]

### Questions for Follow-up
[추가로 확인이 필요한 사항들]

### Similar Workflows
[비슷한 워크플로우를 가진 다른 직무나 산업]

---

## Document Metadata

- **Created**: [YYYY-MM-DD]
- **Last Updated**: [YYYY-MM-DD]
- **Status**: [Draft / In Review / Finalized / MVP In Development / MVP Delivered]
- **Related Documents**:
  - User List: [Link to User List entry]
  - P-S Tree: [Link to P-S Tree entry]
  - MVP Tracking: [Link to MVP Tracking entry]
```

---

## 대화형 보완 프로세스

JTBD 문서를 작성할 때, 질문 대상을 명확히 구분하여 효율적으로 보완합니다.

**질문 대상 구분**:
- **[인터뷰 호스트]**: 즉각 답변 가능 (비언어적 맥락, 관찰 사항 등)
- **[인터뷰 게스트]**: 비동기 확인 필요 (구체적 작업 내용, 도구, 시간 등)

---

### 1단계: 자동 초안 생성

raw data (녹취록, 메모)를 읽고 템플릿 구조에 맞춰 가능한 한 많이 채웁니다.

---

### 2단계: 불분명한 부분 식별 및 질문 대상 분류

불분명한 부분을 발견하면, 질문 대상을 구분합니다.

#### 2-1. [인터뷰 호스트]에게 즉각 질문

**비언어적 맥락 & 관찰 사항**:

**인터뷰이의 감정/태도**:
- "인터뷰이가 '[특정 작업]'을 언급할 때 특별히 짜증나는 표정이나 한숨을 쉬셨나요?"
- "어떤 pain point를 가장 강조하셨나요? (톤, 제스처 등)"

**인터뷰 당시 상황**:
- "화면 공유로 실제 작업을 보셨나요? 그렇다면 어떤 부분이 가장 눈에 띄었나요?"
- "인터뷰 중 인터뷰이가 실제로 [도구 이름]을 사용하는 걸 보셨나요?"

**누락된 맥락**:
- "인터뷰 중에 언급은 안 됐지만, 중요해 보이는 부분이 있었나요?"
- "인터뷰이의 회사 규모나 팀 구조에 대해 추가로 아시는 게 있나요?"

**우선순위 판단**:
- "여러 pain point 중 인터뷰이가 가장 해결하고 싶어하는 것은 무엇이었나요?"
- "인터뷰이가 특별히 '이게 자동화되면 정말 좋겠다'고 강조한 부분이 있었나요?"

---

#### 2-2. [인터뷰 게스트]에게 비동기 확인 필요

**구체적 작업 내용**:

**AS-IS Workflow가 불분명한 경우**:
- "Step 2에서 '데이터를 정제한다'고 하셨는데, 구체적으로 어떤 작업을 하시는 건가요?"
  - 예: 중복 제거? 결측치 처리? 포맷 변환?
- "이 단계에서 사용하는 도구가 언급되지 않았는데, 어떤 도구를 쓰시나요?"
- "Step 3에서 Step 4로 넘어갈 때 조건이 있나요? 항상 다음 단계로 진행하시나요?"

**Pain Point 구체화**:
- "오류가 발생한다고 하셨는데, 얼마나 자주 발생하나요? (매일/매주/가끔)"
- "시간이 오래 걸린다고 하셨는데, 정확히 얼마나 걸리시나요?"
- "'이 작업이 짜증난다'고 하셨는데, 구체적으로 어떤 부분이 가장 불편하신가요?"

**Desired Outcome 명확화**:
- "이상적으로는 어떻게 되면 좋겠다고 생각하시나요?"
- "시간이 절반으로 줄어드는 것만으로도 충분할까요, 아니면 거의 자동화되어야 할까요?"
- "만약 이 문제가 해결된다면, 어떤 점이 가장 좋을 것 같으세요?"

**Technical Constraints 확인**:
- "회사에서 외부 도구 사용에 제약이 있나요?"
- "데이터가 외부로 나가는 것에 문제가 있나요?"
- "API 접근이 가능한가요?"
- "IT 부서 승인 프로세스가 있나요?"

---

### 3단계: 단계별 보완

#### 3-1. 인터뷰 호스트 질문 (즉각 보완)

[인터뷰 호스트]에게 질문하고 답변을 즉시 문서에 반영합니다.

**예시**:
```
Q: "인터뷰이가 'Campaign Reporting'을 언급할 때 특별히 짜증나는 표정을 보이셨나요?"
A: "네, 매주 월요일마다 2시간씩 걸린다고 하면서 한숨을 쉬셨어요."

→ Pain Point에 추가: "빈도: 매주 월요일 / 감정: 매우 짜증 / 시간: 2시간"
```

#### 3-2. 인터뷰 게스트 질문 (비동기 확인 리스트)

[인터뷰 게스트]에게 물어봐야 할 질문을 **"Follow-up Questions for Guest"** 섹션에 정리합니다.

**문서에 추가할 섹션**:
```markdown
## Follow-up Questions for Guest

**목적**: JTBD 문서 완성을 위해 인터뷰 게스트에게 추가 확인이 필요한 사항

### AS-IS Workflow 관련
1. Step 2 '데이터 정제'에서 구체적으로 어떤 작업을 하시나요?
   - [ ] 중복 제거? 결측치 처리? 포맷 변환?
2. 각 단계에서 사용하는 도구가 무엇인가요?
   - [ ] Step 1: [?]
   - [ ] Step 2: [?]

### Pain Point 관련
3. 오류가 얼마나 자주 발생하나요?
   - [ ] 매일 / 매주 / 매월 / 가끔
4. [특정 작업]에 정확히 얼마나 시간이 걸리나요?
   - [ ] 약 [?]분/시간

### Technical Constraints 관련
5. 회사에서 외부 도구 사용에 제약이 있나요?
   - [ ] Yes / No
   - 제약이 있다면: [?]

**확인 방법**: 이메일, 메시지, 또는 짧은 후속 통화
**우선순위**: MVP Go/No-Go 판단에 필수적인 항목부터 확인
```

---

### 4단계: 문서 완성도 평가

#### 4-1. 즉시 완성 가능한 수준

[인터뷰 호스트]의 답변으로 다음이 채워지면 일단 문서를 완성합니다:
- ✅ 핵심 Pain Point 파악
- ✅ AS-IS Workflow 개요
- ✅ Desired Outcome 방향성
- ✅ 인터뷰이의 우선순위

**이 상태로도 Go/No-Go 1차 판단 가능**:
- AI 재설계 가능성은 대략적으로 평가 가능
- 세부 사항은 게스트 확인 후 정교화

#### 4-2. 게스트 확인 후 최종 완성

[인터뷰 게스트]에게 확인 후 다음을 업데이트:
- 구체적인 시간/빈도 수치
- 정확한 도구 스택
- 기술적 제약 조건 상세

**최종 확인 사항** (인터뷰 호스트):
- AS-IS Workflow가 인터뷰 당시 관찰/이해한 내용과 일치하는지
- Pain Points 우선순위가 인터뷰이의 강조 순서와 맞는지
- 누락된 중요한 맥락이 없는지

---

### 보완 전략 요약

```
┌─────────────────────────────────────────────────────────┐
│ Raw Data 분석                                           │
│ ↓                                                       │
│ 자동 초안 생성 (가능한 한 많이 채우기)                 │
│ ↓                                                       │
│ 불분명한 부분 발견                                      │
│ ↓                                                       │
│ ┌─────────────────┬─────────────────────────────┐     │
│ │ [인터뷰 호스트] │ [인터뷰 게스트]             │     │
│ │ (즉각 질문)     │ (비동기 확인 리스트)        │     │
│ │                 │                             │     │
│ │ - 비언어적 맥락 │ - 구체적 작업 내용          │     │
│ │ - 관찰 사항     │ - 정확한 시간/빈도          │     │
│ │ - 우선순위      │ - 도구 스택                 │     │
│ │ - 감정/태도     │ - 기술적 제약               │     │
│ │                 │                             │     │
│ │ → 즉시 반영     │ → Follow-up Questions 섹션  │     │
│ └─────────────────┴─────────────────────────────┘     │
│ ↓                                                       │
│ 1차 문서 완성 (Go/No-Go 판단 가능한 수준)              │
│ ↓                                                       │
│ 게스트 확인 후 최종 완성                                │
└─────────────────────────────────────────────────────────┘
```

---

### 실전 예시

**Raw data에서**: "데이터 정제가 너무 오래 걸려요"

**자동 초안**: Pain Point - 시간 소모

**[인터뷰 호스트]에게 질문**:
- "인터뷰이가 '오래 걸린다'고 할 때 얼마나 짜증나 보였나요?"
- "다른 pain point도 여러 개 언급했는데, 이게 가장 중요해 보였나요?"

**답변**: "네, 매우 짜증나 했고 이 부분을 가장 강조했습니다."

**[인터뷰 게스트]에게 비동기 확인 필요**:
```markdown
## Follow-up Questions for Guest
1. 데이터 정제에 정확히 얼마나 시간이 걸리나요?
2. 어떤 작업들을 하시나요? (중복 제거, 결측치 처리 등)
3. 사용하는 도구는 무엇인가요?
```

**1차 문서 완성**:
```markdown
## Pain Points
### Primary Pain Point 1: 데이터 정제 시간 소모
- **Type**: 시간 소모
- **Description**: 데이터 정제 작업에 상당한 시간 소요
- **Impact**: High (인터뷰이가 가장 강조)
- **Frequency**: [게스트 확인 필요]
- **Estimated Time**: [게스트 확인 필요]
```

**게스트 확인 후 최종**:
```markdown
## Pain Points
### Primary Pain Point 1: 데이터 정제 시간 소모
- **Type**: 시간 소모
- **Description**: CSV 파일에서 중복 제거, 결측치 처리, 포맷 변환
- **Impact**: High (인터뷰이가 가장 강조)
- **Frequency**: 매주 2-3회
- **Estimated Time**: 회당 1-1.5시간
- **Tools**: Excel (수동 작업)
```

---

## 문서 저장 위치

완성된 JTBD 문서는 다음 구조로 저장합니다:

```
./User Discover/
├── User List/
│   └── users.csv              # User ID, 기본 정보, status
├── User Interview/
│   ├── USER_001_2024-02-04.md  # 이 JTBD 문서
│   ├── USER_002_2024-02-05.md
│   └── ...
└── P-S Tree/
    ├── Marketing/               # Business Function
    │   ├── Campaign_Reporting.md  # Problem → Solution 매핑
    │   └── ...
    └── ...
```

---

## 예시: 완성된 JTBD 문서

[references/ 폴더에 example-jtbd.md 파일로 별도 제공]
