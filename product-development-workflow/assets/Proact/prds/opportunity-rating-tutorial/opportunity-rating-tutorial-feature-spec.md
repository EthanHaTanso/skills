# Opportunity Rating Tutorial 기능 정의서 (Feature Specification)

**Last Updated**: 2026년 1월 30일
**Version**: v2.1 (AI Curation 기능 반영)

## 문서 개요

이 문서는 Proact 온보딩의 Opportunity Rating Tutorial 기능을 정의합니다.

**Related Documents**:
- PRD 문서: `opportunity-rating-tutorial.md`
- 상세 정책서: `opportunity-rating-tutorial-detailed-policy.md`
- 관련 기능: LLM Curation Spec (`docs/specs/llm-filtered-opportunities-streaming.md`)

---

## US-001: 튜토리얼 진입 - 로딩 중 튜토리얼 표시

### 사용자 스토리

사용자로서, Company Profile을 확인한 후 Opportunity가 로딩되는 동안 튜토리얼을 통해, 다음 단계에서 무엇을 해야 하는지 미리 파악하고 싶습니다.

### Acceptance Criteria

#### AC-001-01: 튜토리얼 트리거

- Company Profile "Confirm" 버튼 클릭 시 튜토리얼 화면으로 전환
- 기존 로딩 스피너("Loading matching opportunities...") 대신 튜토리얼 표시
- 백그라운드에서 Opportunity 로딩 API 호출 진행

#### AC-001-02: 튜토리얼 레이아웃

- **전체 화면** 튜토리얼 오버레이
- 레이아웃 구성:

| 영역 | 위치 | 내용 |
|------|------|------|
| Skip 버튼 | 우측 상단 | "Skip" 텍스트 버튼 |
| 콘텐츠 영역 | 중앙 | Step별 애니메이션 콘텐츠 |
| Step Indicator | 하단 중앙 | 현재 Step 표시 (예: ● ○ ○) |

#### AC-001-03: Step 전환

- 각 Step은 **30초 ~ 1분** 후 자동 전환
- 또는 "다음" 버튼 클릭으로 수동 전환 (유저가 액션 가능)
- 전환 시 부드러운 fade/slide 애니메이션 적용

#### AC-001-04: 로딩 상태 연동

- 튜토리얼 진행 중 로딩 완료 여부 추적
- **로딩 완료 + 튜토리얼 완료**: 즉시 Opportunity 리스트로 전환
- **로딩 미완료 + 튜토리얼 완료/스킵**: 로딩 대기 화면으로 전환
  - 로딩 스피너 + 대기 메시지 표시
  - **"튜토리얼 다시 보기" 버튼** 함께 표시
  - 버튼 클릭 시 튜토리얼 Step 1부터 다시 시작

---

## US-002: Step 1 - 페이지 개요 및 가치 전달

### 사용자 스토리

사용자로서, 튜토리얼 첫 단계에서 다음 화면의 목적과 내가 얻을 가치를 이해하고, **어떻게 선택하면 되는지** 파악하고 싶습니다.

### Acceptance Criteria

#### AC-002-01: 헤더 메시지

- 상단에 헤더 텍스트 표시:
  - **"다음 단계에서 할 일을 알려드릴게요"**
- 폰트: Bold, 크기 24px 이상

#### AC-002-02: Mock 카드 + Rating 버튼 표시

- 대표 Opportunity 카드 1개 표시 (실제 데이터 기반)
- **핵심 요소만 선명하게, 나머지는 Mute 처리**:
  - **선명하게 표시**: Rating 버튼 영역 (Interested / Not Interested)
  - **Mute 처리 (opacity 낮춤)**: Title, Agency, Description 등 상세 내용
- Rating 버튼 영역을 시각적으로 강조 (테두리 또는 글로우 효과)

#### AC-002-03: 핵심 메시지 + Rating 액션 연동

- 메시지가 순차적으로 등장하며 **Rating 버튼 UI와 연동**:

| 순서 | 메시지 | UI 액션 |
|------|--------|---------|
| 1 | "일부라도 수행할 수 있는 프로젝트를 고르세요" | "Interested" 버튼 하이라이트 + 포인터 가리킴 |
| 2 | (자동으로 Interested 클릭되는 애니메이션) | 버튼이 선택 상태로 변경됨 |
| 3 | "우리가 함께 수주할 파트너를 찾아드릴게요" | 파트너 매칭 시각화 등장 |

- **"Interested" 버튼 클릭 애니메이션**: 실제로 유저가 어떻게 선택하는지 시연
- 메시지 강조: 핵심 키워드("일부라도", "파트너") 볼드 또는 하이라이트

#### AC-002-04: 가치 시각화 (파트너 매칭)

- Interested 선택 후 파트너 매칭 개념을 **다이어그램 또는 아이콘 플로우**로 표시:
  ```
  [👤 You] → [✓ Select Opportunity] → [🤝 Find Partners]
  ```
- 각 단계가 순차적으로 나타나는 애니메이션
- 아이콘 크기: 48px 이상, 화살표로 연결
- "Select Opportunity" 부분에서 방금 선택한 카드와 연결되는 느낌

#### AC-002-05: "일부라도" 강조

- **추가 보조 메시지** (작은 글씨):
  - "전체를 수행할 필요 없어요. 일부라도 가능하면 선택하세요."
- Interested 버튼 근처에 툴팁 또는 callout 형태로 표시

---

## US-003: Step 2 - 기본 Opportunity 카드 구조

### 사용자 스토리

사용자로서, Opportunity 카드의 기본 구조를 미리 파악하여, 실제 화면에서 어떤 정보를 어디서 찾아야 하는지 알고 싶습니다.

### Acceptance Criteria

#### AC-003-01: 헤더 메시지 업데이트

- 헤더 텍스트: **"Opportunity 카드를 살펴볼게요"**

#### AC-003-02: Mock Opportunity 카드

- **실제 데이터 기반** Mock 카드 1개 표시
- **매칭 태그 및 하이라이트 없는** 기본 버전
- 이번에는 **전체 카드 선명하게** 표시 (Mute 해제)
- 표시 필드:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| title | String | 공고 제목 | "Cloud Infrastructure Modernization Support" |
| agency | String | 발주 기관명 | "Department of Defense" |
| projectOverview | String | Project Background & Objective | "The agency seeks to modernize legacy..." |
| scopeOfWork | String | Scope of Work | "The contractor shall provide..." |
| ratingButtons | Component | Interested / Not Interested 버튼 | (버튼 UI) |

#### AC-003-03: 순차적 요소 하이라이트

- 카드의 각 요소를 **순차적으로 강조**하며 설명:

| 순서 | 요소 | 강조 방식 | 설명 텍스트 |
|------|------|-----------|-------------|
| 1 | Title | 테두리 + 포인터 | "공고 제목이에요" |
| 2 | Agency | 테두리 + 포인터 | "발주 기관이에요" |
| 3 | Project Overview | 테두리 + 포인터 | "발주 배경과 목표예요. Agency가 왜 이 프로젝트를 필요로 하는지, 무엇을 달성하고 싶은지 이해할 수 있어요" |
| 4 | Scope of Work | 테두리 + 포인터 | "실제 수행 업무예요. 여기서 당신이 수행 가능한 부분을 찾아보세요" |

- 각 강조 사이 **2-3초 간격**
- 포인터: 화살표 또는 손가락 아이콘 애니메이션

#### AC-003-04: Project Overview vs Scope of Work 구분 강조

- Description 영역 설명 시 **두 섹션의 역할 차이** 명확히 전달:
  - **Project Overview**: "왜(Why) 이 프로젝트가 필요한지"
  - **Scope of Work**: "무엇(What)을 해야 하는지"
- 보조 메시지:
  - **"Scope of Work에서 당신이 수행 가능한 부분을 찾아보세요"**
- 메시지는 Scope of Work 하단에 별도 표시

---

## US-004: Step 3 - AI Curation 기능 소개 (v2 신규)

### 사용자 스토리

사용자로서, AI가 제공하는 Curation 기능(Badge, 태그, 하이라이트, Rationale)을 이해하여, 나와 관련 있는 Opportunity를 빠르게 식별하고 필터링할 수 있게 되고 싶습니다.

### Acceptance Criteria

#### AC-004-01: 헤더 메시지 업데이트

- 헤더 텍스트: **"당신의 비즈니스와 연결된 부분을 찾는 법"**

#### AC-004-02: 기본 UI Mute 처리

- Step 2에서 보여준 **동일한 Mock 카드** 사용
- 기본 요소(Title, Agency, Description 텍스트) **Mute 처리**:
  - 색상: 회색화 (opacity 0.3-0.5)
  - 또는 배경 어둡게 처리
- **Rating 버튼은 Mute하지 않음** (일관성 유지)

#### AC-004-03: CurationBadge 등장

- 카드 우측 상단에 **"✓ Match" 뱃지** 애니메이션 등장:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| curationBadge | Object | Match 뱃지 정보 | `{ type: "match", label: "✓ Match" }` |

- 스타일: 녹색 배경, 체크 아이콘
- 등장 애니메이션: Fade in + Scale up
- 설명 텍스트: **"이 뱃지가 보이면 AI가 당신의 비즈니스와 맞다고 판단한 거예요"**

#### AC-004-04: Portfolio 태그 등장

- 카드 상단에 **Business Portfolio 매칭 태그** 표시:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| matchingTags | Array<String> | Business Portfolio 매칭 아이템 | ["Cloud Computing", "Infrastructure"] |

- 스타일: 기존 Relevance Indicator 태그와 동일
- 등장 애니메이션: Fade in + Slide down
- 설명 텍스트: **"이 태그는 당신의 Business Portfolio와 매칭된 영역이에요"**

#### AC-004-05: Description 하이라이트 등장

- Description 내 특정 문장에 **노란색 하이라이트** 애니메이션 등장:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| highlightedRanges | Array<{start, end}> | 하이라이트 범위 | `[{start: 0, end: 45}]` |

- 하이라이트 범위: 1-2개 문장 (데모용)
- 설명 텍스트: **"하이라이트된 부분이 당신의 사업과 연결돼요"**

#### AC-004-06: RationaleCallout 등장

- 카드 상단(Title 아래)에 **연두색 배경 Callout** 등장:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| rationale | Object | AI 판단 이유 | `{ reasons: ["Cloud infrastructure와 연관", "IT 컨설팅 역량 활용 가능"] }` |

- 스타일: 연두색 배경, 불릿 포인트 리스트
- 등장 애니메이션: Expand + Fade in
- 설명 텍스트: **"AI가 왜 맞다고 판단했는지 이유도 알려드려요"**

#### AC-004-07: "Curated for You" 체크박스 (인터랙티브)

- 화면 상단에 **체크박스 UI Mock** 표시:

| 필드 | 타입 | 설명 | 기본값 |
|------|------|------|--------|
| curatedForYouChecked | boolean | 체크박스 선택 상태 | false |

- **초기 상태**: 미선택 (unchecked)
- 설명 텍스트: **"여기를 클릭하면 AI가 찾은 Opportunity만 볼 수 있어요"**
- **유저 인터랙션 유도**:
  - 체크박스 영역 하이라이트 + 포인터 애니메이션
  - "클릭해보세요" 시각적 힌트

**유저가 체크박스 클릭 시**:
1. 체크 애니메이션 재생
2. Mock 카드 필터링 시뮬레이션 (일부 카드가 사라지는 효과)
3. **선택 상태 localStorage에 저장**:
   - Key: `proact:onboarding:curated-for-you`
   - Value: `true`
4. 실제 Opportunity 페이지 진입 시 "Curated for You" 체크된 상태로 초기화

**유저가 클릭하지 않고 넘어갈 경우**:
- 기본 상태(미선택)로 실제 페이지 진입
- localStorage에 값 저장하지 않음

#### AC-004-08: 행동 가이드

- 모든 Curation 요소 소개 후 **행동 지침** 표시:

```
✓ "Match" 뱃지가 있는 공고를 우선 확인해보세요
✓ 태그와 하이라이트로 어떤 부분이 연결되는지 빠르게 파악하세요
✓ Rationale(이유)를 읽으면 더 정확하게 판단할 수 있어요
✓ 모두 보고 싶으면 "Curated for You" 체크박스를 해제하세요
```

- 체크마크 아이콘과 함께 표시
- 순차적 fade in 애니메이션

#### AC-004-09: 최종 CTA

- Step 3 완료 시 **"시작하기" 버튼** 표시:
  - 텍스트: "시작하기"
  - 스타일: Primary button (배경색, 크기 강조)
- 버튼 클릭 시:
  - **로딩 완료 상태**: 즉시 Opportunity 리스트로 전환
    - "Curated for You" 체크 여부에 따라 필터 상태 적용
  - **로딩 미완료**: 로딩 대기 화면으로 전환
    - "튜토리얼 다시 보기" 버튼 포함

---

## US-005: Skip 기능

### 사용자 스토리

사용자로서, 튜토리얼이 필요 없다고 느낄 때 언제든 건너뛰어, 바로 Opportunity를 확인하고 싶습니다.

### Acceptance Criteria

#### AC-005-01: Skip 버튼 표시

- **모든 Step**에서 우측 상단에 Skip 버튼 표시
- 버튼 스타일:
  - 텍스트: "Skip" 또는 "건너뛰기"
  - 색상: Secondary (회색 또는 투명)
  - 위치: 우측 상단 고정

#### AC-005-02: Skip 동작

- Skip 버튼 클릭 시:
  - 튜토리얼 즉시 종료
  - **"Curated for You" 상태**: 미선택 상태로 처리 (localStorage에 저장하지 않음)
  - **로딩 완료 상태**: Opportunity 리스트로 즉시 전환
  - **로딩 미완료**: 로딩 대기 화면으로 전환
    - 로딩 스피너 + "Opportunity를 준비하고 있어요..." 메시지
    - **"튜토리얼 다시 보기" 버튼** 표시
    - 버튼 클릭 시 튜토리얼 Step 1부터 다시 시작

#### AC-005-03: Skip 추적 (Analytics)

- Skip 이벤트 발생 시 다음 데이터 기록:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| event | String | 이벤트 타입 | "tutorial_skipped" |
| step | Number | Skip 시점의 Step 번호 | 1, 2, 3 |
| elapsedTime | Number | 튜토리얼 시작 후 경과 시간 (초) | 15 |

---

## US-006: 로딩 상태 연동

### 사용자 스토리

사용자로서, 튜토리얼이 끝났을 때 Opportunity가 준비되어 있으면 바로 확인하고, 아직 로딩 중이면 자연스럽게 대기하면서 필요시 튜토리얼을 다시 볼 수 있고 싶습니다.

### Acceptance Criteria

#### AC-006-01: 로딩 상태 추적

- 튜토리얼 진행 중 백그라운드 로딩 상태 추적
- 상태값:

| 상태 | 설명 |
|------|------|
| loading | Opportunity API 호출 중 |
| success | 로딩 완료, 데이터 준비됨 |
| error | 로딩 실패 |

#### AC-006-02: 정상 완료 케이스

- **로딩 success + 튜토리얼 완료**:
  - "시작하기" 버튼 클릭 또는 Step 3 자동 완료 시
  - 즉시 Opportunity 리스트 화면으로 전환
  - **"Curated for You" 상태 적용**: 튜토리얼에서 체크했으면 필터 활성화
  - 전환 애니메이션: Fade 또는 Slide

#### AC-006-03: 로딩 대기 케이스

- **로딩 loading + 튜토리얼 완료/스킵**:
  - 로딩 대기 화면 표시:
    - 로딩 스피너
    - 메시지: "거의 다 됐어요..." 또는 "Opportunity를 준비하고 있어요..."
    - **"튜토리얼 다시 보기" 버튼** (Secondary 스타일)
  - "튜토리얼 다시 보기" 클릭 시:
    - 튜토리얼 Step 1부터 다시 시작
    - **"Curated for You" 선택 상태 유지** (이전에 선택했다면)
    - 로딩은 백그라운드에서 계속 진행
  - 로딩 완료 시 자동 전환

#### AC-006-04: 로딩 에러 케이스

- **로딩 error**:
  - 튜토리얼 종료 후 에러 화면 표시
  - 메시지: "Opportunity를 불러오지 못했어요"
  - "다시 시도" 버튼 제공
  - 다시 시도 시: 로딩 재시작 + 튜토리얼 없이 기존 로딩 UI

---

## 데이터 구조

### Tutorial State

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| isVisible | boolean | 튜토리얼 표시 여부 | true |
| currentStep | number | 현재 Step (1, 2, 3) | 1 |
| isCompleted | boolean | 튜토리얼 완료 여부 | false |
| isSkipped | boolean | Skip 여부 | false |
| startTime | number | 시작 시간 (timestamp) | 1706500000000 |
| curatedForYouChecked | boolean | "Curated for You" 체크 여부 | false |

### Mock Opportunity Data

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| title | String | 공고 제목 | "Cloud Infrastructure Modernization" |
| agency | String | 발주 기관 | "Department of Defense" |
| projectOverview | String | 발주 배경 및 목표 | "The agency seeks to modernize legacy systems..." |
| scopeOfWork | String | 수행 업무 범위 | "The contractor shall provide..." |
| matchingTags | Array<String> | Portfolio 매칭 태그 | ["Cloud Computing", "Infrastructure"] |
| highlightedRanges | Array<{start, end}> | 하이라이트 범위 | [{start: 0, end: 45}] |
| curationBadge | Object | Match 뱃지 | { type: "match", label: "✓ Match" } |
| rationale | Object | AI 판단 이유 | { reasons: ["Cloud infrastructure와 연관"] } |

### localStorage Keys

| Key | 타입 | 설명 | 예시 |
|-----|------|------|------|
| `proact:onboarding:curated-for-you` | boolean | Curated for You 선택 상태 | true |

---

## UI/UX 사양

### 애니메이션 Timing

| 요소 | 애니메이션 | Duration | Easing |
|------|-----------|----------|--------|
| Step 전환 | Fade + Slide | 300ms | ease-out |
| 텍스트 등장 | Fade in | 500ms | ease-in |
| 포인터 이동 | Slide | 400ms | ease-in-out |
| 태그 등장 | Fade + Scale | 400ms | spring |
| 하이라이트 등장 | Background fade | 600ms | ease-in |
| CurationBadge 등장 | Fade + Scale | 400ms | spring |
| RationaleCallout 등장 | Expand + Fade | 500ms | ease-out |
| 체크박스 체크 | Scale + Color | 200ms | ease-out |
| Interested 버튼 클릭 | Scale + Color change | 300ms | ease-out |

### Curation UI 요소 등장 순서 (Step 3)

1. 기본 UI Mute 처리 (0ms)
2. CurationBadge "✓ Match" 등장 (500ms)
3. Portfolio 태그 등장 (1500ms)
4. Description 하이라이트 등장 (2500ms)
5. RationaleCallout 등장 (3500ms)
6. "Curated for You" 체크박스 하이라이트 (4500ms)
7. 행동 가이드 표시 (6000ms)
8. 시작하기 버튼 표시 (7000ms)

### 반응형 디자인

- **Desktop**: 카드 Mock이 실제 크기에 가깝게 표시
- **Mobile**: 카드 Mock이 화면 너비에 맞게 축소, 텍스트 크기 조정

### 접근성

- Skip 버튼: 키보드 Tab으로 접근 가능
- 체크박스: 키보드 Space로 토글 가능
- 애니메이션: `prefers-reduced-motion` 미디어 쿼리 지원
- 색상 대비: WCAG AA 기준 충족

---

## 에러 처리

### 로딩 실패

- **조건**: Opportunity API 호출 실패 (네트워크 에러, 서버 에러)
- **처리**: 튜토리얼 종료 후 에러 화면 표시
- **메시지**: "Opportunity를 불러오지 못했어요. 다시 시도해주세요."

### Mock 데이터 미준비

- **조건**: 실제 데이터 기반 Mock이 없는 경우
- **처리**: 사전 선정된 Fallback 데이터 사용
- **Fallback 포함 항목**: CurationBadge, Portfolio 태그, RationaleCallout 예시 데이터

### localStorage 접근 실패

- **조건**: localStorage 접근 불가 (private 브라우징 등)
- **처리**: "Curated for You" 상태를 메모리에만 유지, 페이지 전환 시 기본값 사용

---

## Analytics 이벤트

### 튜토리얼 관련 이벤트

| 이벤트명 | 트리거 | 데이터 |
|----------|--------|--------|
| tutorial_started | 튜토리얼 시작 시 | `{ timestamp }` |
| tutorial_step_viewed | Step 전환 시 | `{ step, elapsedTime }` |
| tutorial_completed | 튜토리얼 완료 시 | `{ totalTime, curatedForYouChecked }` |
| tutorial_skipped | Skip 클릭 시 | `{ step, elapsedTime }` |
| tutorial_replayed | 다시 보기 클릭 시 | `{ previousCompletionStatus }` |
| curated_checkbox_clicked | 체크박스 클릭 시 | `{ checked, step }` |

---

## 향후 개선 사항

1. **A/B 테스트**: 튜토리얼 유무에 따른 전환율 비교
2. **개인화된 튜토리얼**: 유저의 업종/경험에 따라 강조점 차별화
3. **다시보기**: 설정에서 튜토리얼 재시청 옵션
4. **Curation 확장**: 메인 Discover 페이지에서도 Curation 기능 확대 적용 검토
5. **추가 인터랙티브 요소**: Rating 버튼 직접 클릭 시연 등

---

## 변경 이력

| 날짜 | 버전 | 변경 내용 |
|------|------|----------|
| 2026-01-30 | v2.1 | AI Curation 기능 반영 (CurationBadge, RationaleCallout, Portfolio 태그, Curated for You 체크박스) |
| 2026-01-29 | v1 | 초안 작성 |
