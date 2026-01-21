# Snowflake Foundation Setup

## Database
- PROJECT_DB

## Schemas
- RAW       : As-is ingestion
- BRONZE    : Cleaned & standardized
- SILVER    : SCD Type 2
- ANALYTICS : Reporting layer

## Warehouses
- INGEST_WH     : S3 ingestion & Snowpipe
- TRANSFORM_WH  : Streams, Tasks, SCD logic
- BI_WH         : Reporting & analytics

## Design Principles
- Separation of compute by workload
- Auto-suspend to control cost
- Single database, multiple schemas
