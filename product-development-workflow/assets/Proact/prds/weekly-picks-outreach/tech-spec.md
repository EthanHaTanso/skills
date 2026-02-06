# Weekly Picks Outreach 기술 스펙 (Technical Specification)

**Last Updated**: 2026년 1월 22일
**Related Documents**:
- PRD 문서: [weekly-picks-outreach-prd.md](./weekly-picks-outreach-prd.md)
- 기능정의서: [weekly-picks-outreach-feature-spec.md](./weekly-picks-outreach-feature-spec.md)

---

## 1. Technical Overview

### 1.1. Feature Summary

Weekly Picks Outreach는 60k+ 외부 기업 컨택리스트에 대해 매주 개인화된 공고 추천 이메일을 자동 발송하는 시스템이다. 2-Stage 매칭 파이프라인(Embedding → LLM 검증)을 통해 각 기업에 맞는 Top 5 공고와 "Why Relevant" 설명을 생성한다.

### 1.2. System Architecture

> ⚠️ **구현 범위 참고**: 이메일 발송 (Delivery) 단계는 기존 이메일 발송 시스템 활용으로 **Out of Scope**.
> 본 시스템은 **Stage 1 (Embedding) + Stage 2 (LLM 검증)** 매칭 파이프라인과 결과 내보내기에 집중합니다.

```
┌─────────────────────────────────────────────────────────────────────┐
│                  Weekly Picks Outreach Pipeline                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐           │
│  │  Data Load   │───▶│   Stage 1    │───▶│   Stage 2    │           │
│  │  (Contacts)  │    │  Embedding   │    │ LLM Verify   │           │
│  └──────────────┘    └──────────────┘    └──────────────┘           │
│         │                   │                   │                    │
│         ▼                   ▼                   ▼                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐           │
│  │   Google     │    │  OpenSearch  │    │   OpenAI     │           │
│  │ Spreadsheet  │    │  (Vector DB) │    │   (LLM)      │           │
│  │  or CSV/XLSX │    └──────────────┘    └──────────────┘           │
│  └──────────────┘                                                   │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │                       MySQL                               │       │
│  │  - outreach_pipeline_run                                  │       │
│  │  - outreach_company_match                                 │       │
│  │  - outreach_matched_opportunity                           │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │                 Export (결과 내보내기)                     │       │
│  │  - CSV/JSON 파일 출력                                     │       │
│  │  - 기존 이메일 발송 시스템에서 활용                         │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.3. Dependencies

**기존 코드/컴포넌트:**
- `src/core/database.py` - MySQLClient, get_opensearch_client()
- `src/core/llm_openai.py` - OpenAI LLM 호출
- `src/services/keyword_vectorizer.py` - Embedding 생성 (재사용)
- `src/services/search_service.py` - OpenSearch 검색 (확장)
- `src/services/email_service.py` - 이메일 발송 로직 (참조)
- `src/utils/logging.py` - get_logger()
- `src/utils/normalization.py` - normalize 함수들

### 1.4. New Components

| 컴포넌트 | 위치 | 설명 |
|----------|------|------|
| OutreachPipelineService | `src/services/outreach_pipeline_service.py` | 파이프라인 오케스트레이션 |
| OutreachMatchingService | `src/services/outreach_matching_service.py` | 2-Stage 매칭 로직 |
| OutreachContactLoaderService | `src/services/outreach_contact_loader_service.py` | 컨택리스트 로딩 (Google Sheets / CSV / XLSX) |
| outreach schemas | `src/schemas/outreach.py` | Pydantic 모델 정의 |
| outreach API | `src/api/outreach.py` | FastAPI 라우터 |
| run_outreach CLI | `scripts/run_outreach_pipeline.py` | CLI 스크립트 |

> ⚠️ **Out of Scope**: `OutreachDeliveryService` (이메일 발송) - 기존 이메일 발송 시스템 활용

---

## 2. Database Schema

### 2.1. 신규 테이블

#### outreach_pipeline_run
```sql
CREATE TABLE outreach_pipeline_run (
    pipeline_id VARCHAR(64) PRIMARY KEY,
    weekly_picks_date DATE NOT NULL,
    status ENUM('pending', 'stage1_running', 'stage2_running', 'completed', 'failed') NOT NULL DEFAULT 'pending',
    embedding_base ENUM('keyword', 'description') NOT NULL DEFAULT 'description',
    top_n INT NOT NULL DEFAULT 20,
    total_companies INT DEFAULT 0,
    matched_companies INT DEFAULT 0,
    failed_companies INT DEFAULT 0,
    llm_calls INT DEFAULT 0,
    estimated_cost_usd DECIMAL(10, 4) DEFAULT 0,
    error_message TEXT,
    started_at DATETIME(6),
    stage1_completed_at DATETIME(6),
    stage2_completed_at DATETIME(6),
    completed_at DATETIME(6),
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),

    INDEX idx_weekly_picks_date (weekly_picks_date),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
);
```

#### outreach_company_match
```sql
CREATE TABLE outreach_company_match (
    match_id VARCHAR(64) PRIMARY KEY,
    pipeline_id VARCHAR(64) NOT NULL,
    company_id VARCHAR(64) NOT NULL,
    status ENUM('success', 'failed', 'insufficient_data', 'insufficient_confidence') NOT NULL,
    failure_reason VARCHAR(255),
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),

    INDEX idx_pipeline_id (pipeline_id),
    INDEX idx_company_id (company_id),
    INDEX idx_status (status),
    FOREIGN KEY (pipeline_id) REFERENCES outreach_pipeline_run(pipeline_id) ON DELETE CASCADE
);
```

#### outreach_matched_opportunity
```sql
CREATE TABLE outreach_matched_opportunity (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    match_id VARCHAR(64) NOT NULL,
    opportunity_id VARCHAR(64) NOT NULL,
    opportunity_title VARCHAR(500) NOT NULL,
    agency_name VARCHAR(255),
    due_date DATE,
    why_relevant TEXT NOT NULL,
    confidence INT NOT NULL,
    embedding_score DECIMAL(6, 4),
    rank INT NOT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),

    INDEX idx_match_id (match_id),
    INDEX idx_opportunity_id (opportunity_id),
    FOREIGN KEY (match_id) REFERENCES outreach_company_match(match_id) ON DELETE CASCADE
);
```

> ⚠️ **Out of Scope 테이블** (기존 이메일 발송 시스템 활용):
> - `outreach_email_send` - 이메일 발송 기록
> - `outreach_contact_list` - 컨택리스트 상태 관리 (구독 취소, 반송 등)
>
> 컨택리스트는 **Google Spreadsheet 또는 CSV/XLSX 파일**에서 직접 로딩하여 메모리에서 처리합니다.

---

## 3. Pydantic Schemas

### 3.1. src/schemas/outreach.py

```python
"""Weekly Picks Outreach 스키마 정의"""

from datetime import date, datetime
from decimal import Decimal
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field


# ============================================================
# Enums
# ============================================================

class PipelineStatus(StrEnum):
    """파이프라인 실행 상태"""
    PENDING = "pending"
    STAGE1_RUNNING = "stage1_running"
    STAGE2_RUNNING = "stage2_running"
    COMPLETED = "completed"
    FAILED = "failed"


class EmbeddingBase(StrEnum):
    """Embedding 베이스 옵션"""
    KEYWORD = "keyword"
    DESCRIPTION = "description"


class MatchStatus(StrEnum):
    """기업 매칭 상태"""
    SUCCESS = "success"
    FAILED = "failed"
    INSUFFICIENT_DATA = "insufficient_data"
    INSUFFICIENT_CONFIDENCE = "insufficient_confidence"


class ContactStatus(StrEnum):
    """컨택 상태"""
    ACTIVE = "active"
    UNSUBSCRIBED = "unsubscribed"
    HARD_BOUNCE = "hard_bounce"
    SOFT_BOUNCE = "soft_bounce"
    INSUFFICIENT_DATA = "insufficient_data"


class EmailSendStatus(StrEnum):
    """이메일 발송 상태"""
    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    BOUNCED = "bounced"
    FAILED = "failed"


class BounceType(StrEnum):
    """반송 유형"""
    HARD = "hard"
    SOFT = "soft"


class SamplingMethod(StrEnum):
    """샘플링 방법"""
    RANDOM = "random"
    BY_NAICS = "by_naics"
    BY_CONFIDENCE = "by_confidence"
    MANUAL = "manual"


class QualityRating(StrEnum):
    """품질 평가 등급"""
    GOOD = "good"
    ACCEPTABLE = "acceptable"
    POOR = "poor"


class ContactLoadSource(StrEnum):
    """컨택리스트 로딩 소스"""
    GOOGLE_SHEETS = "google_sheets"
    CSV_FILE = "csv_file"
    XLSX_FILE = "xlsx_file"


class ExportFormat(StrEnum):
    """결과 내보내기 형식"""
    CSV = "csv"
    JSON = "json"


# ============================================================
# Contact Info Model (컨택리스트 로딩)
# ============================================================

class ContactInfo(BaseModel):
    """컨택 정보 (Google Spreadsheet / CSV / XLSX에서 로딩)"""
    email: str = Field(..., description="컨택 이메일")
    first_name: str = Field(..., description="담당자 이름")
    company_name: str = Field(..., description="기업명")
    company_summary: str = Field(..., min_length=50, description="기업 요약 (최소 50자)")

    # Optional fields
    primary_naics_code: str | None = Field(default=None, description="주요 NAICS 코드")
    primary_naics_description: str | None = Field(default=None, description="NAICS 설명")
    state: str | None = Field(default=None, description="주 (지역)")
    set_aside_status: str | None = Field(default=None, description="Set-Aside 상태")
    registration_year: int | None = Field(default=None, description="SAM 등록 연도")
    company_business_portfolio: str | None = Field(default=None, description="비즈니스 포트폴리오")
    company_reference: str | None = Field(default=None, description="참고 정보")


# ============================================================
# Request Models
# ============================================================

class StartPipelineRequest(BaseModel):
    """파이프라인 시작 요청"""
    weekly_picks_date: date = Field(
        ...,
        description="대상 Weekly Picks 날짜 (월요일)"
    )

    # 컨택리스트 소스 설정
    contact_source: ContactLoadSource = Field(
        default=ContactLoadSource.GOOGLE_SHEETS,
        description="컨택리스트 소스 (google_sheets/csv_file/xlsx_file)"
    )
    spreadsheet_id: str | None = Field(
        default=None,
        description="Google Spreadsheet ID (기본값: 환경변수 OUTREACH_GOOGLE_SPREADSHEET_ID)"
    )
    contact_file_path: str | None = Field(
        default=None,
        description="CSV/XLSX 파일 경로 (contact_source가 csv_file 또는 xlsx_file일 때 필수)"
    )

    # 파이프라인 설정
    company_limit: int | None = Field(
        default=None,
        ge=1,
        le=100000,
        description="처리할 기업 수 제한 (테스트용)"
    )
    embedding_base: EmbeddingBase = Field(
        default=EmbeddingBase.DESCRIPTION,
        description="Embedding 베이스 (keyword/description)"
    )
    top_n: int = Field(
        default=20,
        ge=5,
        le=100,
        description="Stage 1에서 추출할 Top N 수"
    )
    dry_run: bool = Field(
        default=False,
        description="테스트 모드 (실제 저장 없이 실행)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "weekly_picks_date": "2026-01-20",
                "contact_source": "google_sheets",
                "spreadsheet_id": "1l9X6kVkjhmbWUFZOuREe-9sY1Rjwlfbre16yP-hyJkU",
                "company_limit": 1000,
                "embedding_base": "description",
                "top_n": 20,
                "dry_run": False
            }
        }


class SendEmailsRequest(BaseModel):
    """이메일 발송 요청"""
    batch_size: int = Field(
        default=1000,
        ge=100,
        le=5000,
        description="배치당 발송 수"
    )
    delay_between_batches_sec: int = Field(
        default=60,
        ge=10,
        le=300,
        description="배치 간 딜레이 (초)"
    )
    start_time: datetime | None = Field(
        default=None,
        description="발송 시작 시간 (None이면 즉시)"
    )
    test_mode: bool = Field(
        default=False,
        description="테스트 모드 (내부 이메일만)"
    )


class GetSamplesRequest(BaseModel):
    """샘플 조회 요청"""
    sampling_method: SamplingMethod = Field(
        default=SamplingMethod.RANDOM
    )
    count: int = Field(
        default=100,
        ge=10,
        le=500
    )
    naics_codes: list[str] | None = Field(
        default=None,
        description="특정 NAICS 코드로 필터 (by_naics 모드)"
    )
    company_ids: list[str] | None = Field(
        default=None,
        description="특정 company_id 지정 (manual 모드)"
    )


class SubmitQualityRatingRequest(BaseModel):
    """품질 평가 제출"""
    match_id: str
    rating: QualityRating
    comment: str | None = None


# ============================================================
# Response Models
# ============================================================

class PipelineProgress(BaseModel):
    """파이프라인 진행 상황"""
    stage: str = Field(description="현재 스테이지 (stage1/stage2/complete)")
    completed: int = Field(description="완료된 기업 수")
    total: int = Field(description="전체 기업 수")
    percentage: float = Field(description="진행률 (%)")


class PipelineMetrics(BaseModel):
    """파이프라인 메트릭"""
    llm_calls: int = Field(default=0)
    current_cost_usd: Decimal = Field(default=Decimal("0"))
    estimated_total_cost_usd: Decimal = Field(default=Decimal("0"))


class StartPipelineResponse(BaseModel):
    """파이프라인 시작 응답"""
    pipeline_id: str
    status: PipelineStatus
    estimated_duration_minutes: int | None = None
    estimated_cost_usd: Decimal | None = None


class PipelineStatusResponse(BaseModel):
    """파이프라인 상태 응답"""
    pipeline_id: str
    status: PipelineStatus
    weekly_picks_date: date
    embedding_base: EmbeddingBase
    top_n: int
    progress: PipelineProgress
    metrics: PipelineMetrics
    total_companies: int
    matched_companies: int
    failed_companies: int
    started_at: datetime | None = None
    estimated_completion: datetime | None = None
    completed_at: datetime | None = None
    error_message: str | None = None


class MatchedOpportunity(BaseModel):
    """매칭된 공고 정보"""
    opportunity_id: str
    opportunity_title: str
    agency_name: str | None = None
    due_date: date | None = None
    why_relevant: str
    confidence: int = Field(ge=0, le=100)
    embedding_score: Decimal | None = None
    rank: int = Field(ge=1, le=10)


class CompanyInfo(BaseModel):
    """기업 정보 (샘플 조회용)"""
    company_id: str
    company_name: str
    company_summary: str | None = None
    primary_naics_code: str | None = None
    primary_naics_description: str | None = None


class CompanyMatchSample(BaseModel):
    """기업 매칭 샘플"""
    company: CompanyInfo
    matched_opportunities: list[MatchedOpportunity]
    match_status: MatchStatus


class SamplesResponse(BaseModel):
    """샘플 조회 응답"""
    pipeline_id: str
    sampling_method: SamplingMethod
    count: int
    samples: list[CompanyMatchSample]


class EmailPreview(BaseModel):
    """이메일 프리뷰"""
    subject: str
    html_body: str
    text_body: str


class SendMetrics(BaseModel):
    """발송 메트릭"""
    total_sent: int = 0
    delivered: int = 0
    bounced: int = 0
    failed: int = 0
    delivery_rate: float = 0.0


class EngagementMetrics(BaseModel):
    """참여 메트릭"""
    opened: int = 0
    open_rate: float = 0.0
    clicked: int = 0
    click_rate: float = 0.0
    click_to_open_rate: float = 0.0


class ConversionMetrics(BaseModel):
    """전환 메트릭"""
    landing_visits: int = 0
    signups_started: int = 0
    signups_completed: int = 0
    conversion_rate: float = 0.0


class HealthMetrics(BaseModel):
    """건강 지표"""
    unsubscribed: int = 0
    unsubscribe_rate: float = 0.0
    spam_complaints: int = 0
    spam_rate: float = 0.0


class PipelineMetricsResponse(BaseModel):
    """파이프라인 성과 지표 응답"""
    pipeline_id: str
    send_metrics: SendMetrics
    engagement_metrics: EngagementMetrics
    conversion_metrics: ConversionMetrics
    health_metrics: HealthMetrics


class SendJobResponse(BaseModel):
    """이메일 발송 작업 응답"""
    send_job_id: str
    status: str
    total_recipients: int
    scheduled_start: datetime | None = None


# ============================================================
# Internal Models (Service Layer)
# ============================================================

class CompanyEmbeddingInput(BaseModel):
    """Embedding 생성용 기업 입력"""
    company_id: str
    text: str  # company_summary + business_portfolio


class OpportunityEmbeddingInput(BaseModel):
    """Embedding 생성용 공고 입력"""
    opportunity_id: str
    text: str  # keyword or description based on config


class LLMVerificationInput(BaseModel):
    """LLM 검증 입력"""
    company_id: str
    company_name: str
    company_summary: str
    business_portfolio: str | None
    candidate_opportunities: list[dict]  # Top N from Stage 1


class LLMVerificationOutput(BaseModel):
    """LLM 검증 출력"""
    verified_opportunities: list[MatchedOpportunity]
    rejected_count: int


class OutreachEmailContent(BaseModel):
    """Outreach 이메일 콘텐츠"""
    company_id: str
    first_name: str
    company_name: str
    email: str
    opportunities: list[MatchedOpportunity]
    cta_url: str
    unsubscribe_url: str
```

---

## 4. Service Specifications

### 4.0. OutreachContactLoaderService

**파일**: `src/services/outreach_contact_loader_service.py`

```python
"""컨택리스트 로딩 서비스 (Google Spreadsheet / CSV / XLSX)"""

from dataclasses import dataclass
from pathlib import Path
from typing import AsyncIterator

import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from src.schemas.outreach import ContactInfo, ContactLoadSource
from src.utils.logging import get_logger
from src.settings import get_settings

logger = get_logger(__name__)


@dataclass
class ContactLoadResult:
    """컨택리스트 로딩 결과"""
    total_loaded: int
    valid_contacts: int
    skipped_insufficient_data: int
    source: ContactLoadSource


class OutreachContactLoaderService:
    """컨택리스트 로딩 서비스

    지원하는 소스:
    1. Google Spreadsheet (기본) - API를 통한 자동 로딩
    2. CSV 파일 - 로컬 파일 업로드
    3. XLSX 파일 - 로컬 파일 업로드
    """

    # 기본 Google Spreadsheet ID
    DEFAULT_SPREADSHEET_ID = "1l9X6kVkjhmbWUFZOuREe-9sY1Rjwlfbre16yP-hyJkU"

    REQUIRED_COLUMNS = ["Email", "First_Name", "Company_Name", "Company_Summary"]
    OPTIONAL_COLUMNS = [
        "Primary_NAICS_Code",
        "Primary_NAICS_Description",
        "State",
        "Set_Aside_Status",
        "Registration_Year",
        "Company_Business_Portfolio",
        "Company_Reference",
    ]

    def __init__(self):
        self._settings = get_settings()

    async def load_from_google_sheets(
        self,
        spreadsheet_id: str | None = None,
        sheet_name: str = "Sheet1",
        limit: int | None = None,
    ) -> tuple[list[ContactInfo], ContactLoadResult]:
        """Google Spreadsheet에서 컨택리스트 로딩

        Args:
            spreadsheet_id: Spreadsheet ID (기본값: 환경변수 또는 DEFAULT_SPREADSHEET_ID)
            sheet_name: 시트 이름 (기본값: Sheet1)
            limit: 로딩할 최대 행 수 (테스트용)

        Returns:
            (contacts, result): 컨택 정보 리스트와 로딩 결과
        """
        spreadsheet_id = spreadsheet_id or self._settings.outreach_google_spreadsheet_id or self.DEFAULT_SPREADSHEET_ID

        logger.info(
            "Loading contacts from Google Spreadsheet",
            spreadsheet_id=spreadsheet_id,
            sheet_name=sheet_name,
            limit=limit,
        )

        try:
            # Google Sheets API 인증
            creds = self._get_google_credentials()
            service = build("sheets", "v4", credentials=creds)

            # 데이터 조회
            range_name = f"{sheet_name}!A:L"  # A부터 L까지 (12개 컬럼)
            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=range_name,
            ).execute()

            values = result.get("values", [])
            if not values:
                return [], ContactLoadResult(0, 0, 0, ContactLoadSource.GOOGLE_SHEETS)

            # DataFrame으로 변환
            df = pd.DataFrame(values[1:], columns=values[0])  # 첫 행은 헤더

            return self._process_dataframe(df, limit, ContactLoadSource.GOOGLE_SHEETS)

        except Exception as e:
            logger.error("Failed to load from Google Sheets", error=str(e), exc_info=True)
            raise

    async def load_from_csv(
        self,
        file_path: str | Path,
        limit: int | None = None,
    ) -> tuple[list[ContactInfo], ContactLoadResult]:
        """CSV 파일에서 컨택리스트 로딩"""
        logger.info("Loading contacts from CSV", file_path=str(file_path), limit=limit)

        df = pd.read_csv(file_path)
        return self._process_dataframe(df, limit, ContactLoadSource.CSV_FILE)

    async def load_from_xlsx(
        self,
        file_path: str | Path,
        sheet_name: str = "Sheet1",
        limit: int | None = None,
    ) -> tuple[list[ContactInfo], ContactLoadResult]:
        """XLSX 파일에서 컨택리스트 로딩"""
        logger.info(
            "Loading contacts from XLSX",
            file_path=str(file_path),
            sheet_name=sheet_name,
            limit=limit,
        )

        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return self._process_dataframe(df, limit, ContactLoadSource.XLSX_FILE)

    def _process_dataframe(
        self,
        df: pd.DataFrame,
        limit: int | None,
        source: ContactLoadSource,
    ) -> tuple[list[ContactInfo], ContactLoadResult]:
        """DataFrame을 ContactInfo 리스트로 변환"""
        # 필수 컬럼 검증
        missing_cols = [col for col in self.REQUIRED_COLUMNS if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # 제한 적용
        if limit:
            df = df.head(limit)

        total_loaded = len(df)
        contacts = []
        skipped = 0

        for _, row in df.iterrows():
            # Company_Summary 최소 길이 검증
            company_summary = str(row.get("Company_Summary", "")).strip()
            if len(company_summary) < 50:
                skipped += 1
                continue

            contact = ContactInfo(
                email=str(row["Email"]).strip(),
                first_name=str(row["First_Name"]).strip(),
                company_name=str(row["Company_Name"]).strip(),
                company_summary=company_summary,
                primary_naics_code=self._safe_str(row.get("Primary_NAICS_Code")),
                primary_naics_description=self._safe_str(row.get("Primary_NAICS_Description")),
                state=self._safe_str(row.get("State")),
                set_aside_status=self._safe_str(row.get("Set_Aside_Status")),
                registration_year=self._safe_int(row.get("Registration_Year")),
                company_business_portfolio=self._safe_str(row.get("Company_Business_Portfolio")),
                company_reference=self._safe_str(row.get("Company_Reference")),
            )
            contacts.append(contact)

        result = ContactLoadResult(
            total_loaded=total_loaded,
            valid_contacts=len(contacts),
            skipped_insufficient_data=skipped,
            source=source,
        )

        logger.info(
            "Contact loading completed",
            total_loaded=result.total_loaded,
            valid_contacts=result.valid_contacts,
            skipped=result.skipped_insufficient_data,
        )

        return contacts, result

    def _get_google_credentials(self) -> Credentials:
        """Google API 인증 정보 로드"""
        credentials_path = self._settings.google_service_account_path
        if not credentials_path:
            raise ValueError("GOOGLE_SERVICE_ACCOUNT_PATH not configured")

        return Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
        )

    @staticmethod
    def _safe_str(value) -> str | None:
        if pd.isna(value):
            return None
        return str(value).strip() or None

    @staticmethod
    def _safe_int(value) -> int | None:
        if pd.isna(value):
            return None
        try:
            return int(value)
        except (ValueError, TypeError):
            return None
```

---

### 4.1. OutreachPipelineService

**파일**: `src/services/outreach_pipeline_service.py`

```python
"""Outreach 파이프라인 오케스트레이션 서비스"""

from datetime import datetime, timezone
from decimal import Decimal
import uuid

from src.core.database import MySQLClient
from src.schemas.outreach import (
    StartPipelineRequest,
    StartPipelineResponse,
    PipelineStatusResponse,
    PipelineStatus,
    PipelineProgress,
    PipelineMetrics,
)
from src.services.outreach_matching_service import OutreachMatchingService
from src.utils.logging import get_logger

logger = get_logger(__name__)


class OutreachPipelineService:
    """파이프라인 전체 흐름을 관리하는 서비스"""

    def __init__(
        self,
        *,
        db: MySQLClient | None = None,
        matching_service: OutreachMatchingService | None = None,
    ):
        self.db = db or MySQLClient.get_instance()
        self._matching_service = matching_service or OutreachMatchingService()

    async def start_pipeline(
        self,
        request: StartPipelineRequest,
    ) -> StartPipelineResponse:
        """새 파이프라인 시작"""
        pipeline_id = f"pipe_{request.weekly_picks_date.strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}"

        # 파이프라인 레코드 생성
        await self._create_pipeline_record(pipeline_id, request)

        # 비용 예측
        estimated_cost = await self._estimate_cost(request)
        estimated_duration = await self._estimate_duration(request)

        logger.info(
            "Pipeline started",
            pipeline_id=pipeline_id,
            weekly_picks_date=str(request.weekly_picks_date),
            embedding_base=request.embedding_base,
        )

        return StartPipelineResponse(
            pipeline_id=pipeline_id,
            status=PipelineStatus.PENDING,
            estimated_duration_minutes=estimated_duration,
            estimated_cost_usd=estimated_cost,
        )

    async def run_pipeline(self, pipeline_id: str) -> None:
        """파이프라인 실행 (백그라운드 태스크)"""
        try:
            await self._update_status(pipeline_id, PipelineStatus.STAGE1_RUNNING)

            # Stage 1: Embedding 매칭
            stage1_result = await self._matching_service.run_stage1(pipeline_id)
            await self._update_stage1_complete(pipeline_id, stage1_result)

            await self._update_status(pipeline_id, PipelineStatus.STAGE2_RUNNING)

            # Stage 2: LLM 검증
            stage2_result = await self._matching_service.run_stage2(pipeline_id)
            await self._update_stage2_complete(pipeline_id, stage2_result)

            await self._update_status(pipeline_id, PipelineStatus.COMPLETED)

        except Exception as e:
            logger.error("Pipeline failed", pipeline_id=pipeline_id, error=str(e), exc_info=True)
            await self._update_status(pipeline_id, PipelineStatus.FAILED, error_message=str(e))
            raise

    async def get_pipeline_status(self, pipeline_id: str) -> PipelineStatusResponse:
        """파이프라인 상태 조회"""
        # DB에서 파이프라인 정보 조회
        pipeline = await self._get_pipeline_record(pipeline_id)

        # 진행 상황 계산
        progress = await self._calculate_progress(pipeline_id, pipeline["status"])

        # 메트릭 집계
        metrics = await self._aggregate_metrics(pipeline_id)

        return PipelineStatusResponse(
            pipeline_id=pipeline_id,
            status=PipelineStatus(pipeline["status"]),
            weekly_picks_date=pipeline["weekly_picks_date"],
            embedding_base=pipeline["embedding_base"],
            top_n=pipeline["top_n"],
            progress=progress,
            metrics=metrics,
            total_companies=pipeline["total_companies"],
            matched_companies=pipeline["matched_companies"],
            failed_companies=pipeline["failed_companies"],
            started_at=pipeline["started_at"],
            completed_at=pipeline["completed_at"],
            error_message=pipeline.get("error_message"),
        )

    async def _estimate_cost(self, request: StartPipelineRequest) -> Decimal:
        """비용 예측"""
        company_count = request.company_limit or 60000
        llm_calls = company_count * request.top_n
        # GPT-4o-mini 기준 대략적 비용
        cost_per_1k_calls = Decimal("0.15")
        return (Decimal(llm_calls) / 1000) * cost_per_1k_calls

    async def _estimate_duration(self, request: StartPipelineRequest) -> int:
        """소요 시간 예측 (분)"""
        company_count = request.company_limit or 60000
        # Stage 1: ~1분/1000기업, Stage 2: ~5분/1000기업
        stage1_min = company_count // 1000
        stage2_min = (company_count * 5) // 1000
        return stage1_min + stage2_min
```

### 4.2. OutreachMatchingService

**파일**: `src/services/outreach_matching_service.py`

```python
"""Outreach 매칭 서비스 (2-Stage Pipeline)"""

from dataclasses import dataclass
from decimal import Decimal

from src.core.database import MySQLClient, get_opensearch_client
from src.core.llm_openai import create_chat_completion
from src.services.keyword_vectorizer import KeywordVectorizer
from src.schemas.outreach import (
    MatchedOpportunity,
    MatchStatus,
    LLMVerificationInput,
    LLMVerificationOutput,
)
from src.utils.logging import get_logger

logger = get_logger(__name__)


@dataclass
class Stage1Result:
    """Stage 1 결과"""
    processed_companies: int
    candidate_matches: int  # company × top_n


@dataclass
class Stage2Result:
    """Stage 2 결과"""
    matched_companies: int
    failed_companies: int
    total_llm_calls: int
    total_cost_usd: Decimal


class OutreachMatchingService:
    """2-Stage 매칭 로직을 담당하는 서비스"""

    def __init__(
        self,
        *,
        db: MySQLClient | None = None,
        keyword_vectorizer: KeywordVectorizer | None = None,
    ):
        self.db = db or MySQLClient.get_instance()
        self.opensearch = get_opensearch_client()
        self._vectorizer = keyword_vectorizer or KeywordVectorizer()

    async def run_stage1(self, pipeline_id: str) -> Stage1Result:
        """Stage 1: Embedding 기반 Top N 추출"""
        config = await self._get_pipeline_config(pipeline_id)
        companies = await self._get_target_companies(pipeline_id)

        processed = 0
        candidates = 0

        for batch in self._batch_companies(companies, batch_size=100):
            # 1. Company Embedding 생성/조회
            company_embeddings = await self._get_or_create_company_embeddings(batch)

            # 2. Weekly Picks와 유사도 검색
            for company_id, embedding in company_embeddings.items():
                top_n_results = await self._search_similar_opportunities(
                    embedding=embedding,
                    weekly_picks_date=config["weekly_picks_date"],
                    top_n=config["top_n"],
                )

                # 3. 후보 저장 (Stage 2 입력용)
                await self._save_stage1_candidates(
                    pipeline_id=pipeline_id,
                    company_id=company_id,
                    candidates=top_n_results,
                )

                processed += 1
                candidates += len(top_n_results)

            # 진행 상황 업데이트
            await self._update_progress(pipeline_id, "stage1", processed, len(companies))

        return Stage1Result(processed_companies=processed, candidate_matches=candidates)

    async def run_stage2(self, pipeline_id: str) -> Stage2Result:
        """Stage 2: LLM 검증 및 Why Relevant 생성"""
        config = await self._get_pipeline_config(pipeline_id)
        companies = await self._get_stage1_completed_companies(pipeline_id)

        matched = 0
        failed = 0
        llm_calls = 0
        total_cost = Decimal("0")

        for batch in self._batch_companies(companies, batch_size=50):
            for company in batch:
                try:
                    # 1. Stage 1 후보 조회
                    candidates = await self._get_stage1_candidates(pipeline_id, company["company_id"])

                    # 2. LLM 검증 호출
                    verification_input = LLMVerificationInput(
                        company_id=company["company_id"],
                        company_name=company["company_name"],
                        company_summary=company["company_summary"],
                        business_portfolio=company.get("business_portfolio"),
                        candidate_opportunities=candidates,
                    )

                    result = await self._verify_with_llm(verification_input)
                    llm_calls += 1
                    total_cost += self._estimate_call_cost(verification_input, result)

                    # 3. 결과 저장
                    if len(result.verified_opportunities) >= 5:
                        await self._save_match_result(
                            pipeline_id=pipeline_id,
                            company_id=company["company_id"],
                            opportunities=result.verified_opportunities[:5],
                            status=MatchStatus.SUCCESS,
                        )
                        matched += 1
                    else:
                        await self._save_match_result(
                            pipeline_id=pipeline_id,
                            company_id=company["company_id"],
                            opportunities=result.verified_opportunities,
                            status=MatchStatus.INSUFFICIENT_CONFIDENCE,
                        )
                        failed += 1

                except Exception as e:
                    logger.warning(
                        "LLM verification failed",
                        company_id=company["company_id"],
                        error=str(e),
                    )
                    await self._save_match_result(
                        pipeline_id=pipeline_id,
                        company_id=company["company_id"],
                        opportunities=[],
                        status=MatchStatus.FAILED,
                        failure_reason=str(e),
                    )
                    failed += 1

            # 진행 상황 업데이트
            await self._update_progress(pipeline_id, "stage2", matched + failed, len(companies))

        return Stage2Result(
            matched_companies=matched,
            failed_companies=failed,
            total_llm_calls=llm_calls,
            total_cost_usd=total_cost,
        )

    async def _verify_with_llm(self, input: LLMVerificationInput) -> LLMVerificationOutput:
        """LLM을 통한 관련성 검증 및 Why Relevant 생성"""
        prompt = self._build_verification_prompt(input)

        response = await create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.3,
        )

        return self._parse_verification_response(response)

    def _build_verification_prompt(self, input: LLMVerificationInput) -> str:
        """검증 프롬프트 생성"""
        opportunities_text = "\n".join([
            f"{i+1}. {opp['title']}\n   Description: {opp['description'][:500]}..."
            for i, opp in enumerate(input.candidate_opportunities)
        ])

        return f"""You are evaluating government contract opportunities for a company.

**Company Information:**
- Name: {input.company_name}
- Summary: {input.company_summary}
- Portfolio: {input.business_portfolio or 'N/A'}

**Candidate Opportunities ({len(input.candidate_opportunities)}):**
{opportunities_text}

**Task:**
For each opportunity, determine if it's relevant to this company's capabilities.
For relevant ones, explain WHY in 2-3 sentences connecting their portfolio to the opportunity's scope.

**Output Format (JSON):**
{{
  "evaluations": [
    {{
      "opportunity_id": "...",
      "is_relevant": true/false,
      "confidence": 0-100,
      "why_relevant": "Your company's experience in X aligns with this opportunity's requirement for Y..."
    }}
  ]
}}

Only include opportunities with confidence >= 50 in your response.
Rank by confidence and return top 5-7 most relevant opportunities."""
```

### 4.3. OutreachDeliveryService

> ⚠️ **OUT OF SCOPE**: 이메일 발송은 기존 이메일 발송 시스템을 활용합니다.
>
> 파이프라인에서 생성된 매칭 결과는 **CSV/JSON 형태로 내보내기**하여
> 기존 대량 이메일 발송 시스템에서 활용합니다.

#### 결과 내보내기 포맷

매칭 결과는 다음 형식으로 내보내기 가능합니다:

**CSV 형식** (이메일 발송 시스템용):
```csv
email,first_name,company_name,opportunity_1_title,opportunity_1_why,opportunity_1_agency,...
john@techcorp.com,John,TechCorp Inc.,"Cloud Services Support","귀사의 AWS 경험이...","DoD",...
```

**JSON 형식** (상세 데이터 분석용):
```json
{
  "pipeline_id": "pipe_20260120_abc123",
  "weekly_picks_date": "2026-01-20",
  "results": [
    {
      "email": "john@techcorp.com",
      "first_name": "John",
      "company_name": "TechCorp Inc.",
      "matched_opportunities": [
        {
          "title": "Cloud Services Support",
          "agency": "DoD",
          "why_relevant": "귀사의 AWS 경험이...",
          "confidence": 87
        }
      ]
    }
  ]
}
```

---

## 5. API Specifications

### 5.1. src/api/outreach.py

```python
"""Outreach API 라우터"""

from fastapi import APIRouter, BackgroundTasks, Query, Path
from fastapi.responses import StreamingResponse
from src.schemas.outreach import (
    StartPipelineRequest,
    StartPipelineResponse,
    PipelineStatusResponse,
    GetSamplesRequest,
    SamplesResponse,
    ExportFormat,
)
from src.services.outreach_pipeline_service import OutreachPipelineService
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/outreach", tags=["outreach"])


@router.post("/pipeline", response_model=StartPipelineResponse, status_code=202)
async def start_pipeline(
    request: StartPipelineRequest,
    background_tasks: BackgroundTasks,
):
    """
    새로운 Outreach 파이프라인을 시작합니다.

    - 컨택리스트 로딩 (Google Sheets / CSV / XLSX)
    - Stage 1: Embedding 기반 Top N 후보 추출
    - Stage 2: LLM 검증 및 Why Relevant 생성
    """
    service = OutreachPipelineService()
    response = await service.start_pipeline(request)

    # 백그라운드에서 파이프라인 실행
    if not request.dry_run:
        background_tasks.add_task(service.run_pipeline, response.pipeline_id)

    return response


@router.get("/pipeline/{pipeline_id}", response_model=PipelineStatusResponse)
async def get_pipeline_status(
    pipeline_id: str = Path(..., description="파이프라인 ID"),
):
    """파이프라인 상태를 조회합니다."""
    service = OutreachPipelineService()
    return await service.get_pipeline_status(pipeline_id)


@router.get("/pipeline/{pipeline_id}/samples", response_model=SamplesResponse)
async def get_pipeline_samples(
    pipeline_id: str = Path(...),
    sampling_method: str = Query("random"),
    count: int = Query(100, ge=10, le=500),
):
    """매칭 결과 샘플을 조회합니다."""
    service = OutreachPipelineService()
    request = GetSamplesRequest(sampling_method=sampling_method, count=count)
    return await service.get_samples(pipeline_id, request)


@router.get("/pipeline/{pipeline_id}/export")
async def export_results(
    pipeline_id: str = Path(...),
    format: ExportFormat = Query(ExportFormat.CSV, description="내보내기 형식"),
):
    """
    매칭 결과를 CSV 또는 JSON 형식으로 내보냅니다.

    기존 이메일 발송 시스템에서 활용할 수 있는 형식으로 출력합니다.
    """
    service = OutreachPipelineService()
    data, filename, media_type = await service.export_results(pipeline_id, format)

    return StreamingResponse(
        data,
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
```

> ⚠️ **Out of Scope API 엔드포인트** (기존 이메일 발송 시스템 활용):
> - `POST /pipeline/{pipeline_id}/send` - 이메일 발송
> - `GET /pipeline/{pipeline_id}/metrics` - 발송 성과 지표
> - `POST /unsubscribe/{token}` - 구독 취소

### 5.2. Router 등록

**src/api/router.py** 수정:
```python
from src.api.outreach import router as outreach_router

# ... 기존 코드 ...

def register_routers(app: FastAPI) -> None:
    # ... 기존 라우터들 ...
    app.include_router(outreach_router, prefix="/api")
```

---

## 6. CLI Script

### 6.1. scripts/run_outreach_pipeline.py

```python
#!/usr/bin/env python
"""Weekly Picks Outreach CLI 스크립트

Usage:
    # 파이프라인 시작 (Google Spreadsheet 사용)
    uv run python scripts/run_outreach_pipeline.py start --date 2026-01-20

    # 파이프라인 시작 (CSV 파일 사용)
    uv run python scripts/run_outreach_pipeline.py start --date 2026-01-20 --source csv --file contacts.csv

    # 파이프라인 시작 (XLSX 파일 사용)
    uv run python scripts/run_outreach_pipeline.py start --date 2026-01-20 --source xlsx --file contacts.xlsx

    # 파이프라인 상태 확인
    uv run python scripts/run_outreach_pipeline.py status --pipeline-id pipe_20260120_abc123

    # 샘플 확인
    uv run python scripts/run_outreach_pipeline.py samples --pipeline-id pipe_20260120_abc123 --count 50

    # 결과 내보내기 (CSV)
    uv run python scripts/run_outreach_pipeline.py export --pipeline-id pipe_20260120_abc123 --format csv

    # 결과 내보내기 (JSON)
    uv run python scripts/run_outreach_pipeline.py export --pipeline-id pipe_20260120_abc123 --format json
"""

import argparse
import asyncio
from datetime import date
from pathlib import Path

from src.services.outreach_pipeline_service import OutreachPipelineService
from src.schemas.outreach import (
    StartPipelineRequest,
    GetSamplesRequest,
    EmbeddingBase,
    ContactLoadSource,
    ExportFormat,
)
from src.utils.logging import get_logger

logger = get_logger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Weekly Picks Outreach Pipeline CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # start command
    start_parser = subparsers.add_parser("start", help="Start a new pipeline")
    start_parser.add_argument("--date", required=True, help="Weekly picks date (YYYY-MM-DD)")
    start_parser.add_argument(
        "--source",
        choices=["google_sheets", "csv", "xlsx"],
        default="google_sheets",
        help="Contact list source"
    )
    start_parser.add_argument("--spreadsheet-id", help="Google Spreadsheet ID (optional)")
    start_parser.add_argument("--file", help="CSV/XLSX file path (required for csv/xlsx source)")
    start_parser.add_argument("--limit", type=int, help="Company limit (for testing)")
    start_parser.add_argument("--embedding", choices=["keyword", "description"], default="description")
    start_parser.add_argument("--top-n", type=int, default=20)
    start_parser.add_argument("--dry-run", action="store_true")

    # status command
    status_parser = subparsers.add_parser("status", help="Check pipeline status")
    status_parser.add_argument("--pipeline-id", required=True)

    # samples command
    samples_parser = subparsers.add_parser("samples", help="View matching samples")
    samples_parser.add_argument("--pipeline-id", required=True)
    samples_parser.add_argument("--count", type=int, default=100)
    samples_parser.add_argument("--method", choices=["random", "by_naics", "by_confidence"], default="random")

    # export command
    export_parser = subparsers.add_parser("export", help="Export matching results")
    export_parser.add_argument("--pipeline-id", required=True)
    export_parser.add_argument("--format", choices=["csv", "json"], default="csv")
    export_parser.add_argument("--output", help="Output file path (optional)")

    return parser.parse_args()


async def cmd_start(args):
    """Start pipeline command"""
    service = OutreachPipelineService()

    # Source 매핑
    source_map = {
        "google_sheets": ContactLoadSource.GOOGLE_SHEETS,
        "csv": ContactLoadSource.CSV_FILE,
        "xlsx": ContactLoadSource.XLSX_FILE,
    }

    # CSV/XLSX 소스인 경우 파일 경로 필수
    if args.source in ["csv", "xlsx"] and not args.file:
        print(f"Error: --file is required when using {args.source} source")
        return

    request = StartPipelineRequest(
        weekly_picks_date=date.fromisoformat(args.date),
        contact_source=source_map[args.source],
        spreadsheet_id=args.spreadsheet_id,
        contact_file_path=args.file,
        company_limit=args.limit,
        embedding_base=EmbeddingBase(args.embedding),
        top_n=args.top_n,
        dry_run=args.dry_run,
    )

    response = await service.start_pipeline(request)
    print(f"Pipeline started: {response.pipeline_id}")
    print(f"Contact source: {args.source}")
    print(f"Estimated duration: {response.estimated_duration_minutes} minutes")
    print(f"Estimated cost: ${response.estimated_cost_usd}")

    if not args.dry_run:
        print("\nRunning pipeline...")
        await service.run_pipeline(response.pipeline_id)
        print("Pipeline completed!")
        print(f"\nTo export results, run:")
        print(f"  uv run python scripts/run_outreach_pipeline.py export --pipeline-id {response.pipeline_id}")


async def cmd_status(args):
    """Status command"""
    service = OutreachPipelineService()
    status = await service.get_pipeline_status(args.pipeline_id)

    print(f"Pipeline: {status.pipeline_id}")
    print(f"Status: {status.status}")
    print(f"Progress: {status.progress.percentage:.1f}% ({status.progress.completed}/{status.progress.total})")
    print(f"Matched: {status.matched_companies}")
    print(f"Failed: {status.failed_companies}")
    print(f"LLM Calls: {status.metrics.llm_calls}")
    print(f"Cost: ${status.metrics.current_cost_usd}")


async def cmd_samples(args):
    """Samples command"""
    service = OutreachPipelineService()
    samples = await service.get_samples(
        args.pipeline_id,
        GetSamplesRequest(sampling_method=args.method, count=args.count),
    )

    for sample in samples.samples:
        print(f"\n{'='*60}")
        print(f"Company: {sample.company.company_name}")
        print(f"NAICS: {sample.company.primary_naics_code}")
        print(f"Summary: {sample.company.company_summary[:200]}...")
        print(f"\nMatched Opportunities:")
        for opp in sample.matched_opportunities:
            print(f"  #{opp.rank}. {opp.opportunity_title}")
            print(f"      Confidence: {opp.confidence}%")
            print(f"      Why: {opp.why_relevant[:150]}...")


async def cmd_export(args):
    """Export command"""
    service = OutreachPipelineService()

    format_enum = ExportFormat.CSV if args.format == "csv" else ExportFormat.JSON
    data, filename, media_type = await service.export_results(args.pipeline_id, format_enum)

    # 출력 파일 경로 결정
    output_path = args.output or filename

    # 파일 저장
    with open(output_path, "wb") as f:
        for chunk in data:
            f.write(chunk)

    print(f"Results exported to: {output_path}")
    print(f"Format: {args.format.upper()}")
    print(f"\nThis file can be used with your existing email sending system.")


async def main():
    args = parse_args()

    commands = {
        "start": cmd_start,
        "status": cmd_status,
        "samples": cmd_samples,
        "export": cmd_export,
    }

    await commands[args.command](args)


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 7. Integration Points

### 7.1. 기존 컴포넌트 활용

| 기존 컴포넌트 | 활용 방식 |
|---------------|-----------|
| `KeywordVectorizer` | Company Summary/Portfolio embedding 생성에 재사용 |
| `SearchService` | OpenSearch KNN 검색 확장 (multi_vector_knn_search 참조) |
| `EmailService` | 이메일 렌더링 패턴 참조, SendGrid/SES 연동 재사용 |
| `MySQLClient` | DB 연결 및 트랜잭션 처리 |
| `get_opensearch_client` | Vector 저장 및 검색 |

### 7.2. 신규 OpenSearch Index

```json
{
  "outreach_company_embeddings": {
    "mappings": {
      "properties": {
        "company_id": { "type": "keyword" },
        "embedding": {
          "type": "knn_vector",
          "dimension": 1536,
          "method": {
            "name": "hnsw",
            "space_type": "cosinesimil"
          }
        },
        "updated_at": { "type": "date" }
      }
    }
  }
}
```

### 7.3. Settings 확장

**src/settings.py** 추가:
```python
class OutreachSettings(BaseSettings):
    """Outreach 관련 설정"""

    # 파이프라인 설정
    default_top_n: int = Field(default=20)
    min_confidence: int = Field(default=50)
    batch_size: int = Field(default=100)  # Embedding 처리 배치 크기
    max_retries: int = Field(default=3)

    # Google Spreadsheet 설정
    google_spreadsheet_id: str = Field(
        default="1l9X6kVkjhmbWUFZOuREe-9sY1Rjwlfbre16yP-hyJkU",
        validation_alias="OUTREACH_GOOGLE_SPREADSHEET_ID",
        description="기본 컨택리스트 Google Spreadsheet ID"
    )
    google_service_account_path: str = Field(
        default="",
        validation_alias="GOOGLE_SERVICE_ACCOUNT_PATH",
        description="Google Service Account JSON 파일 경로"
    )

    # 결과 내보내기 설정
    export_output_dir: str = Field(
        default="./output/outreach",
        description="결과 파일 출력 디렉토리"
    )

    model_config = SettingsConfigDict(
        env_file=f".env{os.getenv('PROFILE', '')}",
        env_prefix="outreach_",
        case_sensitive=False,
    )
```

**환경 변수 예시** (`.env` 파일):
```bash
# Google Spreadsheet 설정
OUTREACH_GOOGLE_SPREADSHEET_ID=1l9X6kVkjhmbWUFZOuREe-9sY1Rjwlfbre16yP-hyJkU
GOOGLE_SERVICE_ACCOUNT_PATH=/path/to/service-account.json

# 결과 내보내기 설정
OUTREACH_EXPORT_OUTPUT_DIR=./output/outreach
```

---

## 8. Error Handling

### 8.1. 에러 분류

| 에러 유형 | 처리 방식 | 재시도 |
|-----------|-----------|--------|
| LLM Rate Limit | Exponential backoff | 최대 3회 |
| LLM Timeout | 재시도 후 스킵 | 최대 3회 |
| OpenSearch 연결 오류 | 파이프라인 중단 | 없음 |
| MySQL 데드락 | 자동 재시도 (기존 로직) | 최대 5회 |
| 이메일 발송 실패 | 개별 건 스킵 | 없음 |
| Bounce 수신 | 상태 업데이트 | 없음 |

### 8.2. 로깅 패턴

```python
# 성공 케이스
logger.info(
    "Company matched successfully",
    pipeline_id=pipeline_id,
    company_id=company_id,
    matched_count=5,
)

# 실패 케이스
logger.warning(
    "LLM verification failed",
    pipeline_id=pipeline_id,
    company_id=company_id,
    error=str(e),
    retry_count=retry,
)

# 치명적 오류
logger.error(
    "Pipeline failed",
    pipeline_id=pipeline_id,
    error=str(e),
    exc_info=True,
)
```

---

## 9. Performance Considerations

### 9.1. 병렬 처리

- Stage 1 Embedding: 배치 단위 (100 기업씩) 병렬 처리
- Stage 2 LLM: 50 기업씩 배치, rate limit 고려
- 이메일 발송: 1000건씩 배치, 배치 간 60초 딜레이

### 9.2. 예상 처리 시간

| 단계 | 60k 기업 기준 | 병목 |
|------|---------------|------|
| Stage 1 | 1-2시간 | OpenSearch 검색 |
| Stage 2 | 4-6시간 | LLM API 호출 |
| 이메일 발송 | 1-2시간 | SendGrid rate limit |

### 9.3. 비용 최적화

- Stage 1에서 confidence 낮은 후보 조기 제거
- LLM 호출 시 batch 처리 (여러 기업 한 번에)
- 이전 파이프라인의 embedding 재사용

---

## 10. Testing Strategy

### 10.1. Unit Tests

```python
# tests/services/test_outreach_matching_service.py

async def test_stage1_returns_top_n_candidates():
    """Stage 1이 지정된 Top N 개수만큼 후보를 반환하는지 확인"""
    ...

async def test_stage2_filters_low_confidence():
    """Stage 2가 낮은 confidence 결과를 필터링하는지 확인"""
    ...

async def test_verify_with_llm_generates_why_relevant():
    """LLM 검증이 Why Relevant 설명을 생성하는지 확인"""
    ...
```

### 10.2. Integration Tests

```python
# tests/api/test_outreach_api.py

async def test_start_pipeline_returns_pipeline_id():
    """POST /outreach/pipeline이 pipeline_id를 반환하는지 확인"""
    ...

async def test_get_pipeline_status_returns_progress():
    """GET /outreach/pipeline/{id}가 진행 상황을 반환하는지 확인"""
    ...
```

---

## 11. Deployment Checklist

- [ ] MySQL 마이그레이션 스크립트 실행 (신규 테이블 생성)
  - `outreach_pipeline_run`
  - `outreach_company_match`
  - `outreach_matched_opportunity`
- [ ] OpenSearch 인덱스 생성 (`outreach_company_embeddings`)
- [ ] Google Service Account 설정
  - Service Account JSON 파일 배치
  - `GOOGLE_SERVICE_ACCOUNT_PATH` 환경 변수 설정
  - Spreadsheet 공유 권한 확인
- [ ] 환경 변수 설정
  - `OUTREACH_GOOGLE_SPREADSHEET_ID`
  - `OUTREACH_EXPORT_OUTPUT_DIR`
- [ ] 라우터 등록 확인 (src/api/router.py)
- [ ] CLI 스크립트 테스트 (dry-run 모드)
  - Google Spreadsheet 로딩 테스트
  - CSV/XLSX 파일 로딩 테스트
- [ ] 1k 샘플 파이프라인 실행 및 검증
- [ ] 결과 내보내기 테스트 (CSV/JSON)
- [ ] 기존 이메일 발송 시스템 연동 확인
