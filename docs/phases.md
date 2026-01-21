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

Further phases are added incrementally.
