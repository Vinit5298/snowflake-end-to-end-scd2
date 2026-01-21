# Operational Monitoring & Recovery

## Monitoring Strategy

### Tasks
- Use INFORMATION_SCHEMA.TASK_HISTORY
- Monitor:
  - LAST_SUCCESS_TIME
  - LAST_FAILED_TIME
  - ERROR_MESSAGE

### Streams
- Ensure streams are not stale
- Verify SYSTEM$STREAM_HAS_DATA triggers

## Common Failure Scenarios

### Task Failure
- Causes:
  - Warehouse suspended
  - Permission changes
  - Syntax errors
- Recovery:
  - Fix root cause
  - Resume task
  - No data loss due to streams

### Missing Data
- Check:
  - Raw table ingestion
  - Stream lag
  - Task execution history

## Restart Safety
- Snowflake streams ensure:
  - Exactly-once processing
  - No duplicate ingestion
- Tasks can be safely resumed without reprocessing data

## Production Readiness
This pipeline is idempotent, restart-safe,
and observable using native Snowflake features.
