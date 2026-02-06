# Proact Knowledge Asset

이 폴더는 Proact 제품에 대한 지식을 축적하고 관리하는 곳입니다.

## 📁 폴더 구조

```
assets/Proact/
├── README.md                                      # 이 파일
├── proact-knowledge-base.md                      # 원천 문서 (최신 통합 버전)
├── prds/                                          # PRD 문서들 (피쳐별 폴더)
│   ├── opportunity-rating-tutorial/
│   │   ├── README.md                             # 정책서
│   │   ├── detailed-policy.md                    # 상세 정책서
│   │   └── feature-spec.md                       # 기능정의서
│   ├── opportunity-relevance-indicator/
│   │   ├── README.md
│   │   ├── detailed-policy.md
│   │   └── feature-spec.md
│   ├── weekly-picks-outreach/
│   │   ├── README.md
│   │   ├── detailed-policy.md
│   │   ├── feature-spec.md
│   │   └── tech-spec.md
│   └── weekly-picks-search/
│       └── README.md
└── raw/                                           # 세션별 학습 로그
    └── 2026-01-02-weekly-picks-search-ideation.md
```

## 📄 문서 역할

### 1. `proact-knowledge-base.md` (원천 문서)
- **목적:** Proact에 대한 모든 학습 내용을 통합한 최신 버전
- **업데이트 시점:** 새로운 세션에서 학습한 내용이 있을 때마다
- **사용:** 다음 아이디에이션 시작 시 이 문서를 먼저 읽고 컨텍스트 파악

**포함 내용:**
- 제품 개요 (목적, 타겟 유저, 핵심 가치)
- 핵심 기능 및 워크플로우
- 데이터 구조
- 현재 문제점 및 해결 방향
- 제품 철학 및 설계 원칙
- 주요 결정사항 기록
- 용어집

### 2. `raw/` 폴더 (세션별 로그)
- **목적:** 특정 아이디에이션 세션에서 새로 학습한 내용을 기록
- **명명 규칙:** `YYYY-MM-DD-[주제]-[타입].md`
  - 예: `2026-01-02-weekly-picks-search-ideation.md`
- **사용:** 
  - 원천 문서 업데이트 시 참조
  - 히스토리 추적 및 의사결정 맥락 이해

**포함 내용:**
- 세션 주제 및 날짜
- 새로 학습한 기능/문제/솔루션 상세
- 의사결정 과정 및 논의 내용
- 기술적 실현 가능성 검증
- 다음 단계

### 3. `prds/` 폴더 (정책서/PRD 문서)
- **목적:** 완성된 PRD 문서 보관
- **명명 규칙:** `YYYY-MM-DD-[기능명].md`
  - 예: `2026-01-02-weekly-picks-search.md`
- **사용:**
  - 개발팀 핸드오프
  - 기능정의서 작성 시 참조
  - 향후 기능 개선 시 기준 문서

**포함 내용:**
- Product 목표 & Success 정의
- JTBD (Jobs-to-be-Done)
- 유저/비즈니스 가치
- 전체 유저 플로우
- 상세 플로우 및 디자인 의도
- 기술 사양
- Success Metrics

## 🔄 업데이트 워크플로우

### 새로운 아이디에이션 시작 시:
1. `proact-knowledge-base.md` 읽기
2. 기존 컨텍스트 파악
3. 아이디에이션 진행

### 아이디에이션 종료 시:
1. `raw/YYYY-MM-DD-[주제]-[타입].md` 생성
2. 새로 학습한 내용 기록
3. PRD 작성 시: `prds/YYYY-MM-DD-[기능명].md` 생성
4. `proact-knowledge-base.md` 업데이트
   - 새로운 정보 추가
   - 기존 정보 수정/보완
   - 업데이트 로그 작성

## 📝 문서 작성 가이드

### Raw 문서 작성 시:
- ✅ 해당 세션에서 **새로 알게 된 내용**만 기록
- ✅ 구체적인 숫자, 예시, 의사결정 근거 포함
- ✅ "왜 이 결정을 내렸는지" 맥락 기록
- ❌ 이미 원천 문서에 있는 내용 중복 금지

### 원천 문서 업데이트 시:
- ✅ 날짜별로 업데이트 로그 작성
- ✅ 상충되는 정보는 최신 정보로 교체 (변경 이유 로그에 기록)
- ✅ 관련 섹션에 통합 (새 섹션 추가 지양)
- ✅ 용어집 지속 업데이트

## 🎯 이 폴더의 목표

1. **컨텍스트 전환 비용 최소화**
   - 다음 세션 시작 시 빠른 컨텍스트 파악
   
2. **지식 누적**
   - 세션마다 배운 내용이 사라지지 않고 축적
   
3. **의사결정 히스토리 관리**
   - 왜 이 방향으로 갔는지 추적 가능
   
4. **팀 온보딩**
   - 새로운 팀원이 Proact 이해 시 참고 자료

---

**최초 생성:** 2026년 1월 2일  
**마지막 업데이트:** 2026년 1월 2일
