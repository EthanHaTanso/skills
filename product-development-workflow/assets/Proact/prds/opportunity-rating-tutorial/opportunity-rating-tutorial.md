# 정책서: Opportunity Rating Tutorial (온보딩)

**작성일:** 2026-01-29
**상태:** Draft (v2 - Curation 반영)
**작성자:** Product Team

---

## 1. 왜 만드는가? (Why)

### 1.1. 문제 정의
**현상:**
- 온보딩 중 [Opportunity Load → "Interested" Rating] 전환율이 **50%**로 기대 이하

**원인:**
- 유저가 Opportunity 선별의 맥락을 오해함
- **오해:** "내가 직접 수주할 수 있는 프로젝트"를 골라야 함 (fully 수행 가능)
- **실제 의도:** "일부라도 수행할 수 있는 프로젝트"를 고르면, 시스템이 함께 수주할 파트너를 찾아줌

**결과:**
- "나한테 맞는 게 없다"며 이탈
- 또는 잘못된 선택 기준으로 Opportunity 선별 → 부적합한 파트너 매칭

### 1.2. 비즈니스 임팩트
- 온보딩 전환율 저하 → 신규 유저 활성화 실패
- 잘못된 Opportunity 선택 → 파트너 매칭 품질 저하 → 핵심 가치 제안 훼손

### 1.3. 왜 지금인가?
- **LLM Curation 기능이 새로 추가됨** (PA-1256)
  - AI가 Opportunity별로 관련성 평가 후 Badge 표시
  - "Curated for You" 필터로 관련 있는 것만 볼 수 있음
  - RationaleCallout으로 "왜 매칭되는지" 이유 설명
- 새로운 UI 요소에 대한 설명 없이는 유저가 활용법을 모를 수 있음
- 로딩 시간(5-10초)이 자연스러운 교육 시점으로 활용 가능

---

## 2. 무엇을 만드는가? (What)

### 2.1. 핵심 기능
**Company Profile Confirm → Opportunity Load** 사이 로딩 화면에서 **순차 애니메이션 튜토리얼** 제공

### 2.2. 튜토리얼 구성 (v2 - Curation 반영)

| 단계 | 제목 | 내용 | 목적 |
|------|------|------|------|
| **Step 1** | 페이지 개요 | 유저 과업 + 결과(파트너 매칭) + Rating 방법 시연 | "왜 이걸 하는지" + "어떻게 선택하는지" 이해 |
| **Step 2** | Opportunity 카드 기본 | Title, Agency, Project Overview, Scope of Work | "무엇을 보는지" 이해 |
| **Step 3** | AI Curation 기능 | CurationBadge + RationaleCallout + "Curated for You" 필터 | "AI가 어떻게 도와주는지" 이해 |

### 2.3. 핵심 메시지
> **"일부라도 수행할 수 있는 프로젝트를 고르세요. 우리가 함께 수주할 파트너를 찾아드릴게요."**

> **"AI가 당신의 비즈니스와 맞는 Opportunity를 찾아 표시해드립니다."**

### 2.4. 인터랙션
- **진행 방식:** 순차 애니메이션 (자동 진행)
- **단계별 소요 시간:** 30초 ~ 1분
- **스킵 기능:** 제공 (유저가 원하면 튜토리얼 건너뛰기 가능)
- **다시보기:** 로딩 대기 중일 때 "튜토리얼 다시 보기" 버튼 제공
- **로딩과의 관계:** 튜토리얼이 로딩보다 길어도 OK (로딩 완료 후에도 튜토리얼 계속 진행)

### 2.5. Mock 데이터
- Generic하되, **실제 시스템 데이터** 활용
- 가짜 데이터 사용 금지

---

## 3. 어떻게 성공을 측정하는가? (How)

### 3.1. 핵심 지표
| 지표 | 현재 | 목표 |
|------|------|------|
| Opportunity Load → "Interested" Rating 전환율 | 50% | **80%** |

### 3.2. 보조 지표
- 튜토리얼 완료율 (스킵하지 않고 끝까지 본 비율)
- 튜토리얼 스킵률
- 튜토리얼 이후 평균 "Interested" 선택 개수
- "Curated for You" 필터 사용률

---

## 4. 범위 및 제약사항

### 4.1. In Scope
- 온보딩 플로우 내 튜토리얼 (Company Profile Confirm → Opportunity Load 사이)
- 3단계 순차 애니메이션 (각 30초~1분)
- 실제 데이터 기반 Mock UI
- 스킵 기능
- 로딩 대기 중 "튜토리얼 다시 보기" 버튼

### 4.2. Out of Scope
- 온보딩 외 다른 진입점에서의 튜토리얼
- 튜토리얼 A/B 테스트

---

## 5. 연관 문서
- LLM Curation Spec: `docs/specs/llm-filtered-opportunities-streaming.md`
- Proact Knowledge Base: [../proact-knowledge-base.md](../proact-knowledge-base.md)

---

## 변경 이력

| 날짜 | 변경 내용 | 작성자 |
|------|----------|--------|
| 2026-01-29 | v2: PA-1256 Curation 기능 반영하여 Step 3 재설계 | Product Team |
| 2026-01-29 | 초안 작성 | Product Team |
