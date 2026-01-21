# BRONZE Layer – Standardized Customer Data

## Purpose
The BRONZE layer transforms RAW JSON data into a structured,
typed relational format suitable for downstream processing.

## Source
- RAW.RAW_CUSTOMER (VARIANT)
- RAW.RAW_CUSTOMER_STREAM (append-only)

## Target Table
- BRONZE.BRONZE_CUSTOMER

## Transformation Logic
- Extract fields from RAW_PAYLOAD
- Apply explicit data types
- Preserve record hash for change detection
- Add ingestion metadata

## Table Structure
| Column | Description |
|------|------------|
| CUSTOMER_ID | Business key |
| CUSTOMER_NAME | Customer name |
| EMAIL_ID | Email address |
| PHONE_NUMBER | Phone number |
| CITY | City |
| STATE | State |
| COUNTRY | Country |
| CUSTOMER_SEGMENT | Segment |
| CREDIT_RATING | Credit rating |
| CUSTOMER_STATUS | Active/Inactive |
| SOURCE_SYSTEM | Source system |
| RECORD_HASH | Hash for change detection |
| LOAD_DATE | Load date |
| LOAD_TIMESTAMP | Load timestamp |

## Automation
- Snowflake STREAM on RAW table
- Snowflake TASK executes every minute
- Event-driven execution using SYSTEM$STREAM_HAS_DATA

## Validation Results
- Total records loaded: 1,500,000
- No duplicate customer IDs
- Task execution successful

## Status
Completed
