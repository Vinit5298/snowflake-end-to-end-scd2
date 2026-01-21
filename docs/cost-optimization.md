# Cost & Warehouse Optimization

## Overview
This project follows Snowflake best practices for cost control by
separating compute workloads and enabling auto-suspend.

## Warehouse Strategy

### INGEST_WH
- Size: XSMALL
- Purpose: Snowpipe ingestion and COPY operations
- Reason:
  - Ingestion is lightweight
  - Event-driven
  - No heavy joins or transformations

### TRANSFORM_WH
- Size: SMALL
- Purpose:
  - Streams
  - Tasks
  - SCD Type 2 merges
- Reason:
  - Transformations require more compute
  - CDC merge operations are CPU intensive

### BI_WH
- Size: SMALL
- Purpose:
  - Reporting
  - Analytics queries
- Reason:
  - Read-heavy workload
  - Isolated from ingestion and transformations

## Auto-Suspend Configuration
- INGEST_WH: 60 seconds
- TRANSFORM_WH: 60 seconds
- BI_WH: 120 seconds

This ensures:
- Zero cost when idle
- No manual intervention required

## Cost Control Benefits
- No shared warehouses across workloads
- Predictable billing
- Easy future scaling per workload

## Production Readiness
This design prevents runaway queries and ensures
cost transparency across ingestion, transformation,
and analytics workloads.
