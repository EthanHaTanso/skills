# Proact Knowledge Base

**문서 목적:** Proact 제품에 대한 지식을 축적하여 향후 아이디에이션 시 컨텍스트를 빠르게 이해할 수 있도록 함  
**최초 생성:** 2026년 1월 2일  
**최종 업데이트:** 2026년 1월 29일

---

## 1. 제품 개요

### 1.1. Proact란?
- **제품명:** Proact
- **도메인:** 미국 정부 입찰 공고 추천 및 Sequence 생성 플랫폼
- **핵심 가치 제안:** 정부 입찰 공고를 유저의 비즈니스와 연관도 높은 순으로 추천하여, 매주 새로운 영업 기회(Sequence) 발굴을 돕는다

### 1.2. 타겟 유저
- 미국 정부 입찰에 참여하는 기업들 (주로 B2G 사업자)
- IT, 컨설팅, 인프라, 보안 등 다양한 업종

---

## 2. 핵심 기능 및 워크플로우

### 2.1. 온보딩 프로세스
**목적:** 유저의 비즈니스 관심사를 파악하여 개인화된 공고 추천의 기준점 설정

**프로세스:**
1. 유저가 Proact DB에 있는 입찰공고 중 "자신의 비즈니스와 연관도가 높다"고 판단하는 공고를 **1개 이상 선택**
2. 선택된 공고의 **Top 10 keywords**를 추출
3. 이를 "Search Query"로 사용하여 전체 공고와의 유사도 계산

**Company Description 구조** (2026-01-26 추가):
- 시스템이 웹검색으로 자동 생성
- 구성: **Summary + Business Portfolio**
  - Summary: 회사에 대한 간단한 설명
  - Business Portfolio: [아이템명 / 아이템 설명] 형식의 사업 영역 리스트
- 예시 (Google):
  ```
  Google is a global technology company providing diverse internet-related
  services and products, primarily generating revenue through online advertising.

  Business Portfolio:
  - Cloud Computing: Offers scalable infrastructure through Google Cloud.
  - Artificial Intelligence: Integrates advanced AI technologies across products.
  - ...
  ```

**현재 한계:**
- 1개 공고만으로는 유저의 전체 비즈니스 역량/관심사를 충분히 커버하기 어려움
- 유저의 비즈니스가 진화/확장해도 온보딩 시점의 선택만 반영됨

---

### 2.2. Relevant Score 계산 로직

**방식:** Vector 유사도 기반 매칭

**계산 과정:**
1. **Base:** Proact이 수집한 모든 입찰공고의 RFP 문서에서 **Top 10 keywords** 추출
2. **Search Query:** 온보딩에서 유저가 선택한 공고의 **Top 10 keywords**
3. **Scoring 대상:** 모든 입찰공고의 Top 10 keywords
4. Vector 유사도 계산 → **Relevant Score** 산출

**현재 한계:**
- **Semantic Gap:** 동일 개념을 다른 용어로 표현 시 매칭 실패
  - 예: "Cloud Migration" vs "Data Center Modernization"
  - 예: "Cybersecurity" vs "Information Assurance"
- **Context Blindness:** 키워드는 같지만 의미가 다른 경우 오매칭
  - 예: "training" → AI model training vs employee training
- **Generic/Specific 문제:** 
  - 너무 넓은 키워드(예: "support", "services") → 노이즈 많음
  - 너무 좁은 키워드(예: "Cisco ASA 5500 series") → 관련 공고 놓침

---

### 2.3. Weekly Picks 기능

**목적:** 매주 새로운 Sequence 생성을 위한 트리거 제공

**작동 방식:**
1. **일주일간 새로 업데이트된 모든 공고**를 보여줌
2. **Relevant Score 기준 내림차순 정렬**
3. **NAICS/PSC 코드 필터** 제공 (Default: Relevant Score 상위 10개 자동 선택)

**유저 행동:**
- 열심히 하는 유저: 약 20개 공고까지 확인
- 일반 유저: 상위 10개 정도만 확인
- 최소 **2개 이상 적합한 공고**를 발견하면 Sequence 생성으로 이어짐

**현재 문제:**
- 약 **10% 유저**가 "이번주 공고에는 내가 할 수 있는 공고가 없다"고 피드백
- 실제로는 적합한 공고가 있지만, **상위 70% 범위 밖**에 있어서 발견하지 못함
- Weekly Picks 외 다른 탐색 방법이 없어서, 못 찾으면 **제품 이탈**

---

### 2.4. 입찰공고 데이터 구조

**공고당 추출 정보:**
1. **Title:** 공고 제목
2. **Description:** RFP 문서에서 추출한 핵심 요약
   - **1) Project Background & Objective**
   - **2) Scope of Work**
3. **NAICS/PSC 코드:** 산업 분류 코드
4. **Top 10 keywords:** Relevant Score 계산에 사용

**Description 추출 프롬프트:**
- Background: 프로젝트가 필요한 이유, 현재 상황, 제약사항, 기존 시스템
- Objective: 프로젝트 성공 시 달성할 목표/결과
- Scope of Work: 계약자가 제공해야 할 핵심 기능, 서비스, 통합, 보안/컴플라이언스 요구사항

**유저의 공고 발견 메커니즘:**
- Description의 **Scope of Work 부분**을 읽다가
- 특정 **키워드**가 눈에 들어오고
- 맥락상 자신의 비즈니스 아이템과 부합한다고 판단 → 발견!

---

## 3. 핵심 메트릭

### 3.1. 제품 성공 지표
- **Sequence 생성 수:** 유저가 Weekly Picks에서 공고를 발견하고 실제로 입찰 준비(Sequence)를 시작한 횟수
- **Weekly Picks 리텐션:** 매주 Weekly Picks를 확인하고 계속 사용하는 유저 비율
- **Engagement 증가:** 지속적인 제품 사용으로 이어지는 유저 활동도

### 3.2. 현재 문제 지표
- 약 **10% 유저**가 Weekly Picks에서 원하는 공고를 찾지 못하고 이탈
- 적합한 공고가 **상위 70% 범위** 밖에 있으면 발견 실패

---

## 4. 제품 철학 및 설계 원칙

### 4.1. Aha-Moment 정의
- **"내 비즈니스에 딱 맞는 정부 입찰 공고를 매주 자동으로 받아볼 수 있다"**
- Weekly Picks가 이 Aha-Moment의 핵심 트리거

### 4.2. 유저 경험 설계 원칙
- **명확한 Input/Output:** 유저가 들여야 하는 노력의 상한이 명확해야 함
  - 예: "이 키워드 있으면 Good, 없으면 Pass" ← 노력의 상한이 명확
- **Progressive Disclosure:** 필요할 때만 기능 노출
  - 예: 상위 10개 확인 후에도 못 찾으면 검색창 노출
- **실패 경험의 납득성:** 유저가 시도했는데 결과가 없으면, 깔끔하게 납득하고 넘어갈 수 있어야 함

---

## 5. 기술 스택 (추정)

### 5.1. 데이터 수집
- 미국 정부 입찰 공고 크롤링 및 DB 저장
- RFP 문서 파싱 및 구조화

### 5.2. AI/ML
- Keyword 추출: Top 10 keywords 자동 추출
- Vector 유사도 계산: Relevant Score 산출
- NLP: Description 요약 생성 (Background, Objective, Scope of Work)

### 5.3. 프론트엔드
- Weekly Picks 리스트 UI
- 필터링 (NAICS/PSC)
- (향후) 키워드 검색 기능

---

## 6. 주요 결정 사항 기록

### 2026년 1월 2일 - Weekly Picks 탐색 개선 아이디에이션

**결정:**
- Relevant Score 로직 개선(Option A)보다 **추가 탐색 경로 제공(Option B)** 선택
- 이유: Score 개선은 시간이 오래 걸리고 불확실성 높음

**세부 설계:**
- 유저가 상위 10개 스크롤 시 키워드 검색창 노출 (Progressive Disclosure)
- 검색 범위: 이번 주 새 공고의 Title + Description
- 검색 결과: 매칭된 공고만 필터링 (Relevant Score 순서 유지)
- 결과 없음 처리:
  - 1차: "결과가 없습니다. 다른 키워드로 검색해보세요"
  - 2차: "결과가 없습니다. 이번 주는 관련 공고가 없는 것 같아요. 다음 주에 다시 확인해보세요"

**기대 효과:**
- 검색을 통한 Sequence 생성 수 증가
- Weekly Picks 리텐션 개선 (이탈률 10% → 감소 목표)
- 장기적으로 필수 탐색 기능으로 자리매김

### 2026년 1월 26일 - Opportunity Relevance Indicator 아이디에이션

**문제:**
- 온보딩 중 [Opportunity 리스트 확인] → [Relevant Opportunity 선택] 전환율이 **50%**로 기대 이하
- 공고 하나당 3-5분 투자 필요 (Title에 구체 정보 없어 Description 전체 읽어야 함)
- 가설: 적합한 공고가 있지만 유저가 판단하지 못하는 케이스 존재

**결정:**
- **매칭 태그 + 본문 하이라이트** 조합 채택
- 태그: Business Portfolio 아이템명 표시 (빠른 스캔)
- 하이라이트: Description 내 매칭 문장에 형광색 표시 (맥락 제공)
- 매칭 방식: Semantic 매칭 (단순 키워드 아닌 의미 기반)

**세부 설계:**
- 태그 개수: 제한 없음 (Portfolio 아이템 수가 많지 않음)
- 하이라이트 범위: Description 전체
- 하이라이트 상한: Description의 20%
- 매칭 없는 공고: 태그 없이 그대로 표시

**성공 지표:**
- 전환율 50% → **80%** 목표

**참고 PRD:** `prds/opportunity-relevance-indicator.md`

### 2026년 1월 29일 - Opportunity Rating Tutorial 아이디에이션

**문제:**
- 온보딩 중 [Opportunity Load → "Interested" Rating] 전환율이 **50%**
- 유저가 Opportunity 선별 맥락을 오해: "내가 직접 수주할 프로젝트"를 고르는 것으로 이해
- 실제 의도: "일부라도 수행 가능한 프로젝트"를 고르면 함께 수주할 파트너를 찾아줌

**결정:**
- Company Profile Confirm → Opportunity Load 사이 **로딩 중 튜토리얼** 제공
- 순차 애니메이션 3단계 구성, 각 단계 30초~1분
- Mock UI는 실제 데이터 활용 (가짜 데이터 금지)

**튜토리얼 구성:**
| 단계 | 내용 | 목적 |
|------|------|------|
| Step 1 | 페이지 개요 + 유저 과업 + 결과(파트너 매칭) | "왜 이걸 하는지" 이해 |
| Step 2 | 기본 Opportunity 카드 (매칭 기능 없이) | "무엇을 보는지" 이해 |
| Step 3 | 매칭 태그 + 하이라이트 (기본 UI mute) | "어떻게 판단하는지" 이해 |

**핵심 메시지:**
> "일부라도 수행할 수 있는 프로젝트를 고르세요. 우리가 함께 수주할 파트너를 찾아드릴게요."

**인터랙션:**
- 스킵 기능: 제공
- 다시보기: 불필요 (새로고침 시 다시 표시)

**성공 지표:**
- 전환율 50% → **80%** 목표

**참고 PRD:** `prds/opportunity-rating-tutorial.md`

---

## 7. 향후 탐색 필요 영역

### 7.1. Relevant Score 개선 방향 (장기)
- Semantic Gap 해결: 동의어/유사 개념 매칭 개선
- Context-aware matching: 문맥 이해 기반 매칭
- Multi-signal 통합: Top 10 keywords 외 다른 신호 추가

### 7.2. 온보딩 개선
- 1개 공고 선택의 한계 극복
- 유저 비즈니스 변화 반영 메커니즘

### 7.3. 필터링 정확도 개선
- NAICS/PSC Default 값이 Relevant Score 기반이라 부정확
- 다른 방식의 Default 설정 고려

---

## 8. 용어집

| 용어 | 정의 |
|------|------|
| **Weekly Picks** | 매주 새로 업데이트된 공고 중 유저의 비즈니스와 연관도 높은 공고를 추천하는 기능 |
| **Sequence** | 유저가 특정 입찰 공고에 대해 생성하는 영업/입찰 준비 프로세스 |
| **Relevant Score** | 온보딩 시 선택한 공고와의 Vector 유사도를 기반으로 계산된 공고 추천 점수 |
| **Top 10 keywords** | RFP 문서에서 추출한 가장 중요한 10개의 키워드 |
| **NAICS/PSC** | 북미 산업 분류 체계 / 제품·서비스 코드 (공고 필터링에 사용) |
| **RFP** | Request for Proposal (제안 요청서) - 정부 입찰 공고 문서 |
| **Description** | 공고의 핵심 내용 요약 (Background & Objective + Scope of Work) |
| **Company Description** | 시스템이 웹검색으로 자동 생성한 유저 회사 정보 (Summary + Business Portfolio) |
| **Business Portfolio** | Company Description의 구성 요소로, 유저 회사의 사업 영역 리스트 (아이템명/설명) |
| **매칭 태그** | Opportunity 카드에 표시되는 Business Portfolio 아이템명 태그 |
| **Semantic 매칭** | 단순 키워드가 아닌 의미 기반으로 Company Description과 Opportunity를 연결하는 방식 |

---

## 9. 참고자료

- RFP Description 추출 프롬프트: [2026-01-02 아이디에이션 세션에서 제공받음]
- Weekly Picks 개선 PRD: [작성 예정]

---

## 업데이트 로그

- **2026-01-29:** Opportunity Rating Tutorial 아이디에이션 내용 추가 (온보딩 튜토리얼)
- **2026-01-26:** Opportunity Relevance Indicator 아이디에이션 내용 추가, Company Description 구조 문서화, 용어집 확장
- **2026-01-02:** 초기 문서 생성 (Weekly Picks 탐색 개선 아이디에이션 기반)
