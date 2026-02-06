# Opportunity Relevance Indicator PRD 문서

**생성 일시**: 2026년 1월 26일
**최종 편집 일시**: 2026년 1월 26일
**상태**: 초안

---

## 1. Product 목표 & Success 정의

### 1.1. 제품 컨텍스트 요약

- Proact의 핵심 가치:
    > "정부 입찰 공고를 유저의 비즈니스와 연관도 높은 순으로 추천하여, 영업 기회(Sequence) 발굴을 돕는다"
- 지금까지:
    - (1) 온보딩을 통해 유저의 Company Description 자동 생성 (Summary + Business Portfolio)
    - (2) Generate Profile 시 Company Description 기반으로 매칭된 Opportunity 리스트 제공
- 새로 추가하는 Opportunity Relevance Indicator:
    - (3) 각 Opportunity가 유저의 어떤 Business Portfolio 아이템과 매칭되는지 시각적으로 표시

### 1.2. 왜 Opportunity Relevance Indicator가 중요한가

- **현재 문제**: [Opportunity 리스트 확인] → [Relevant Opportunity 선택] 전환율이 **50%**로 기대 이하
    - 유저가 공고 하나당 3-5분을 투자해야 적합 여부를 판단할 수 있음
    - Title에 구체적인 정보가 없어 Description 전체를 읽어야 함
    - 10개 이상 확인해야 적합한 공고를 발견 → 높은 cognitive load
- **가설**: 실제로는 적합한 공고가 리스트에 있지만, 유저가 Description을 심도있게 읽기 어려워 판단하지 못하는 케이스가 존재
- **해결 방향**: 유저가 빠르게 "이 공고가 나와 관련있다"를 인지하고, "어떤 부분이 연결되는지" 맥락을 파악할 수 있도록 지원

> 따라서 Opportunity Relevance Indicator의 최우선 목표:
> - *"[Opportunity 리스트 확인] → [Relevant Opportunity 선택] 전환율을 50%에서 80%로 개선"*

---

## 2. JTBD 정의

### JTBD #1 - "적합한 공고 빠르게 스캔하기" (리스트 탐색)

> **When**
> 나는 Generate Profile 후 Opportunity 리스트를 처음 마주했을 때

> **I want to**
> 어떤 공고가 내 비즈니스와 관련있는지 빠르게 파악하고 싶다

> **So that**
> 모든 공고를 일일이 읽지 않고도, 집중해서 검토할 공고를 효율적으로 선별할 수 있다

---

### JTBD #2 - "매칭 이유 이해하기" (상세 검토)

> **When**
> 태그를 보고 관심있는 공고를 발견했을 때

> **I want to**
> Description의 어떤 부분이 내 비즈니스와 연결되는지 구체적으로 확인하고 싶다

> **So that**
> 이 공고가 정말 나에게 적합한지 확신을 갖고 Interested 여부를 결정할 수 있다

---

### JTBD #3 - "관련없는 공고 빠르게 스킵하기" (효율적 탐색)

> **When**
> 리스트에 많은 공고가 있고, 시간이 제한적일 때

> **I want to**
> 내 비즈니스와 관련없는 공고를 빠르게 걸러내고 싶다

> **So that**
> 정말 검토가 필요한 공고에만 시간을 투자할 수 있다

---

## 3. 유저 가치 & 비즈니스 가치 정리

### 유저 가치

1. **판단 시간 단축**
    - 공고당 3-5분 → 태그로 5-10초 내 1차 필터링 가능
    - 하이라이트로 Description 내 핵심 부분만 집중 검토
2. **판단 정확도 향상**
    - 내 Business Portfolio와 매칭되는 부분을 놓치지 않음
    - Semantic 매칭으로 다른 용어로 표현된 관련 내용도 발견
3. **인지 부하 감소**
    - "왜 이 공고가 추천됐는지" 명확히 이해
    - 불확실성 감소로 의사결정 스트레스 완화

### 비즈니스 가치

1. **온보딩 전환율 개선**
    - [Opportunity 리스트 확인] → [Relevant Opportunity 선택] 전환율: 50% → 80%
2. **Sequence 생성 증가**
    - 적합한 공고 발견율 향상 → Sequence 생성으로 이어지는 유저 증가
3. **온보딩 이탈률 감소**
    - 온보딩은 1회성 프로세스로, 이탈 시 회복 어려움
    - 첫 경험에서 가치를 즉시 전달하여 이탈 방지

---

## 4. 솔루션 개요

### 4.1. 핵심 컴포넌트

| 컴포넌트 | 설명 | 위치 |
|----------|------|------|
| **매칭 태그** | 유저의 Business Portfolio 아이템명을 태그로 표시 | Opportunity 카드 상단 |
| **본문 하이라이트** | Description 내 매칭되는 문장에 형광색(노란색) 표시 | Opportunity 카드 Description 영역 |

### 4.2. 매칭 로직

- **매칭 기준**: 유저의 Company Description (Summary + Business Portfolio) 기반
- **매칭 방식**: Semantic 매칭 (단순 키워드 매칭이 아닌 의미 기반)
    - 예: "Cloud Computing" ↔ "data center modernization" 매칭 가능
- **매칭 대상**: Opportunity의 Description 전체 (Project Background, Objective, Scope of Work)

### 4.3. 디스플레이 규칙

| 항목 | 규칙 |
|------|------|
| 태그 개수 | 제한 없음 (Portfolio 아이템 수가 많지 않음) |
| 하이라이트 범위 | Description 전체 |
| 하이라이트 상한선 | Description 전체의 **20%** 초과 시 가장 관련도 높은 부분만 표시 |
| 매칭 없는 공고 | 태그 없이 그대로 표시 (리스트에서 제외하지 않음) |

---

## 5. 유저 플로우

### Flow A. Opportunity 리스트 탐색

- Entry Point: **Generate Profile 완료 후 Opportunity 리스트 화면**
- 유저가 프로필 생성을 완료하고 추천된 공고 리스트를 확인하는 시점
- 플로우:
    - Step 1: 유저가 Opportunity 카드를 보면, 상단에 **매칭 태그** 표시됨 (예: `Cloud Computing`, `AI`)
    - Step 2: 태그를 보고 관심있는 공고 발견 시, Description 영역에서 **하이라이트된 문장** 확인
    - Step 3: 하이라이트 부분을 중심으로 빠르게 검토 후 Interested 여부 결정
- 완료 후: 유저가 Interested 공고를 선택하여 다음 단계로 진행

---

## 6. 상세 설계

### 6.1. 매칭 태그 — 빠른 스캔 지원

**상황**

- 유저가 Opportunity 리스트를 스크롤하며 훑어볼 때
- 유저의 심리/기대: "어떤 공고가 나랑 관련있지? 빨리 찾고 싶다"

**디스플레이**

- Opportunity 카드 상단에 태그 형태로 표시
- 태그 텍스트: Business Portfolio의 아이템명 (예: `Cloud Computing`, `Artificial Intelligence`)
- 태그 스타일: 배경색이 있는 pill 형태, 눈에 띄되 과하지 않게

**예시**
```
┌─────────────────────────────────────────────┐
│ [Cloud Computing] [AI]                      │  ← 매칭 태그
│                                             │
│ Federal Cloud Migration Services            │  ← Title
│                                             │
│ The agency seeks to modernize its legacy    │  ← Description (하이라이트 포함)
│ infrastructure through ███████████████████  │
│ while ensuring compliance with FedRAMP...   │
└─────────────────────────────────────────────┘
```

**디자인 의도**

- 5-10초 내 1차 필터링 가능하도록 시각적 단서 제공
- Desktop 3개 / Mobile 1개 레이아웃에서도 즉시 인지 가능

---

### 6.2. 본문 하이라이트 — 맥락 이해 지원

**상황**

- 유저가 태그를 보고 관심있는 공고를 발견했을 때
- 유저의 심리/기대: "어떤 부분이 나랑 연결되는 거지? 확인해보자"

**디스플레이**

- Description 텍스트 내 매칭되는 문장에 형광색(노란색) 배경 적용
- 문장 단위로 하이라이트 (단어 단위 아님)
- 하이라이트 상한: 전체 Description의 20%

**예시**
```
The agency seeks to modernize its legacy infrastructure through
[cloud-based solutions and data center consolidation] ← 하이라이트
while ensuring compliance with FedRAMP requirements. The contractor
shall provide [machine learning capabilities for predictive analytics] ← 하이라이트
to support decision-making processes.
```

**디자인 의도**

- Semantic 매칭의 결과를 시각적으로 표현
- 유저가 전체 Description을 읽지 않아도 핵심 연결점 파악 가능
- 20% 상한으로 하이라이트 과다 방지 → 가독성 유지

---

## 7. 매칭 품질 기준 (초안)

### 7.1. Semantic 매칭 정확도

| 수준 | 정의 | 예시 |
|------|------|------|
| **High** | 동일 개념, 다른 표현 | "Cloud Computing" ↔ "cloud-based solutions" |
| **Medium** | 관련 개념, 명확한 연결 | "Cloud Computing" ↔ "data center modernization" |
| **Low** | 간접 연결, 맥락 의존 | "Cloud Computing" ↔ "IT infrastructure" |

**MVP 기준**: High + Medium 수준만 매칭으로 표시 (Low는 제외)

### 7.2. 품질 검증 방법

- **정성적 검증**: 내부 QA로 10-20개 샘플 검토, 매칭 적합성 확인
- **정량적 검증**:
    - False Positive Rate: 하이라이트된 부분이 실제로 관련없는 비율 < 10%
    - Coverage: 실제 관련있는 내용 중 하이라이트된 비율 > 70%

### 7.3. Fallback 처리

- 매칭 신뢰도가 낮은 경우 → 태그/하이라이트 표시하지 않음 (over-matching보다 under-matching이 나음)
- 매칭이 전혀 없는 공고 → 태그 없이 기존 방식대로 표시

---

## 8. 성공 지표

### Primary Metric
- **[Opportunity 리스트 확인] → [Relevant Opportunity 선택] 전환율**: 50% → **80%**

### Secondary Metrics
- 유저당 선택하는 Opportunity 개수
- 리스트 평균 체류 시간 (감소 기대)
- 태그가 있는 공고 vs 없는 공고의 선택 비율 비교

---

## 9. MVP 범위

| 항목 | MVP 포함 | 향후 고려 |
|------|----------|-----------|
| 매칭 태그 표시 | ✅ | - |
| 본문 하이라이트 | ✅ | - |
| Semantic 매칭 (High + Medium) | ✅ | Low 수준 매칭 추가 |
| 하이라이트 20% 상한 | ✅ | 유저 피드백 기반 조정 |
| 태그 클릭 시 해당 하이라이트로 스크롤 | ❌ | UX 개선으로 추후 검토 |
| 매칭 품질 피드백 수집 (👍/👎) | ❌ | 품질 개선용 데이터 수집 |

---

## 10. 리스크 & 대응

| 리스크 | 영향 | 대응 방안 |
|--------|------|-----------|
| 하이라이트 과다로 가독성 저하 | 중 | 20% 상한 적용, 관련도 높은 순 우선 |
| 매칭 품질 낮아 유저 신뢰 하락 | 상 | High+Medium만 표시, 샘플 QA 필수 |
| 매칭 없는 공고가 많아 기능 무용화 | 중 | 매칭률 모니터링, 매칭 기준 조정 |
| 태그가 너무 많아 시각적 과부하 | 하 | Portfolio 아이템 수가 제한적이라 낮은 리스크 |

---

## 11. Open Questions

- [ ] Semantic 매칭 구현 방식: 실시간 생성 vs 사전 계산 저장?
- [ ] 하이라이트 색상: 노란색 외 다른 옵션 검토 필요?
- [ ] 태그 디자인: 기존 UI 컴포넌트와의 일관성 확인 필요
- [ ] 매칭 품질 평가를 위한 테스트 데이터셋 구성

---

## 12. 참고자료

- Proact Knowledge Base: `assets/Proact/proact-knowledge-base.md`
- Weekly Picks 검색 기능 PRD: `assets/Proact/prds/2026-01-02-weekly-picks-search.md`
