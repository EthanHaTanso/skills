# MVP Ideation 템플릿

**Version**: 1.0
**Date**: 2026-02-04
**Purpose**: JTBD 완료 후 MVP 아이디어를 간단히 정리하는 내부 문서

이 문서는 **내부용**입니다. JTBD 분석이 완료된 후, 상세한 MVP Proposal을 작성하기 전에 핵심 아이디어를 빠르게 정리하는 단계입니다.

---

## 언제 사용하나?

**Phase 1 (JTBD) 완료 후 → Phase 2 (MVP Proposal) 시작 전**

```
JTBD 완료
    ↓
[Follow-up 질문 있나?]
    ↓
    ├─ 없음 → 바로 MVP Ideation 진행 → MVP Proposal
    │
    └─ 있음 → 사용자에게 "MVP Ideation 진행할까요?" 물어보기
        ↓
        ├─ Yes → MVP Ideation (질문 포함) → 답변 수합 → Ideation 업데이트 → MVP Proposal
        │
        └─ No → 답변 수합 먼저 → MVP Ideation → MVP Proposal
```

---

## MVP Ideation 구조

```markdown
# MVP Ideation: [Solution 이름]

**User**: [인터뷰이 이름] ([직무])
**Date**: [YYYY-MM-DD]
**Status**: 💡 Ideation / 🔍 Follow-up 대기 / ✅ Ready for Proposal

---

## 1. Core Problem (from JTBD)

**Top 3 Pain Points**:
1. [Pain Point 1 - 한 줄 요약]
2. [Pain Point 2 - 한 줄 요약]
3. [Pain Point 3 - 한 줄 요약]

**Impact**:
- 시간: [현재 소요 시간]
- 빈도: [얼마나 자주 발생]
- 감정: [인터뷰이가 표현한 감정]

---

## 2. Core Solution Idea

**핵심 아이디어** (1-2문장):
> [AI가 어떻게 문제를 해결할 수 있는지 핵심 아이디어]

**예시**:
> "거래 내역을 자동으로 tracking하고 AI가 comment 초안을 생성하면, 사용자는 Yes/No만 클릭"

---

## 3. Key Features (MVP v1.0)

**필수 기능 3-5개**:

1. **[기능 1 이름]**
   - 목적: [왜 필요한가]
   - 동작: [어떻게 작동하나 - 1줄]

2. **[기능 2 이름]**
   - 목적: [왜 필요한가]
   - 동작: [어떻게 작동하나 - 1줄]

3. **[기능 3 이름]**
   - 목적: [왜 필요한가]
   - 동작: [어떻게 작동하나 - 1줄]

[4-5개 기능...]

---

## 4. Out of Scope (v1.1 이후)

**제외 항목**:
- ❌ [제외 기능 1] - 이유: [왜 제외]
- ❌ [제외 기능 2] - 이유: [왜 제외]
- ❌ [제외 기능 3] - 이유: [왜 제외]
- ❌ [제외 기능 4] - 이유: [왜 제외]

---

## 5. Expected Impact

**정량적**:
- 시간 절약: [현재] → **[목표]**
- [지표 2]: [현재] → **[목표]**

**정성적**:
- [기대 효과 1]
- [기대 효과 2]
- Big Fan 가능성: [HIGH/MEDIUM/LOW]

---

## 6. Open Questions (Follow-up)

**질문 있음**: ✅ / ❌

### [카테고리 1] 관련
1. [질문 1]
2. [질문 2]

### [카테고리 2] 관련
1. [질문 1]
2. [질문 2]

**답변 수합 필요 여부**:
- [ ] 답변 없이도 MVP Proposal 작성 가능 (질문만 포함)
- [ ] 답변 수합 후 Ideation 업데이트 필요 (scope 영향 큼)

---

## 7. Next Step

**현재 상태**:
- [ ] Ideation 완료 → MVP Proposal 작성 가능
- [ ] Follow-up 답변 대기 중
- [ ] Follow-up 답변 반영 후 MVP Proposal 작성

**Proposal 작성 준비도**: [Ready / Waiting for answers]

---

**JTBD Document**: [Link to JTBD]
**Last Updated**: [YYYY-MM-DD]
```

---

## 작성 가이드

### DO
- ✅ **간단하게**: 1-2줄 요약 수준으로 작성
- ✅ **핵심만**: 상세 설명은 MVP Proposal에서
- ✅ **빠르게**: 10-15분 내에 작성 가능해야 함
- ✅ **내부용**: 기술 용어 사용 OK, 사용자 친화적 언어 불필요

### DON'T
- ❌ **상세 설명**: UI 목업, 시나리오 등은 MVP Proposal에서
- ❌ **사용자 언어**: 내부 문서이므로 기술 용어 사용 OK
- ❌ **완벽주의**: 빠른 아이디어 정리가 목적

### 작성 시간
- **10-15분**: 빠른 브레인스토밍
- **상세 내용은 MVP Proposal에서**

---

## 저장 위치

MVP Ideation 문서는 JTBD와 같은 폴더에 저장:

```
./User Discover/User Interview/
├── USER_001_2026-02-03.md              # JTBD 문서
└── USER_001_2026-02-03_ideation.md     # MVP Ideation (NEW!)
```

또는 P-S Tree에 임시 저장 후 MVP Proposal로 전환:

```
./P-S Tree/[Business Function]/[Problem]/
├── _ideation.md                        # MVP Ideation (임시)
└── [Solution].md                       # MVP Proposal (최종)
```

---

## Follow-up Question 처리 플로우

### Case 1: Follow-up 질문 없음
```
JTBD 완료
    ↓
MVP Ideation 작성 (5분)
    ↓
MVP Proposal 작성 (템플릿 기반)
```

### Case 2: Follow-up 질문 있음 → 바로 Ideation
```
JTBD 완료 (Follow-up 질문 있음)
    ↓
사용자에게 질문: "MVP Ideation 진행할까요?"
    ↓
Yes
    ↓
MVP Ideation 작성 (Open Questions 섹션 포함)
    ↓
사용자에게 Follow-up 질문 전달
    ↓
답변 수합
    ↓
MVP Ideation 업데이트 (답변 반영)
    ↓
MVP Proposal 작성
```

### Case 3: Follow-up 질문 있음 → 답변 먼저
```
JTBD 완료 (Follow-up 질문 있음)
    ↓
사용자에게 질문: "MVP Ideation 진행할까요?"
    ↓
No (답변 먼저 수합)
    ↓
Follow-up 답변 수합
    ↓
JTBD 문서 업데이트
    ↓
MVP Ideation 작성 (답변 반영됨)
    ↓
MVP Proposal 작성
```

---

## Example: AI Tax Assistant

```markdown
# MVP Ideation: AI Tax Assistant

**User**: 조윤수 (CEO & Founder)
**Date**: 2026-02-04
**Status**: 🔍 Follow-up 대기

---

## 1. Core Problem

**Top 3 Pain Points**:
1. Context switching: 본업 아닌 행정 작업에서 불필요한 전환
2. 세무사 설명 부담: Context 없는 타인에게 매번 설명
3. 시간 소모: 새벽 1시까지 작업

**Impact**:
- 시간: 새벽 1시까지 (정확한 시간 미확인)
- 빈도: 거의 매일 (주 10회 거래)
- 감정: "진절머리 난다"

---

## 2. Core Solution Idea

> "거래 내역을 자동 tracking하고 AI가 comment 초안 생성 → 사용자는 Yes/No만 클릭 → 세무사에게 자동 전달"

---

## 3. Key Features (MVP v1.0)

1. **거래 내역 자동 수집**
   - 목적: 수기 입력 제거
   - 동작: 팝빌 API로 실시간/주기적 수집

2. **AI Comment 초안 생성**
   - 목적: 과거 패턴 학습 → 자동 제안
   - 동작: LLM 기반 유사 거래 찾기

3. **배치 승인 UI**
   - 목적: Adhoc → 배치 처리로 전환
   - 동작: 매일/매주 정해진 시간에 Yes/No 클릭

4. **세무사 전달 포맷**
   - 목적: 세무사 재질문 제거
   - 동작: 엑셀/CSV export

---

## 4. Out of Scope (v1.1 이후)

- ❌ 주기적 지출 자동 챙김 - 이유: v1.0은 tracking에 집중
- ❌ 세무사 직접 연동 - 이유: 세무사 시스템 API 불확실
- ❌ 음성 입력 - 이유: 텍스트로 충분
- ❌ 모바일 앱 - 이유: 웹 먼저, 필요시 PWA

---

## 5. Expected Impact

**정량적**:
- 시간 절약: 새벽 1시까지 → **하루 10분**
- Context switching: 주 10회 → **주 1-2회**

**정성적**:
- 법적 리스크 걱정 감소
- 세무사 설명 부담 제거
- Big Fan 가능성: **HIGH**

---

## 6. Open Questions (Follow-up)

**질문 있음**: ✅

### 프로세스 관련
1. 세무사 커뮤니케이션 타이밍? (월말? 수시로?)
2. 입금 기록 방식? (나중에 모아서? 즉시?)
3. 어제 새벽 1시 작업 상세? (몇 건 처리?)

### 기술 환경 관련
4. 은행명?
5. 빠른조회 서비스 지원 여부?
6. 추가메시지 Export 가능?

### 비용/효과 검증
7. 현재 세무대행 비용?
8. 실제 소요 시간? (일/주/월 단위)

**답변 수합 필요 여부**:
- [x] 답변 수합 후 Ideation 업데이트 필요 (scope 영향 큼)
  - 특히 질문 4, 5번은 팝빌 API 사용 가능 여부 결정 (Critical)

---

## 7. Next Step

**현재 상태**:
- [x] Ideation 완료
- [ ] Follow-up 답변 대기 중
- [ ] Follow-up 답변 반영 후 MVP Proposal 작성

**Proposal 작성 준비도**: Waiting for answers (Q4, Q5 critical)

---

**JTBD Document**: [USER_001_2026-02-03.md](../User%20Interview/USER_001_2026-02-03.md)
**Last Updated**: 2026-02-04
```

---

## Integration with MVP Proposal

MVP Ideation 완료 후 MVP Proposal 작성 시:

1. **Section 1 (현재 상황)** ← Ideation Section 1 (Core Problem)
2. **Section 2 (해결 방법)** ← Ideation Section 2-3 (Core Idea + Key Features)
3. **Section 5 (제외 항목)** ← Ideation Section 4 (Out of Scope)
4. **Section 8 (미확인 사항)** ← Ideation Section 6 (Open Questions)

MVP Ideation을 빠르게 작성하고, 상세 내용은 MVP Proposal에서 보완합니다.
