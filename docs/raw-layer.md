# Phase 3 – RAW Layer (S3 → Snowflake)

## Objective
Ingest raw customer JSON data from Amazon S3 into Snowflake
without applying any transformations.

The RAW layer acts as the immutable source of truth.

---

## S3 Structure
s3://snowflake-end-to-end-scd2/
└── raw/
└── customer/
├── full/ (initial bulk load – COPY INTO)
└── cdc/ (incremental updates – Snowpipe)


---

## Snowflake Objects Created

### File Format
- Name: `JSON_FF`
- Type: JSON
- Purpose: Read raw JSON as-is

### Stage
- Name: `RAW_CUSTOMER_STAGE`
- Type: External stage
- Storage Integration: `s3_snowflake_int`
- Path: `s3://snowflake-end-to-end-scd2/raw/customer/`

### Table
- Name: `RAW_CUSTOMER`
- Columns:
  - `RAW_PAYLOAD` (VARIANT)
  - `METADATA_FILENAME`
  - `METADATA_ROW_NUMBER`
  - `LOAD_TIMESTAMP`

---

## Load Strategy

### Initial Full Load
- Tool: `COPY INTO`
- Source: `raw/customer/full/`
- Reason:
  - Large file (~800MB)
  - One-time historical backfill
  - Better control and auditability

### Incremental Load (Planned)
- Tool: Snowpipe (Auto-ingest)
- Source: `raw/customer/cdc/`
- Trigger: S3 event notifications

---

## Design Principles
- Schema-on-read
- Immutable RAW data
- No business logic in RAW layer
- Supports replay and audit

---

## Validation Performed
- Stage connectivity verified using `LIST`
- Successful COPY INTO execution
- JSON payload validated via VARIANT query
