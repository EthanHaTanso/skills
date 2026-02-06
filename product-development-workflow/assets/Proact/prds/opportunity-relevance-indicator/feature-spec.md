# Opportunity Relevance Indicator 기능 정의서 (Feature Specification)

## 문서 개요

이 문서는 Proact의 **Opportunity Relevance Indicator** 기능을 정의합니다.

**Related Documents**:
- PRD 문서: `prds/opportunity-relevance-indicator.md`
- 정책서 (상세): `prds/opportunity-relevance-indicator-detailed-policy.md`

---

## US-001: Opportunity 리스트 - 매칭 태그 표시

### 사용자 스토리

사용자로서, Opportunity 리스트를 확인할 때 **각 공고가 내 Business Portfolio의 어떤 항목과 관련있는지** 한눈에 파악하여, 관심있는 공고를 빠르게 선별하고 싶습니다.

### Acceptance Criteria

#### AC-001-01: 태그 표시 위치

- 매칭 태그는 **Opportunity 카드의 상단**에 표시됩니다
- 태그는 Title보다 위에 위치하여 스크롤 시 가장 먼저 눈에 들어옵니다
- 카드 레이아웃:

```
┌─────────────────────────────────────────────┐
│ [Tag 1] [Tag 2] [Tag 3]                     │  ← 매칭 태그 영역
│                                             │
│ Opportunity Title                           │  ← Title
│                                             │
│ Description text with highlights...         │  ← Description
└─────────────────────────────────────────────┘
```

#### AC-001-02: 태그 콘텐츠

- 태그 텍스트는 **유저의 Business Portfolio 아이템명**입니다
- 표시되는 정보:

| 필드 | 타입 | 필수 여부 | 설명 | 예시 |
|------|------|-----------|------|------|
| tagText | String | 필수 | Portfolio 아이템명 | "Cloud Computing" |
| portfolioItemId | String | 필수 | 매칭된 Portfolio 아이템 ID | "portfolio_001" |

- 태그는 유저의 Company Description에서 추출한 Business Portfolio 아이템명 중 **해당 Opportunity와 Semantic 매칭된 것만** 표시합니다

#### AC-001-03: 태그 개수

- 태그 개수 **제한 없음** (Portfolio 아이템 수가 제한적이므로)
- 복수의 Portfolio 아이템이 매칭되면 모두 표시
- 표시 순서: 매칭 신뢰도가 높은 순

#### AC-001-04: 태그 스타일

- 태그 형태: **Pill 형태의 뱃지** (둥근 모서리)
- 배경색: 연한 색상 (예: `bg-blue-100` 또는 `bg-gray-100`)
- 텍스트 색상: 진한 색상 (예: `text-blue-700` 또는 `text-gray-700`)
- 폰트 크기: 본문보다 작게 (예: `text-xs` 또는 `text-sm`)
- 태그 간 간격: `4px` (gap-1)
- 호버 효과: 없음 (MVP)

#### AC-001-05: 태그 영역 오버플로우 처리

- 태그가 카드 너비를 초과할 경우:
  - **줄바꿈 허용** (flex-wrap)
  - 최대 2줄까지 표시
  - 2줄 초과 시 마지막에 `+N` 형태로 축약 표시
- 예시:
  ```
  [Cloud Computing] [AI] [Cybersecurity]
  [Data Analytics] +2
  ```

#### AC-001-06: 매칭 없음 처리

- Opportunity가 유저의 Business Portfolio와 매칭되지 않는 경우:
  - 태그 영역이 **비어있음** (빈 공간으로 표시하지 않고 영역 자체를 숨김)
  - 카드 레이아웃이 태그 없이 Title부터 시작
- 매칭이 없어도 Opportunity는 리스트에서 **제외되지 않음**

---

## US-002: Opportunity 리스트 - 본문 하이라이트 표시

### 사용자 스토리

사용자로서, Opportunity Description 내에서 **내 Business Portfolio와 관련있는 부분이 시각적으로 강조**되어, 전체 텍스트를 읽지 않고도 핵심 연결점을 빠르게 파악하고 싶습니다.

### Acceptance Criteria

#### AC-002-01: 하이라이트 위치

- 하이라이트는 **Opportunity 카드의 Description 영역** 내에 적용됩니다
- Description 전체 (Project Background, Objective, Scope of Work 모두 포함)가 하이라이트 대상입니다

#### AC-002-02: 하이라이트 단위

- 하이라이트 단위: **문장 (Sentence)**
- 단어 단위가 아닌 문장 단위로 하이라이트하여 맥락 파악 용이
- 문장 경계: 마침표(.), 느낌표(!), 물음표(?) 기준

#### AC-002-03: 하이라이트 스타일

- 배경색: **노란색** (`bg-yellow-200` 또는 `#FEF08A`)
- 텍스트 색상: 변경 없음 (기존 색상 유지)
- 추가 스타일: 없음 (밑줄, 볼드 등 적용하지 않음)
- 예시:
  ```
  The agency seeks to modernize its legacy infrastructure.
  [The contractor shall provide cloud-based solutions and
  data center consolidation services.] ← 하이라이트
  Compliance with FedRAMP is required.
  ```

#### AC-002-04: 하이라이트 상한

- 하이라이트 총량: Description 전체의 **20% 이하**
- 20% 초과 시:
  - 매칭 신뢰도가 높은 문장부터 우선 하이라이트
  - 나머지 문장은 하이라이트하지 않음
- 계산 방법: `하이라이트된 문자 수 / 전체 Description 문자 수 <= 0.2`

#### AC-002-05: 복수 하이라이트 처리

- 하나의 Opportunity에서 여러 문장이 매칭될 수 있음
- 각 매칭 문장에 개별적으로 하이라이트 적용
- 연속된 문장이 모두 매칭되면 하나의 블록으로 하이라이트

#### AC-002-06: 매칭 없음 처리

- Description과 매칭되는 내용이 없는 경우:
  - 하이라이트 없이 **기존 Description 그대로 표시**
  - 별도 안내 메시지 없음

---

## US-003: Semantic 매칭 로직

### 사용자 스토리

사용자로서, 내 Business Portfolio와 **동일한 키워드가 아니더라도 의미상 관련있는 내용**이 매칭되어, 키워드 차이로 놓칠 수 있는 관련 공고를 발견하고 싶습니다.

### Acceptance Criteria

#### AC-003-01: 매칭 입력 데이터

- **Source (유저 측)**: Company Description
  - Summary 텍스트
  - Business Portfolio 각 아이템의 아이템명 + 아이템 설명

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| summary | String | 회사 요약 | "Google is a global technology company..." |
| portfolioItems | Array | Business Portfolio 아이템 리스트 | - |
| portfolioItems[].name | String | 아이템명 | "Cloud Computing" |
| portfolioItems[].description | String | 아이템 설명 | "Offers scalable infrastructure through Google Cloud" |

- **Target (공고 측)**: Opportunity Description
  - Project Background & Objective
  - Scope of Work

#### AC-003-02: 매칭 신뢰도 수준

- 매칭 결과는 **신뢰도 수준**과 함께 반환됩니다:

| 수준 | 정의 | 표시 여부 | 예시 |
|------|------|-----------|------|
| **High** | 동일 개념, 다른 표현 | ✅ 표시 | "Cloud Computing" ↔ "cloud-based solutions" |
| **Medium** | 관련 개념, 명확한 연결 | ✅ 표시 | "Cloud Computing" ↔ "data center modernization" |
| **Low** | 간접 연결, 맥락 의존 | ❌ 미표시 | "Cloud Computing" ↔ "IT infrastructure" |

- MVP에서는 **High + Medium만 표시**, Low는 제외

#### AC-003-03: 매칭 출력 데이터

- 매칭 결과는 다음 형태로 반환됩니다:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| opportunityId | String | Opportunity ID | "opp_12345" |
| matches | Array | 매칭 결과 리스트 | - |
| matches[].portfolioItemName | String | 매칭된 Portfolio 아이템명 | "Cloud Computing" |
| matches[].confidenceLevel | Enum | 신뢰도 수준 | "high" \| "medium" |
| matches[].highlightedSentences | Array | 하이라이트할 문장들 | - |
| matches[].highlightedSentences[].text | String | 문장 텍스트 | "The contractor shall provide cloud-based..." |
| matches[].highlightedSentences[].startIndex | Number | 시작 위치 | 145 |
| matches[].highlightedSentences[].endIndex | Number | 끝 위치 | 231 |

#### AC-003-04: 매칭 품질 기준

- **False Positive Rate**: 하이라이트된 부분이 실제로 관련없는 비율 **< 10%**
- **Coverage**: 실제 관련있는 내용 중 하이라이트된 비율 **> 70%**
- 품질 검증: 출시 전 10-20개 샘플 QA 필수

---

## US-004: 태그-하이라이트 연동

### 사용자 스토리

사용자로서, 태그와 하이라이트가 **서로 연결되어** 어떤 Portfolio 아이템이 Description의 어떤 부분과 매칭되는지 명확히 이해하고 싶습니다.

### Acceptance Criteria

#### AC-004-01: 태그-하이라이트 매핑

- 각 태그는 해당하는 하이라이트 문장과 논리적으로 연결됩니다
- 예시:
  - 태그 `Cloud Computing` → Description 내 "cloud-based solutions" 문장 하이라이트
  - 태그 `AI` → Description 내 "machine learning capabilities" 문장 하이라이트

#### AC-004-02: MVP 인터랙션

- MVP에서는 **시각적 연결만** 제공 (태그와 하이라이트 동시 표시)
- 태그 클릭 시 동작: **없음** (향후 개선 사항)
- 하이라이트 호버 시 동작: **없음** (향후 개선 사항)

#### AC-004-03: 향후 인터랙션 (Post-MVP)

- 태그 클릭 시 해당 하이라이트 위치로 스크롤
- 하이라이트 호버 시 관련 태그 강조

---

## 데이터 구조

### Company Description

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| companyId | String | 회사 ID | "company_001" |
| summary | String | 회사 요약 | "Google is a global technology company..." |
| portfolioItems | Array\<PortfolioItem\> | Business Portfolio | - |

### Portfolio Item

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| id | String | Portfolio 아이템 ID | "portfolio_001" |
| name | String | 아이템명 (태그에 표시) | "Cloud Computing" |
| description | String | 아이템 설명 | "Offers scalable infrastructure..." |

### Opportunity (확장)

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| id | String | Opportunity ID | "opp_12345" |
| title | String | 공고 제목 | "Federal Cloud Migration Services" |
| description | String | 공고 설명 (전체) | "Project Background: ... Scope of Work: ..." |
| matchingTags | Array\<MatchingTag\> | 매칭 태그 목록 | - |
| highlightedRanges | Array\<HighlightRange\> | 하이라이트 범위 목록 | - |

### Matching Tag

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| portfolioItemId | String | Portfolio 아이템 ID | "portfolio_001" |
| portfolioItemName | String | 태그에 표시될 텍스트 | "Cloud Computing" |
| confidenceLevel | Enum | 매칭 신뢰도 | "high" \| "medium" |

### Highlight Range

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| portfolioItemId | String | 관련 Portfolio 아이템 ID | "portfolio_001" |
| startIndex | Number | 하이라이트 시작 위치 | 145 |
| endIndex | Number | 하이라이트 끝 위치 | 231 |
| text | String | 하이라이트된 문장 텍스트 | "The contractor shall provide..." |

---

## UI/UX 사양

### 컴포넌트 구조

```
OpportunityCard
├── TagContainer
│   └── Tag (multiple)
├── Title
└── Description
    └── HighlightedText (multiple)
```

### 컴포넌트 재사용

- **Tag**: 기존 shadcn/ui의 Badge 컴포넌트 활용 또는 커스텀
- **HighlightedText**: Description 렌더링 시 하이라이트 적용하는 래퍼 컴포넌트

### 반응형 디자인

| 디바이스 | 카드 개수 | 태그 줄 수 | 비고 |
|----------|-----------|------------|------|
| Desktop | 3개/row | 최대 2줄 | - |
| Mobile | 1개/row | 최대 2줄 | 태그 크기 동일 |

### 접근성

- 태그: `role="status"` 또는 적절한 ARIA 라벨
- 하이라이트: 시각적 표시 외에 스크린 리더 대응 고려 (향후)
- 색상 대비: WCAG AA 기준 충족 (노란색 배경 + 검은 텍스트)

---

## API 명세

### 매칭 결과 조회

**Endpoint**: `GET /api/v1/opportunities/{opportunityId}/relevance`

**Headers**:
```
Authorization: Bearer {token}
```

**Response**:
```json
{
  "opportunityId": "opp_12345",
  "matches": [
    {
      "portfolioItemId": "portfolio_001",
      "portfolioItemName": "Cloud Computing",
      "confidenceLevel": "high",
      "highlightedSentences": [
        {
          "text": "The contractor shall provide cloud-based infrastructure modernization services.",
          "startIndex": 145,
          "endIndex": 231
        }
      ]
    },
    {
      "portfolioItemId": "portfolio_002",
      "portfolioItemName": "AI",
      "confidenceLevel": "medium",
      "highlightedSentences": [
        {
          "text": "Machine learning capabilities for predictive analytics are required.",
          "startIndex": 450,
          "endIndex": 520
        }
      ]
    }
  ],
  "totalHighlightPercentage": 15.2
}
```

### Opportunity 리스트 조회 (확장)

**Endpoint**: `GET /api/v1/opportunities`

**Response** (기존 + 매칭 정보 추가):
```json
{
  "opportunities": [
    {
      "id": "opp_12345",
      "title": "Federal Cloud Migration Services",
      "description": "...",
      "relevantScore": 85,
      "matchingTags": [
        {
          "portfolioItemId": "portfolio_001",
          "portfolioItemName": "Cloud Computing",
          "confidenceLevel": "high"
        }
      ],
      "highlightedRanges": [
        {
          "portfolioItemId": "portfolio_001",
          "startIndex": 145,
          "endIndex": 231,
          "text": "..."
        }
      ]
    }
  ]
}
```

---

## 에러 처리

### Company Description 미존재

- **조건**: 유저의 Company Description이 생성되지 않은 경우
- **처리**: 매칭 기능 비활성화, 기존 UI로 폴백
- **메시지**: 없음 (조용히 기능 미표시)

### 매칭 서비스 오류

- **조건**: Semantic 매칭 API 호출 실패
- **처리**: 태그/하이라이트 없이 기존 UI로 폴백
- **메시지**: 없음 (조용히 기능 미표시)
- **로깅**: 에러 로그 기록 (모니터링용)

### Description 파싱 오류

- **조건**: Description 텍스트 파싱 중 오류 (인덱스 범위 초과 등)
- **처리**: 해당 Opportunity만 하이라이트 미적용
- **메시지**: 없음

---

## 성능 요구사항

- **매칭 계산**: Opportunity 리스트 로딩 시 병렬 처리 또는 사전 계산
- **렌더링**: 하이라이트 적용으로 인한 렌더링 지연 최소화 (< 100ms 추가)
- **캐싱**: 동일 Company Description + Opportunity 조합의 매칭 결과 캐싱 권장

---

## 보안 요구사항

- Company Description은 해당 유저에게만 표시
- 매칭 결과는 인증된 유저의 요청에만 응답
- API 호출 시 조직(Organization) 권한 검증

---

## 향후 개선 사항

1. **태그 클릭 → 하이라이트 스크롤**: 태그 클릭 시 해당 하이라이트 위치로 자동 스크롤
2. **매칭 피드백 수집**: 유저가 "이 매칭이 맞다/틀리다" 피드백 제공 → 알고리즘 개선
3. **하이라이트 색상 커스터마이징**: 다크모드, 색맹 사용자 대응
4. **Weekly Picks 확장**: 온보딩 외 Weekly Picks 화면에도 동일 기능 적용
5. **Low 신뢰도 매칭 옵션**: 유저가 원하면 Low 신뢰도 매칭도 볼 수 있는 토글
