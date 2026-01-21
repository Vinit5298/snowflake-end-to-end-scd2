# Project Phases

## Phase 0 – Project Setup
- Repository structure
- Git versioning
- Documentation foundation

## Phase 1 – AWS Setup
- S3 bucket creation
- IAM role configuration
- Snowpipe event notifications

## Phase 2 – Snowflake Foundation
- Database creation (PROJECT_DB)
- Schema setup (RAW, BRONZE, SILVER, ANALYTICS)
- Warehouse design (INGEST_WH, TRANSFORM_WH, BI_WH)
- Cost-optimized auto-suspend configuration

## Phase 3 – RAW Layer (Ingestion)
- S3 external stage using Storage Integration
- JSON file format
- RAW_CUSTOMER table with VARIANT payload
- Historical load using COPY INTO
- Metadata capture (filename, row number)

## Phase 4 – BRONZE Layer (Standardization)
- Structured relational table (BRONZE.BRONZE_CUSTOMER)
- Extracted fields from RAW JSON payload
- Standardized data types
- Record hash preserved for change detection
- Snowflake STREAM on RAW table (append-only)
- Event-driven TASK (RAW_TO_BRONZE_CUSTOMER_TASK)
- Automated ingestion from RAW → BRONZE
- Validated 1.5M records successfully loaded

## Phase 5 – SILVER Layer (SCD Type 2 with CDC)
- Customer dimension table (SILVER.SILVER_CUSTOMER)
- Surrogate key (CUSTOMER_SK) with business key (CUSTOMER_ID)
- Initial load from BRONZE
- Snowflake STREAM on BRONZE table for CDC
- SCD Type 2 MERGE logic:
- Close old records on change
- Insert new version with updated attributes
- Effective date tracking (EFFECTIVE_START_DT, EFFECTIVE_END_DT)
- Current record indicator (IS_CURRENT)
- Automated TASK (BRONZE_TO_SILVER_CUSTOMER_TASK)
- CDC data ingested via incremental JSON files from S3
- Validated historical tracking and current-state correctness

## Phase 6 – ANALYTICS Layer (Gold)

- BI-ready analytics schema
- DIM_CUSTOMER view built on SILVER SCD table
- Read-optimized warehouse (BI_WH)
- No transformation logic

## Phase 7 – Finalization & Production Hardening

- Data quality validation
- Cost optimization documentation
- Operational monitoring & recovery
- Interview and portfolio readiness
- Final architecture documentation
