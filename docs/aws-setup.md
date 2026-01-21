# AWS Setup – S3 & IAM

## S3 Bucket
- Bucket Name: snowflake-end-to-end-scd2
- Region: Asia Pacific (Mumbai) ap-south-1

## Folder Structure
raw/
└── customer/
    ├── full/
    └── cdc/

## Purpose
- `full` – Initial and backfill loads
- `cdc` – Incremental changes for Snowpipe

## IAM Bootstrap Trust
Due to AWS validation rules, the IAM role was initially created
trusting the local AWS account root. 

The trust policy is later updated with Snowflake-provided principal and external ID.

## Final IAM Trust Policy

The IAM role trusts the Snowflake-managed IAM user returned by
`DESC INTEGRATION`, protected by a Snowflake-generated External ID.

Principal:
arn:aws:iam::682967445054:user/wndf1000-s

External ID:
ZK92184_SFCRole=2_e8NkzAevmfMN8QnluPWYkhYyn7k=

