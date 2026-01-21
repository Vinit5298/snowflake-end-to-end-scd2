# ANALYTICS Layer (Gold)

## Purpose
The ANALYTICS layer provides BI-ready, consumption-focused objects
built on top of the SILVER SCD Type 2 tables.

## Source
- SILVER.SILVER_CUSTOMER (SCD Type 2)

## Objects Created
### DIM_CUSTOMER (VIEW)
- One row per customer
- Only current records (IS_CURRENT = TRUE)
- No historical duplication

## Design Decisions
- Implemented as a VIEW to:
  - Avoid data duplication
  - Always reflect latest SCD state
  - Minimize maintenance

## Usage
- Reporting
- Dashboards
- Ad-hoc analytics

## Status
✔ Phase 6 completed
