# Weekly Picks Outreach 기능 정의서 (Feature Specification)

## 문서 개요

이 문서는 Proact의 Weekly Picks Outreach 시스템의 기능을 정의합니다.

**Related Documents**:
- PRD 문서: [weekly-picks-outreach-prd.md](./weekly-picks-outreach-prd.md)
- 상세 정책서: [weekly-picks-outreach-detailed-policy.md](./weekly-picks-outreach-detailed-policy.md)

---

## US-001: 파이프라인 실행 - 2-Stage 매칭 시스템

### 사용자 스토리

운영자로서, Weekly Picks가 업데이트된 후 매칭 파이프라인을 실행하여, 각 기업에 맞는 Top 5 공고와 Why Relevant 설명을 자동 생성하고 싶습니다.

### Acceptance Criteria

#### AC-001-01: 파이프라인 트리거

- 운영자가 CLI 명령어 또는 스케줄러를 통해 파이프라인 실행
- **자동 데이터 로딩**:
  - **Weekly Picks**: OpenSearch에서 해당 주차 공고 ID 목록 자동 조회
  - **컨택리스트**: Google Spreadsheet에서 대상 기업 정보 자동 불러오기

- 입력 파라미터:

| 파라미터 | 타입 | 필수 여부 | 설명 | 예시 |
|----------|------|-----------|------|------|
| weekly_picks_date | String | 필수 | 대상 Weekly Picks 날짜 | "2026-01-20" |
| spreadsheet_id | String | 선택 | Google Spreadsheet ID (기본값 사용 시 생략) | "1ABC...xyz" |
| company_limit | Number | 선택 | 처리할 기업 수 제한 (테스트용) | 1000 |
| embedding_base | String | 선택 | Embedding 베이스 (keyword/description) | "description" |
| top_n | Number | 선택 | Stage 1에서 추출할 Top N 수 | 20 |
| dry_run | Boolean | 선택 | 실제 저장 없이 테스트 실행 | false |

- 실행 시 파이프라인 ID 반환 (추적용)

#### AC-001-02: Stage 1 - Embedding 생성 및 유사도 계산

- **Company Embedding**:
  - Company_Summary + Business_Portfolio 텍스트 concat
  - OpenAI text-embedding-3-small 사용
  - 결과를 벡터 DB에 저장 (이미 존재하면 재사용)

- **공고 Embedding**:
  - embedding_base 파라미터에 따라:
    - "keyword": Top 10 Keywords 사용
    - "description": Description (Background + Scope of Work) 사용
  - Weekly Picks 전체에 대해 생성

- **유사도 계산**:
  - 각 기업에 대해 모든 공고와 cosine similarity 계산
  - Top N 공고 추출 (유사도 내림차순)

- **진행률 표시**:
  ```
  [Stage 1] Embedding 생성 중...
  - Company Embedding: 45,000 / 60,000 (75%)
  - 공고 Embedding: 2,000 / 2,000 (100%)
  - 유사도 계산: 30,000 / 60,000 (50%)
  예상 완료: 2시간 30분
  ```

#### AC-001-03: Stage 2 - LLM 검증 및 Why Relevant 생성

- **입력**: 각 기업의 Top N 공고 후보
- **LLM 호출 내용**:
  ```
  Company: {Company_Name}
  Summary: {Company_Summary}
  Portfolio: {Business_Portfolio}

  후보 공고 {N}개:
  1. {Title_1} - {Description_1}
  2. {Title_2} - {Description_2}
  ...

  Task:
  1. 각 공고가 이 기업과 관련있는지 판단 (Yes/No, Confidence 0-100)
  2. 관련있는 공고에 대해 "왜 관련있는지" 2-3문장으로 설명
  3. 최종 Top 5 선정 (Confidence 높은 순)
  ```

- **출력 형식**:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| opportunity_id | String | 공고 ID | "opp_12345" |
| is_relevant | Boolean | 관련성 판단 | true |
| confidence | Number | 확신도 (0-100) | 85 |
| why_relevant | String | 관련성 설명 | "귀사의 Cloud Migration 경험이..." |
| rank | Number | 최종 순위 (1-5) | 1 |

- **진행률 표시**:
  ```
  [Stage 2] LLM 검증 중...
  - 처리 완료: 30,000 / 60,000 기업 (50%)
  - LLM 호출 수: 150,000
  - 예상 비용: $180
  예상 완료: 4시간
  ```

#### AC-001-04: 결과 저장

- 기업별 최종 결과 저장:

| 필드 | 타입 | 설명 |
|------|------|------|
| company_id | String | 기업 ID |
| pipeline_id | String | 파이프라인 실행 ID |
| weekly_picks_date | String | 대상 주차 |
| matched_opportunities | Array | Top 5 공고 배열 |
| created_at | DateTime | 생성 시간 (UTC) |

- matched_opportunities 배열 구조:

| 필드 | 타입 | 설명 | 예시 |
|------|------|------|------|
| opportunity_id | String | 공고 ID | "opp_12345" |
| opportunity_title | String | 공고 제목 | "Cloud Services..." |
| agency_name | String | 발주 기관 | "Department of Defense" |
| due_date | String | 마감일 | "2026-02-15" |
| why_relevant | String | 관련성 설명 | "귀사의 경험이..." |
| confidence | Number | 확신도 | 85 |
| rank | Number | 순위 | 1 |

#### AC-001-05: 예외 처리

- **매칭 실패 (Top 5 미달)**:
  - 조건: confidence 50 이상인 공고가 5개 미만
  - 처리: 해당 기업은 발송 대상에서 제외
  - 로깅: `matching_failed` 상태로 기록

- **LLM 호출 실패**:
  - 조건: API 오류 또는 timeout
  - 처리: 최대 3회 재시도, 실패 시 해당 기업 스킵
  - 로깅: `llm_error` 상태로 기록

- **데이터 불완전**:
  - 조건: Company_Summary 50자 미만
  - 처리: Stage 1 시작 전 필터링, 발송 대상 제외
  - 로깅: `insufficient_data` 상태로 기록

---

## US-002: 품질 검증 - 매칭 결과 확인

### 사용자 스토리

운영자로서, 파이프라인 완료 후 매칭 결과를 샘플링하여 확인하고, 발송 전 품질을 검증하고 싶습니다.

### Acceptance Criteria

#### AC-002-01: 샘플 추출

- 조건: 파이프라인 완료 후 실행 가능
- 샘플링 옵션:

| 옵션 | 설명 |
|------|------|
| random | 전체 중 랜덤 N개 추출 |
| by_naics | NAICS 코드별 균등 추출 |
| by_confidence | confidence 분포별 추출 (상/중/하) |
| manual | 특정 company_id 지정 |

- 기본값: random 100개

#### AC-002-02: 매칭 결과 조회

- 각 샘플에 대해 표시할 정보:

**Company 정보:**
| 필드 | 표시 내용 |
|------|-----------|
| company_name | 기업명 |
| company_summary | 비즈니스 요약 (처음 200자) |
| primary_naics | 주요 NAICS 코드 및 설명 |

**매칭된 공고 (Top 5):**
| 필드 | 표시 내용 |
|------|-----------|
| rank | 순위 (1-5) |
| opportunity_title | 공고 제목 |
| agency_name | 발주 기관 |
| why_relevant | 관련성 설명 |
| confidence | 확신도 (%) |

#### AC-002-03: 수동 평가 기록

- 운영자가 각 매칭에 대해 평가 입력:

| 필드 | 타입 | 옵션 |
|------|------|------|
| quality_rating | Enum | good / acceptable / poor |
| comment | String (선택) | 자유 코멘트 |

- 평가 결과 집계:
  ```
  샘플 100개 평가 완료
  - Good: 65개 (65%)
  - Acceptable: 25개 (25%)
  - Poor: 10개 (10%)
  ```

#### AC-002-04: LLM-as-Judge 자동 평가

- 수동 평가 대신 LLM으로 자동 평가 옵션:
  ```
  Company: {Company_Name}
  Summary: {Company_Summary}

  매칭된 공고: {Opportunity_Title}
  Why Relevant: {Why_Relevant}

  이 매칭이 적절한가요?
  - 1: 전혀 관련없음
  - 2: 약간 관련있음
  - 3: 관련있음
  - 4: 매우 관련있음
  - 5: 완벽하게 매칭
  ```

- 자동 평가 결과 표시:
  - 평균 점수, 분포, 점수별 예시

#### AC-002-05: 이메일 프리뷰

- 실제 발송될 이메일 형태로 렌더링
- 표시 요소:
  - 제목 (Subject)
  - 본문 (HTML 렌더링)
  - 텍스트 버전
- 프리뷰에서 확인할 수 있는 항목:
  - 개인화 변수 치환 정상 여부
  - Why Relevant 문구의 자연스러움
  - CTA 버튼 링크 정상 여부

---

## US-003: 이메일 발송 - 대량 메일 전송

> ⚠️ **OUT OF SCOPE**: 기존 이메일 발송 시스템 활용. 본 기능은 별도 구현하지 않습니다.
> 파이프라인에서 생성된 매칭 결과를 기존 대량 이메일 발송 시스템에서 활용합니다.

### 사용자 스토리

운영자로서, 품질 검증을 통과한 매칭 결과를 기반으로 개인화된 이메일을 대량 발송하고 싶습니다.

### Acceptance Criteria

#### AC-003-01: 발송 대상 확정

- 발송 가능 조건:
  - 파이프라인 상태: completed
  - matched_opportunities: 5개 보유
  - company_email: 유효한 이메일
  - unsubscribed: false

- 발송 대상 집계:
  ```
  전체 기업: 60,000
  - 매칭 성공: 55,000
  - 데이터 불완전 제외: 3,000
  - 이전 반송 제외: 1,500
  - 구독 취소 제외: 500

  최종 발송 대상: 55,000
  ```

#### AC-003-02: 이메일 템플릿

- 템플릿 변수:

| 변수 | 설명 | 예시 |
|------|------|------|
| {first_name} | 수신자 이름 | "John" |
| {company_name} | 기업명 | "TechCorp Inc." |
| {opportunity_1_title} | 1번 공고 제목 | "Cloud Services..." |
| {opportunity_1_agency} | 1번 공고 기관 | "DoD" |
| {opportunity_1_due_date} | 1번 공고 마감일 | "Feb 15, 2026" |
| {opportunity_1_why} | 1번 공고 Why Relevant | "귀사의 경험이..." |
| ... | (2-5번 동일 구조) | ... |
| {cta_url} | CTA 링크 (트래킹 포함) | "https://..." |
| {unsubscribe_url} | 구독 취소 링크 | "https://..." |

- 발신자 설정:
  - From Name: "Proact Team" 또는 개인 이름 (A/B 테스트용)
  - From Email: outreach@proact.ai (또는 커스텀)
  - Reply-To: support@proact.ai

#### AC-003-03: 발송 실행

- 발송 옵션:

| 옵션 | 타입 | 설명 | 기본값 |
|------|------|------|--------|
| batch_size | Number | 배치당 발송 수 | 1000 |
| delay_between_batches | Number | 배치 간 딜레이 (초) | 60 |
| start_time | DateTime | 발송 시작 시간 | 즉시 |
| test_mode | Boolean | 테스트 발송 (내부 이메일만) | false |

- 발송 진행률:
  ```
  [발송 중] 35,000 / 55,000 (63%)
  - 성공: 34,800
  - 실패: 200
  - 예상 완료: 1시간 20분
  ```

#### AC-003-04: 반송 처리

- Hard Bounce (영구 실패):
  - 조건: 이메일 주소 없음, 도메인 없음
  - 처리: company.email_status = 'hard_bounce' 업데이트
  - 향후 발송 제외

- Soft Bounce (일시적 실패):
  - 조건: 메일함 가득 참, 서버 일시 오류
  - 처리: bounce_count += 1
  - 3회 연속 soft bounce 시 hard_bounce로 전환

#### AC-003-05: CAN-SPAM 준수

- 필수 포함 요소:
  - 발신자 명확히 표시
  - 물리적 주소 (Footer)
  - 구독 취소 링크 (1-click unsubscribe)
  - 10일 이내 구독 취소 처리

---

## US-004: 성과 추적 - 이메일 분석

> ⚠️ **OUT OF SCOPE**: 기존 이메일 발송 시스템 활용. 본 기능은 별도 구현하지 않습니다.
> 성과 추적은 기존 이메일 발송 시스템의 분석 기능을 활용합니다.

### 사용자 스토리

운영자로서, 발송된 이메일의 성과를 실시간으로 추적하고, 세그먼트별 분석을 통해 최적화 인사이트를 얻고 싶습니다.

### Acceptance Criteria

#### AC-004-01: 실시간 지표 대시보드

- 표시 지표:

| 지표 | 계산 방법 | 목표 |
|------|-----------|------|
| Delivered | 발송 - 반송 | 98%+ |
| Open Rate | 오픈 / Delivered | 40%+ |
| Click Rate | 클릭 / Delivered | 10%+ |
| Click-to-Open | 클릭 / 오픈 | 25%+ |
| Unsubscribe Rate | 구독취소 / Delivered | 1% 이하 |
| Bounce Rate | 반송 / 발송 | 2% 이하 |

- 시간별 추이 그래프:
  - 발송 후 1시간 / 6시간 / 24시간 / 48시간 / 7일

#### AC-004-02: 전환 추적

- UTM 파라미터 설정:
  ```
  utm_source=outreach
  utm_medium=email
  utm_campaign=weekly_picks_{date}
  utm_content={company_id}
  ```

- 추적 이벤트:
  - Landing Page 방문
  - 회원가입 시작
  - 회원가입 완료
  - (장기) 유료 전환

- 전환 퍼널:
  ```
  발송: 55,000
  └─ 오픈: 22,000 (40%)
     └─ 클릭: 5,500 (10%)
        └─ 가입시작: 550 (1%)
           └─ 가입완료: 275 (0.5%)
  ```

#### AC-004-03: 세그먼트별 분석

- 분석 가능 세그먼트:

| 세그먼트 | 분석 목적 |
|----------|-----------|
| NAICS 코드 | 어떤 산업군이 반응 좋은가 |
| 기업 규모 (추정) | 소기업 vs 중견기업 반응 차이 |
| Embedding 방식 | Keyword vs Description 성과 비교 |
| Confidence 수준 | 높은 confidence 매칭이 더 효과적인가 |
| 지역 (State) | 지역별 반응 차이 |

- 세그먼트별 지표 비교 테이블:
  ```
  NAICS별 성과:
  | NAICS | 발송 | 오픈율 | 클릭율 | 전환율 |
  |-------|------|--------|--------|--------|
  | 541512 | 5,000 | 45% | 12% | 0.8% |
  | 541519 | 3,000 | 38% | 9% | 0.5% |
  ```

#### AC-004-04: A/B 테스트 결과

- 테스트 가능 변수:
  - 제목 (Subject line)
  - 발신자 이름
  - CTA 문구
  - 발송 시간대
  - Embedding 방식 (Keyword vs Description)

- 통계적 유의성 표시:
  - 샘플 크기
  - p-value
  - 승리 변형 및 개선율

#### AC-004-05: 리포트 생성

- 주간 Outreach 리포트 자동 생성:
  - 발송 요약
  - 핵심 지표
  - 세그먼트 인사이트
  - 다음 주 권장 사항

- 내보내기 형식: PDF, CSV, Google Sheets 연동

---

## US-005: 데이터 관리 - 컨택리스트 관리

> ⚠️ **OUT OF SCOPE (부분)**: 이메일 발송 상태 관리 (구독 취소, 반송 처리 등)는 기존 이메일 발송 시스템 활용.
> 본 스펙에서는 **컨택리스트 소스 로딩 (AC-005-00)** 만 구현합니다.

### 사용자 스토리

운영자로서, 컨택리스트의 상태를 관리하고, 품질을 유지하여 지속적인 Outreach가 가능하도록 하고 싶습니다.

### Acceptance Criteria

#### AC-005-00: 컨택리스트 소스 - Google Spreadsheet

- **데이터 소스**: Google Spreadsheet (60k+ 기업 컨택 정보)
- **자동 로딩**: 파이프라인 시작 시 Spreadsheet에서 자동으로 데이터 불러오기
- **필수 컬럼**:

| 컬럼명 | 설명 | 필수 |
|--------|------|------|
| Email | 컨택 이메일 주소 | Yes |
| First_Name | 담당자 이름 | Yes |
| Company_Name | 기업명 | Yes |
| Primary_NAICS_Code | 주요 NAICS 코드 | No |
| Primary_NAICS_Description | NAICS 설명 | No |
| State | 주 (지역) | No |
| Set_Aside_Status | Set-Aside 상태 | No |
| Registration_Year | SAM 등록 연도 | No |
| Company_Summary | 기업 요약 | Yes |
| Company_Business_Portfolio | 비즈니스 포트폴리오 | No |
| Company_Reference | 참고 정보 | No |

- **Spreadsheet 설정**: 환경 변수 `OUTREACH_GOOGLE_SPREADSHEET_ID`로 기본 Spreadsheet ID 지정

#### AC-005-01: 컨택 상태 관리

- 컨택 상태 Enum:

| 상태 | 설명 | 발송 가능 |
|------|------|-----------|
| active | 활성 상태 | Yes |
| unsubscribed | 구독 취소 | No |
| hard_bounce | 영구 반송 | No |
| soft_bounce | 일시 반송 (3회 미만) | Yes |
| insufficient_data | 데이터 불완전 | No |
| recently_contacted | 최근 발송 (N일 이내) | 설정에 따라 |

#### AC-005-02: 구독 취소 처리

- 구독 취소 링크 클릭 시:
  - 즉시 상태 변경: status = 'unsubscribed'
  - 확인 페이지 표시: "구독이 취소되었습니다"
  - 향후 모든 발송에서 제외

- 재구독 옵션:
  - 구독 취소 후에도 재구독 가능하도록 옵션 제공
  - 단, 적극적 동의 필요

#### AC-005-03: 발송 이력 관리

- 각 컨택별 발송 이력:

| 필드 | 타입 | 설명 |
|------|------|------|
| company_id | String | 기업 ID |
| sent_at | DateTime | 발송 시간 |
| pipeline_id | String | 파이프라인 ID |
| opened | Boolean | 오픈 여부 |
| clicked | Boolean | 클릭 여부 |
| converted | Boolean | 전환 여부 |

- 발송 빈도 제어:
  - 기본: 주 1회 이하
  - 설정 가능: contact_frequency_days = 7

#### AC-005-04: 데이터 보강 대상 관리

- insufficient_data 상태 컨택 목록 조회
- 보강 필요 필드 표시:
  - Company_Summary 누락/부족
  - Business_Portfolio 누락/부족
- 외부 데이터 소스 연동 옵션 (향후)

---

## 데이터 구조 종합

### Pipeline Run

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| pipeline_id | String | 파이프라인 실행 ID | "pipe_20260120_001" |
| weekly_picks_date | String | 대상 주차 | "2026-01-20" |
| status | Enum | 상태 | running / completed / failed |
| embedding_base | String | 사용된 Embedding 방식 | "description" |
| top_n | Number | Stage 1 Top N 설정 | 20 |
| total_companies | Number | 전체 대상 기업 수 | 60000 |
| matched_companies | Number | 매칭 성공 기업 수 | 55000 |
| failed_companies | Number | 매칭 실패 기업 수 | 5000 |
| llm_calls | Number | LLM 호출 수 | 1100000 |
| estimated_cost | Number | 예상 비용 ($) | 180.50 |
| started_at | DateTime | 시작 시간 | "2026-01-20T08:00:00Z" |
| completed_at | DateTime | 완료 시간 | "2026-01-20T14:30:00Z" |

### Company Match Result

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| result_id | String | 결과 ID | "res_12345" |
| company_id | String | 기업 ID | "comp_67890" |
| pipeline_id | String | 파이프라인 ID | "pipe_20260120_001" |
| status | Enum | 매칭 상태 | success / failed |
| matched_opportunities | Array | 매칭된 공고 배열 | [MatchedOpportunity] |
| failure_reason | String | 실패 사유 (실패 시) | "insufficient_confidence" |
| created_at | DateTime | 생성 시간 | "2026-01-20T10:15:00Z" |

### Matched Opportunity

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| opportunity_id | String | 공고 ID | "opp_11111" |
| opportunity_title | String | 공고 제목 | "Cloud Services Support" |
| agency_name | String | 발주 기관 | "Department of Defense" |
| due_date | String | 마감일 | "2026-02-15" |
| why_relevant | String | 관련성 설명 | "귀사의 AWS 경험이..." |
| confidence | Number | 확신도 (0-100) | 87 |
| rank | Number | 순위 (1-5) | 1 |
| embedding_score | Number | Embedding 유사도 | 0.82 |

### Email Send Record

| 필드명 | 타입 | 설명 | 예시 |
|--------|------|------|------|
| send_id | String | 발송 ID | "send_99999" |
| company_id | String | 기업 ID | "comp_67890" |
| pipeline_id | String | 파이프라인 ID | "pipe_20260120_001" |
| email | String | 수신 이메일 | "john@techcorp.com" |
| sent_at | DateTime | 발송 시간 | "2026-01-21T09:00:00Z" |
| status | Enum | 발송 상태 | sent / bounced / failed |
| opened | Boolean | 오픈 여부 | true |
| opened_at | DateTime | 오픈 시간 | "2026-01-21T10:30:00Z" |
| clicked | Boolean | 클릭 여부 | true |
| clicked_at | DateTime | 클릭 시간 | "2026-01-21T10:32:00Z" |
| unsubscribed | Boolean | 구독 취소 여부 | false |

---

## API 명세

### 파이프라인 실행

**Endpoint**: `POST /api/v1/outreach/pipeline`

**Request**:
```json
{
  "weekly_picks_date": "2026-01-20",
  "company_limit": 1000,
  "embedding_base": "description",
  "top_n": 20,
  "dry_run": false
}
```

**Response**:
```json
{
  "pipeline_id": "pipe_20260120_001",
  "status": "running",
  "estimated_duration_minutes": 360,
  "estimated_cost": 180.50
}
```

### 파이프라인 상태 조회

**Endpoint**: `GET /api/v1/outreach/pipeline/{pipeline_id}`

**Response**:
```json
{
  "pipeline_id": "pipe_20260120_001",
  "status": "running",
  "progress": {
    "stage1_embedding": { "completed": 45000, "total": 60000 },
    "stage2_llm": { "completed": 20000, "total": 60000 }
  },
  "metrics": {
    "llm_calls": 400000,
    "current_cost": 65.20
  },
  "estimated_completion": "2026-01-20T14:30:00Z"
}
```

### 샘플 매칭 결과 조회

**Endpoint**: `GET /api/v1/outreach/pipeline/{pipeline_id}/samples`

**Query Parameters**:
- `sampling_method`: random | by_naics | by_confidence
- `count`: 샘플 수 (기본 100)

**Response**:
```json
{
  "samples": [
    {
      "company": {
        "company_id": "comp_67890",
        "company_name": "TechCorp Inc.",
        "company_summary": "Cloud computing...",
        "primary_naics": "541512"
      },
      "matched_opportunities": [
        {
          "rank": 1,
          "opportunity_title": "Cloud Services...",
          "why_relevant": "귀사의 AWS 경험이...",
          "confidence": 87
        }
      ]
    }
  ]
}
```

### 이메일 발송 실행

**Endpoint**: `POST /api/v1/outreach/pipeline/{pipeline_id}/send`

**Request**:
```json
{
  "batch_size": 1000,
  "delay_between_batches": 60,
  "start_time": "2026-01-21T09:00:00Z",
  "test_mode": false
}
```

**Response**:
```json
{
  "send_job_id": "job_12345",
  "status": "scheduled",
  "total_recipients": 55000,
  "scheduled_start": "2026-01-21T09:00:00Z"
}
```

### 성과 지표 조회

**Endpoint**: `GET /api/v1/outreach/pipeline/{pipeline_id}/metrics`

**Response**:
```json
{
  "pipeline_id": "pipe_20260120_001",
  "send_metrics": {
    "total_sent": 55000,
    "delivered": 53900,
    "bounced": 1100,
    "delivery_rate": 0.98
  },
  "engagement_metrics": {
    "opened": 21560,
    "open_rate": 0.40,
    "clicked": 5390,
    "click_rate": 0.10,
    "click_to_open_rate": 0.25
  },
  "conversion_metrics": {
    "landing_visits": 5390,
    "signups_started": 539,
    "signups_completed": 269,
    "conversion_rate": 0.005
  },
  "health_metrics": {
    "unsubscribed": 270,
    "unsubscribe_rate": 0.005,
    "spam_complaints": 5,
    "spam_rate": 0.0001
  }
}
```

---

## 에러 처리

### LLM API 오류

- **조건**: OpenAI API 호출 실패 (rate limit, timeout 등)
- **처리**:
  - 자동 재시도 (exponential backoff, 최대 3회)
  - 재시도 실패 시 해당 기업 스킵, 로깅
- **메시지**: "LLM 호출 실패: {company_id}, 원인: {error_message}"

### 이메일 발송 오류

- **조건**: SendGrid/SES API 오류
- **처리**:
  - 배치 단위 재시도
  - 특정 이메일만 실패 시 해당 건만 재시도 큐에 추가
- **메시지**: "이메일 발송 실패: {email}, 원인: {error_message}"

### 데이터 정합성 오류

- **조건**: 참조하는 공고가 DB에 없음
- **처리**: 해당 공고 제외, 차순위로 대체
- **메시지**: "공고 데이터 누락: {opportunity_id}"

---

## 성능 요구사항

- **Stage 1 (Embedding)**: 60k 기업 처리 - 2시간 이내
- **Stage 2 (LLM)**: 60k × Top 20 = 1.2M 호출 - 6시간 이내
- **이메일 발송**: 55k건 - 2시간 이내 (배치 처리)
- **전체 파이프라인**: Weekly Picks 업데이트 후 24시간 이내 발송 완료

---

## 보안 요구사항

- **API 키 관리**: OpenAI, SendGrid API 키는 환경 변수로 관리
- **이메일 데이터**: PII로 취급, 로그에 마스킹
- **구독 취소 링크**: 추측 불가능한 토큰 사용
- **발송 권한**: 운영자 인증 필수

---

## 향후 개선 사항

1. **Algorithm A 지원**: 공고당 Top 100 기업 매칭 파이프라인 추가
2. **Teaming 파트너 연결**: 공고별 경험자 매칭 및 소개 기능
3. **자동 A/B 테스트**: 제목, CTA 등 자동 변형 및 최적화
4. **뉴스레터 구독 전환**: 일회성 Outreach → 구독자 풀 구축
5. **실시간 대시보드**: 발송 후 성과 실시간 모니터링 UI
