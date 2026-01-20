# Snowflake End-to-End ETL / ELT Project (SCD Type 2)

## Project Overview
This project demonstrates a real-world, end-to-end **Snowflake data engineering pipeline**
built using native Snowflake features.

The solution supports:
- Batch ingestion using COPY command
- Near real-time ingestion using Snowpipe
- Change Data Capture (CDC) using Streams
- Orchestration using Tasks
- Historical tracking using Slowly Changing Dimension (SCD Type 2)
- Analytics-ready dimensional modeling

---

## High-Level Architecture
- **Source**: AWS S3
- **Ingestion**: COPY (Batch), Snowpipe (Near Real-Time)
- **Data Layers**:
  - RAW – As-is ingestion
  - BRONZE – Standardized & cleaned
  - SILVER – SCD Type 2 implementation
  - ANALYTICS – Star schema for reporting
- **Orchestration**: Snowflake Streams & Tasks
- **Audit & Recovery**: Time Travel
- **Compute**: Multi-cluster Virtual Warehouses

---

## Technology Stack
- AWS S3
- Snowflake
- Snowpipe
- Streams & Tasks
- SQL
- Git & GitHub

---

## Repository Structure
snowflake-end-to-end-scd2/
│
├── README.md
├── docs/
│ ├── project-overview.md
│ ├── architecture.md
│ └── phases.md
│
├── diagrams/
│ ├── architecture.png
│ └── dimensional_model.png
│
├── sql/
│ ├── raw/
│ ├── bronze/
│ ├── silver/
│ └── analytics/
│
├── data/
│ └── sample/
│
├── scripts/
└── .gitignore


---

## Project Phases
1. Phase 0 – Project Setup & Documentation
2. Phase 1 – AWS S3 & IAM Setup
3. Phase 2 – Snowflake Foundation
4. Phase 3 – RAW Layer (Ingestion)
5. Phase 4 – BRONZE Layer
6. Phase 5 – SILVER Layer (SCD Type 2)
7. Phase 6 – ANALYTICS Layer
8. Phase 7 – Automation, Monitoring & Recovery

------------------------------------------------------------------

## Author
Built as part of advanced Snowflake Data Engineering practice.
