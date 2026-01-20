# AWS Setup – S3 & IAM

## S3 Bucket
- Bucket Name: snowflake-end-to-end-scd2
- Region: us-east-1

## Folder Structure
raw/
└── customer/
    ├── full/
    └── cdc/

## Purpose
- `full` – Initial and backfill loads
- `cdc` – Incremental changes for Snowpipe
