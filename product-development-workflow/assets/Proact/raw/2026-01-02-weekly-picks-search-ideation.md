# Proact 학습 로그 - 2026-01-02

**세션 주제:** Weekly Picks 탐색 개선 아이디에이션  
**참여자:** 제품 매니저, Claude (Ideation Agent)  
**날짜:** 2026년 1월 2일

---

## 새로 학습한 내용

### 1. Weekly Picks 기능 상세

**기능 목적:**
- 매주 새로운 Sequence 생성을 위한 트리거 역할

**현재 작동 방식:**
- 일주일간 새로 업데이트된 **모든 공고** 노출
- Relevant Score 기준 내림차순 정렬
- NAICS/PSC 필터 제공 (Default: Relevant Score 상위 10개 자동 선택)

**유저 행동 패턴:**
- 열심히 하는 유저: ~20개 공고 확인
- 일반 유저: 상위 10개 정도만 확인
- **최소 2개 이상 적합한 공고 발견** → Sequence 생성

---

### 2. 발견한 문제

**문제 규모:**
- 약 **10% 유저**가 "이번주 공고에는 내가 할 수 있는 공고가 없다" 피드백

**문제 원인 (2가지 케이스):**
1. **Case 1 (우리가 해결할 영역):** 
   - 실제로는 유저에게 적합한 공고가 게시되었지만
   - "탐색의 어려움"으로 발견하지 못함
   
2. **Case 2 (통제 불가):** 
   - 실제로 유저 비즈니스와 맞는 공고가 게시되지 않음

**구체적 문제 지점:**
- 적합한 공고가 **상위 70% 범위** 밖에 있으면 발견 실패
- 문제 조합:
  - Top 10 keyword 매칭의 한계
  - Weekly Picks 외 다른 탐색 방법 부재

---

### 3. Relevant Score 계산 로직 상세

**Vector 유사도 기반:**
1. **Base:** 모든 입찰공고 RFP 문서의 Top 10 keywords
2. **Search Query:** 온보딩에서 유저가 선택한 공고의 Top 10 keywords  
3. **Scoring:** Vector 유사도 계산 → Relevant Score

**Top 10 keyword 매칭의 한계 분석 (MECE):**

**축 1: Keyword 추출 문제**
- A1. 온보딩 시 선택한 1개 공고만으로는 유저 비즈니스 전체를 대표 못 함
  - 예: IT 컨설팅 회사가 "Network Security" 공고만 선택 → Cloud, Data Analytics 공고 놓침
- A2. 추출된 키워드가 너무 generic/specific
  - Generic: "support", "services" → 노이즈 많음
  - Specific: "Cisco ASA 5500 series" → 관련 공고 놓침

**축 2: Keyword 매칭 문제**
- B1. Semantic Gap (동의어/유사 개념 매칭 실패)
  - "Cloud Migration" vs "Data Center Modernization"
  - "Cybersecurity" vs "Information Assurance"
- B2. Context Blindness (맥락 무시)
  - "training" → AI model training vs employee training

**축 3: Scope 문제**
- C1. 유저 비즈니스 진화 미반영
  - 3개월 전: "IT Infrastructure"만 → 현재: "Cybersecurity"도 함

**가장 유력한 문제:** B1 (Semantic Gap) + A1 (온보딩 1개 공고 한계)

---

### 4. 입찰공고 데이터 구조

**Description 구성:**
1. **Project Background & Objective**
   - Background: 프로젝트 필요 이유, 현재 상황, 제약사항
   - Objective: 성공 시 달성 목표/결과
   
2. **Scope of Work**
   - 계약자가 제공해야 할 기능, 서비스, 통합
   - 보안/컴플라이언스 요구사항
   - 구체적 수치, 시스템명, 표준/정책 포함

**유저의 발견 메커니즘:**
- **Scope of Work** 섹션을 읽다가
- 특정 **키워드**가 눈에 들어오고
- 맥락상 자신의 비즈니스와 부합 → 발견!

---

### 5. NAICS/PSC 필터의 문제

**현재 방식:**
- Default 값을 "Relevant Score 기반 상위 10개"로 자동 설정

**문제:**
- Relevant Score 자체가 부정확하면, 필터도 부정확해짐
- 유저가 수동으로 조정 가능하지만, 대부분 Default 사용

---

### 6. 솔루션 방향 결정

**고려한 옵션:**
- **Option A:** Relevant Score 로직 자체 개선
- **Option B:** 추가 탐색 경로 제공 (Relevant Score 불완전 전제)

**선택:** Option B  
**이유:** Score 개선은 시간 오래 걸리고 불확실성 높음

---

### 7. 검색 기능 설계 상세

**기본 방향:**
- 키워드 직접 검색 (typing)
- 이유: 명확한 input/output, 노력의 상한 명확

**검색 범위:**
- 이번 주 새 공고의 **Title + Description** (전체 텍스트)
- 전체 DB는 포함 안 함 (Weekly Picks = 이번 주 트리거)

**검색창 노출 조건 (Progressive Disclosure):**
- **트리거:** 유저가 상위 10개 공고까지 스크롤
- **방식:** 스크롤 기반 (Option A 선택)
- 검토한 다른 옵션:
  - Option B: 클릭 기반 (N개 공고 클릭 시)
  - Option C: 시간 기반 (N초 체류 시)
  - Option D: 조합

**검색 결과 표시:**
- 매칭된 공고만 필터링
- Relevant Score 순서 유지 (변경 없음)

**결과 없음 처리:**
- **1차 검색 실패:** "결과가 없습니다. 다른 키워드로 검색해보세요"
- **2차 검색 실패:** "결과가 없습니다. 이번 주는 관련 공고가 없는 것 같아요. 다음 주에 다시 확인해보세요"
- 목적: 유저가 "진짜 없구나" 하고 납득하며 넘어갈 수 있게

**Placeholder 문구:**
- 예: "관심 기술이나 서비스 키워드를 검색해보세요"

---

### 8. 기대 효과 & Success Metric

**Primary Metric:**
- **검색을 통한 Sequence 생성 수** 증가

**Secondary Metric:**
- **Weekly Picks 리텐션** 개선
- 이탈률 10% → 감소 목표

**장기 비전:**
- Relevant Score가 완벽해질 수 없으므로
- 검색 기능은 **필수 탐색 기능**으로 자리매김 예상

---

### 9. 제품 철학 & 설계 원칙 학습

**명확한 Input/Output:**
- 유저가 들여야 하는 노력의 상한이 명확해야 함
- 예: "이 키워드 있으면 Good, 없으면 Pass"

**Progressive Disclosure:**
- 필요할 때만 기능 노출
- 너무 이른 노출 = 복잡도 증가
- 너무 늦은 노출 = 기회 놓침

**실패 경험의 납득성:**
- 유저가 시도했는데 결과가 없으면
- 깔끔하게 납득하고 넘어갈 수 있어야 함
- 불필요한 좌절감/피로감 방지

---

### 10. 기술적 실현 가능성 확인

**검색 구현:**
- Title + Description 전체 텍스트 검색
- 기술 난이도: **낮음**
- 방법:
  - PostgreSQL: `LIKE` 또는 `ILIKE` (대소문자 무시)
  - Full-text search: `ts_vector` 같은 고급 기능 활용 가능

**구현 복잡도:**
- 스크롤 기반 트리거: **낮음**
- 텍스트 검색 + 필터링: **낮음**
- 전체 feature: **Medium (2-3주 추정)**

---

## 다음 단계

1. ✅ Knowledge Base 문서 생성
2. 🔄 PRD (정책서) 작성
3. ⏭️ 기능정의서 작성
4. ⏭️ 프로토타입 개발

---

## 메모

- RFP Description 추출 프롬프트 받음 (별도 문서 참조)
- Relevant Score 개선은 장기 과제로 남겨둠
- NAICS/PSC 필터 개선도 향후 탐색 필요
