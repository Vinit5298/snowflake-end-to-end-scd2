# Architecture Design

## End-to-End Flow
1. Data lands in AWS S3
2. Snowpipe ingests incremental files
3. COPY command loads historical data
4. RAW layer stores data as-is
5. BRONZE layer standardizes data
6. SILVER layer applies SCD Type 2 logic
7. ANALYTICS layer supports BI reporting

## Design Principles
- RAW layer is immutable
- SCD logic exists only in SILVER
- Tasks are event-driven
- Separate warehouses for ingestion and analytics