# Data Quality & Validation

## Purpose
This document defines validation rules to ensure correctness,
consistency, and reliability of the data pipeline.

## Key Checks Implemented

### SCD Type 2 Integrity
- Only one active record per CUSTOMER_ID
- Historical versions preserved
- Valid effective date ranges

### Domain Validation
- Valid credit ratings (A, B, C)
- Valid email formats
- Valid phone number lengths

## Execution
All checks are implemented as SQL validation queries and
can be run manually or scheduled in production.

## Expected Outcome
All validation queries should return zero rows
unless data quality issues are present.
