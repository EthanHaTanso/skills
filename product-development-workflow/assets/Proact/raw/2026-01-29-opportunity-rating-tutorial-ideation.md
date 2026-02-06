# Ideation Log: Opportunity Rating Tutorial

**날짜:** 2026-01-29
**주제:** 온보딩 Opportunity Rating 단계 튜토리얼

---

## 문제 발견 과정

### 초기 맥락
- 온보딩에서 Company Profile 확인 후 Relevant Opportunity를 로드
- 유저가 "일부라도 수행 가능한" Opportunity를 선택해야 함
- 선택된 Opportunity 기반으로 potential partner (incumbent vendor) 식별

### 유저 피드백
- 유저가 Opportunity 선별의 맥락/의도를 이해하기 어려워함
- **오해:** "내가 직접 수주할 프로젝트"를 골라야 한다고 생각
- **결과:** 전환율 50%, "나한테 맞는 게 없다"며 이탈

---

## 핵심 인사이트

### 메시지 프레이밍
**공급자 관점 (Before):**
> "선택한 Opportunity 기반으로 potential partner를 식별하고, 이들의 B2G Sales Channel을 leverage하여..."

**유저 관점 (After):**
> "일부라도 수행할 수 있는 프로젝트를 고르세요. 우리가 함께 수주할 파트너를 찾아드릴게요."

### 튜토리얼 타이밍
- Company Profile Confirm → Opportunity Load 사이 5-10초 로딩 시간 활용
- 로딩 대기 시간을 교육 기회로 전환
- 튜토리얼이 로딩보다 길어도 OK (오히려 안전)

---

## 결정 사항

### 튜토리얼 구성
1. **Step 1:** 페이지 개요 + 유저 과업 + 결과(파트너 매칭)
2. **Step 2:** 기본 Opportunity 카드 (매칭 태그/하이라이트 없이)
3. **Step 3:** 매칭 태그 + 하이라이트 (기본 UI mute)

### 인터랙션
- 순차 애니메이션 진행
- 각 단계 30초 ~ 1분
- 스킵 기능 제공
- 다시보기 불필요 (새로고침 시 다시 표시)

### Mock 데이터
- Generic하되 실제 시스템 데이터 활용
- 가짜 데이터 금지

### 성공 지표
- 전환율 50% → 80% 목표

---

## 열린 질문 (해결됨)
- ✅ 스킵 기능: 제공
- ✅ 다시보기: 불필요 (새로고침으로 대체)
- ✅ 소요 시간: 단계당 30초~1분

---

## 산출물
- PRD: [opportunity-rating-tutorial.md](../prds/opportunity-rating-tutorial.md)
