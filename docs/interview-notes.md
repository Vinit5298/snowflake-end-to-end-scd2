# Interview Notes – Snowflake End-to-End SCD2 Project

## Project Overview
This project implements an end-to-end data pipeline on Snowflake using
AWS S3 as the source and follows a RAW → BRONZE → SILVER → ANALYTICS architecture.

The pipeline supports near real-time ingestion and SCD Type 2
historical tracking for customer data.

---

## Key Design Decisions

### Why use Snowpipe?
- Event-driven ingestion
- Near real-time data availability
- No manual scheduling required

### Why separate schemas?
- RAW: immutable ingestion
- BRONZE: cleaned, structured data
- SILVER: historical truth (SCD Type 2)
- ANALYTICS: BI-ready consumption layer

### Why SCD Type 2 in SILVER?
- Business requires full history
- Track changes over time
- Support auditing and analytics

### Why Analytics as Views?
- Avoid data duplication
- Always reflect latest SCD state
- Zero maintenance

---

## Cost Optimization
- Separate warehouses by workload
- Smallest viable warehouse sizes
- Auto-suspend enabled everywhere

---

## Failure Handling
- Streams provide exactly-once processing
- Tasks are restart-safe
- No data loss on failure

---

## Common Interview Questions

### How do you ensure one current record?
Using IS_CURRENT flag with SCD Type 2 merge logic.

### How do you handle CDC?
CDC data is ingested via S3, captured by streams,
and processed using MERGE statements.

### What happens if a task fails?
Fix root cause, resume task — streams prevent reprocessing.

---

## Technologies Used
- Snowflake
- AWS S3
- Snowpipe
- Streams & Tasks
- SQL
- Python
- GitHub
