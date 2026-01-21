# Silver Layer – SCD Type 2 (Customer Dimension)

## Purpose
The Silver layer maintains historical customer data using Slowly Changing Dimension Type 2 (SCD2).

## Source
- BRONZE.BRONZE_CUSTOMER
- BRONZE.BRONZE_CUSTOMER_STREAM

## Target
- SILVER.SILVER_CUSTOMER

## Key Columns
- CUSTOMER_ID : Business key
- CUSTOMER_SK : Surrogate key (auto-increment)
- RECORD_HASH : Change detection
- EFFECTIVE_START_DT : Version start date
- EFFECTIVE_END_DT : Version end date
- IS_CURRENT : Active record flag

## Processing Logic
1. Initial load inserts all current bronze records.
2. Incremental changes captured via STREAM.
3. MERGE logic:
   - If RECORD_HASH changes → expire old row, insert new row.
   - Ensures only one IS_CURRENT = TRUE per CUSTOMER_ID.

## Automation
- Snowflake TASK executes MERGE every minute.
- Event-driven using SYSTEM$STREAM_HAS_DATA.

## Validation
- No duplicate active records.
- History preserved for changed customers.
