# Weekly Picks Outreach PRD 문서

**생성 일시**: 2026년 1월 22일
**최종 편집 일시**: 2026년 1월 22일
**상태**: 초안

---

## 1. Product 목표 & Success 정의

### 1.1. 제품 컨텍스트 요약

- Proact의 핵심 가치:
    > "정부 입찰 공고를 유저의 비즈니스와 연관도 높은 순으로 추천하여, 매주 새로운 영업 기회(Sequence) 발굴을 돕는다"
- 지금까지:
    - (1) Weekly Picks - 기존 유저 대상 매주 맞춤 공고 추천
    - (2) Sequence 생성 - 입찰 준비 프로세스 지원
- 새로 추가하는 Weekly Picks Outreach:
    - (3) 서비스 외부 유저(60k+ 컨택리스트) 대상 개인화된 공고 추천 이메일 발송

### 1.2. 왜 Weekly Picks Outreach가 중요한가

- 현재 콜드메일의 문제점: **"적시성 부재"**
    - 콜드메일 수신자(SAM.gov 등록 완료, Award 0)가 지금도 B2G에 관심 있는지 알 수 없음
    - 일반적인 가치 제안만으로는 행동 유도가 어려움
- Weekly Picks Outreach의 해결책:
    - 실제 관련 공고를 구체적으로 제시 → "이 공고가 너의 비즈니스와 맞아 보인다"
    - B2G 관심이 식은 사람 → 관심 재점화 ("너의 Revenue Channel이 여기 있다")
    - B2G 관심이 뜨거운 사람 → Shortcut 제공 (Teaming 솔루션)

> 따라서 Weekly Picks Outreach의 최우선 목표:
> - *"지속 가능한 CAC 효율의 외부 유저 유입 시스템 구축"*
> - *"CTR 40%+ / 전환율 1%+ 달성 (현재 30% / 0.5% 대비)"*

---

## 2. JTBD 정의

### JTBD #1 - "관련 B2G 기회 발견" (잠재 고객 관점)

> **When**
> 나는 SAM.gov에 등록했지만 아직 실적이 없고, 어떤 공고가 내 비즈니스에 맞는지 모를 때

> **I want to**
> 내 비즈니스 역량에 딱 맞는 정부 입찰 공고를 쉽게 찾고 싶다

> **So that**
> 첫 번째 B2G 성공 사례를 만들 수 있다

---

### JTBD #2 - "효율적인 리드 발굴" (Proact 팀 관점)

> **When**
> 우리는 매주 새로운 Weekly Picks 공고가 업데이트될 때

> **I want to**
> 이 공고들과 가장 잘 매칭되는 외부 기업들에게 자동으로 개인화된 이메일을 발송하고 싶다

> **So that**
> 지속 가능한 비용으로 Landing Page 유입과 전환을 늘릴 수 있다

---

### JTBD #3 - "B2G 관심 재점화" (휴면 잠재 고객 관점)

> **When**
> 나는 예전에 B2G에 관심 있었지만 어려워서 포기했을 때

> **I want to**
> 내 비즈니스에 실제로 맞는 구체적인 기회를 보고 싶다

> **So that**
> B2G가 나와 상관없는 게 아니라 실제 Revenue Channel이 될 수 있다고 느낄 수 있다

---

## 3. 유저 가치 & 비즈니스 가치 정리

### 유저 가치 (이메일 수신자)

1. **적시성 있는 기회 발견**
    - 일반적인 "B2G 해보세요" 메시지가 아닌, 이번 주 실제 공고 기반 구체적 제안
2. **개인화된 연관성 설명**
    - "이 공고의 [Scope of Work]가 당신의 [Business Portfolio]와 연관됩니다" 형태의 명확한 이유 제시
3. **진입 장벽 낮춤**
    - Teaming 파트너 연결 제안 (향후 Algorithm A 적용 시)

### 비즈니스 가치 (Proact)

1. **지속 가능한 리드 파이프라인**
    - 일회성 콜드메일 → 매주 새 콘텐츠 기반 시스템으로 전환
2. **CAC 최적화**
    - 대량 발송 + LLM 생성 비용 대비 전환 ROI 측정 가능
3. **데이터 자산 활용**
    - 60k+ 컨택리스트와 Weekly Picks 데이터의 시너지

---

## 4. Weekly Picks Outreach 전체 유저 플로우 (High-level)

### Flow A. Algorithm B - 기업당 Top N 공고 추천 (MVP)

- Entry Point: **매주 Weekly Picks 업데이트 후 파이프라인 실행**
- Outreach 프로세스 (시스템 주도)
    - Step 1: 60k 기업 Company_Summary/Portfolio를 Embedding
    - Step 2: 각 기업에 대해 2,000개 Weekly Picks와 유사도 계산 → Top N 추출
    - Step 3: LLM이 Top N을 검증 + "Why Relevant" 설명 생성
    - Step 4: 개인화된 이메일 발송 (뉴스레터 형식)
- 수신자 경험:
    - "이번 주 당신을 위한 Top 5 B2G 기회" 이메일 수신
    - 각 공고별 "왜 관련있는지" 설명 포함
    - CTA: Proact Landing Page 방문

---

### Flow B. Algorithm A - 공고당 Top 100 기업 선정 (향후)

- Entry Point: **Algorithm B 성공 검증 후 시도**
- Outreach 프로세스
    - Step 1: 각 Weekly Pick 공고에 대해 60k 기업과 유사도 계산
    - Step 2: 공고당 Top 100 기업 선정 (중복 시 상위 공고로 귀속)
    - Step 3: "이 공고 + Teaming 파트너 연결" 형태의 1:1 제안 이메일 발송
- 수신자 경험:
    - "이 공고가 당신의 비즈니스와 맞아 보입니다" 개별 제안 수신
    - Teaming 파트너 소개 (해당 Agency 경험자)
    - CTA: Proact Landing Page 방문

---

## 5. 기술 구현 상세

### 5.1. 데이터 소스

**Company 컨택리스트 (60k+)**
- 출처: SAM.gov 등록정보 + 자체 수집
- 필드:
    - Email, First_Name, Company_Name
    - Primary_NAICS_Code, Primary_NAICS_Description
    - State, Set_Aside_Status, Registration_Year
    - **Company_Summary** (핵심 - 매칭에 사용)
    - **Company_Business_Portfolio** (핵심 - 매칭에 사용)
    - Company_Reference
- 데이터 품질: 정확하고 구체적 (검증됨)

**Weekly Picks (주간 2,000개)**
- 출처: Proact 기존 인프라
- 필드:
    - Title, Description (Background & Objective + Scope of Work)
    - Top 10 Keywords
    - NAICS/PSC 코드
- Embedding 베이스: Keyword vs Description 둘 다 테스트 예정

---

### 5.2. 매칭 알고리즘 - 2-Stage Approach

**Stage 1: Embedding 기반 Top N 추출**
- Company_Summary + Business_Portfolio → Embedding Vector
- 공고 [Keyword or Description] → Embedding Vector
- Vector 유사도 계산 → 각 기업당 Top N 공고 추출
- N 값: 테스트를 통해 최적값 결정 (초기 10~20 예상)

**Stage 2: LLM 검증 + Why Relevant 생성**
- Input: Company 정보 + Top N 공고 정보
- LLM 작업:
    1. 진짜 관련있는지 판단 (Yes/No + Confidence)
    2. 최종 Top 5 선정
    3. 각 공고에 대해 "Why Relevant" 설명 생성
- Output: 기업당 최종 5개 공고 + 각각의 관련성 설명

**Embedding 베이스 테스트 계획**
- Option A: Keyword 기반 - 핵심 집중, 노이즈 적음
- Option B: Description 기반 - Semantic 풍부함, Recall 우선
- 평가 방법:
    - 배포 전: 수동 샘플링 + LLM-as-judge
    - 배포 후: 이메일 성과 기반 (CTR, 전환율)

---

### 5.3. 비용 추정

| 항목 | 산출 근거 | 주간 비용 |
|------|-----------|-----------|
| Embedding 생성 (1회성) | 60k 기업 × Company Summary | 초기 $50-100 |
| Embedding 검색 (주간) | 60k × 2,000 유사도 계산 | OpenSearch 비용 |
| LLM 검증 (주간) | 60k × Top N (10~20) | $150-300 |
| Why Relevant 생성 (주간) | 60k × 5 = 300k 설명 | LLM 비용에 포함 |
| 이메일 발송 | 최대 60k건 | SendGrid/SES 비용 |

- **LLM 크레딧**: $80,000 보유 (충분)
- **시간 제약**: 2-3일 여유 있음 (Weekly Picks 업데이트 후)

---

### 5.4. 이메일 콘텐츠 구조 (Algorithm B)

**제목**: "이번 주 [Company_Name]을 위한 Top 5 B2G 기회"

**본문 구조**:
```
Hi [First_Name],

이번 주 새로 올라온 정부 입찰 공고 중,
[Company_Name]의 비즈니스와 연관성이 높아 보이는 기회들을 정리했습니다.

━━━━━━━━━━━━━━━━━━━━━━━━

🎯 #1. [공고 Title]
왜 관련있나요?
→ "[Why Relevant 설명 - Company Portfolio와 Scope of Work 연결]"

🎯 #2. [공고 Title]
왜 관련있나요?
→ "[Why Relevant 설명]"

... (총 5개)

━━━━━━━━━━━━━━━━━━━━━━━━

이 기회들로 첫 번째 B2G Success Case를 만들어보고 싶으시다면?
→ [Proact에서 더 알아보기] (CTA Button)

1,000+ B2G 전문 벤더들의 도움을 받을 수 있습니다.
```

---

## 6. MVP 정의

### 6.1. 범위

- **대상**: 1,000개 기업 샘플 (60k 중 선정)
- **알고리즘**: Algorithm B (기업당 Top 5 공고)
- **Embedding 테스트**: Keyword vs Description 병렬 테스트 (500개씩)
- **평가 기간**: 2주

### 6.2. 성공 기준

| 지표 | 현재 Baseline | MVP 목표 |
|------|---------------|----------|
| CTR (Landing 유입) | 30% | 40%+ |
| 전환율 (회원가입/미팅) | 0.5% | 1%+ |
| CAC | 측정 필요 | 지속 가능한 수준 |

### 6.3. 테스트 흐름

1. 1,000개 기업 샘플 선정 (NAICS 다양성 고려)
2. Embedding 생성 (Company Summary + Portfolio)
3. 2-Stage 매칭 실행 (Top N + LLM 검증)
4. 이메일 발송 (500개: Keyword 매칭 / 500개: Description 매칭)
5. 2주간 성과 추적 (Open, Click, 회원가입)
6. 결과 분석 및 최적 설정 결정

---

## 7. Open Questions

### 2026년 1월 22일 - Ideation 세션

**논의 내용**:
- Algorithm A (공고 중심) vs Algorithm B (기업 중심) 비교
- Embedding 베이스: Keyword vs Description
- 2-Stage 접근법 (Embedding → LLM 검증) 합의

**결정 사항**:
- MVP는 Algorithm B로 시작 (현재 매칭 정밀도로 "하나의 최적 공고" 판단 어려움)
- Embedding 베이스는 둘 다 테스트
- Description 매칭 품질이 좋으면 향후 Algorithm A (Teaming 연결) 시도

**남은 불확실성**:
- Company ↔ 공고 매칭 품질 (실제 테스트 필요)
- 최적 Top N 값 (샘플 테스트로 결정)
- Why Relevant 설명의 적정 길이/형식

---

## 8. 향후 확장 계획

### Phase 2: Algorithm A 도입 (조건부)

**전제 조건**: MVP에서 Description 기반 매칭 품질이 충분히 검증됨

**Algorithm A 차별점**:
- 공고당 Top 100 기업 → 1:1 개별 제안
- Teaming 파트너 연결 ("이 Agency와 일해본 경험자 소개")
- 더 강한 개인화 느낌

### Phase 3: 자동화 및 최적화

- Weekly 파이프라인 완전 자동화
- A/B 테스트 프레임워크 구축 (제목, 본문, CTA 변형)
- 성과 기반 Top N 동적 조정

---

## 9. 참고자료

- [Proact Knowledge Base](/assets/Proact/proact-knowledge-base.md)
- [Weekly Picks 탐색 개선 PRD](/assets/Proact/prds/) (향후 링크)
- Company 컨택리스트 데이터 스키마 (내부 문서)
