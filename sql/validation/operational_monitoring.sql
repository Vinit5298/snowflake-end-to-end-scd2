-- =====================================
-- TASK MONITORING
-- =====================================

-- Check task execution history
SELECT
    NAME,
    STATE,
    SCHEDULE,
    LAST_SUCCESS_TIME,
    LAST_FAILED_TIME,
    ERROR_MESSAGE
FROM TABLE(
    INFORMATION_SCHEMA.TASK_HISTORY(
        SCHEDULED_TIME_RANGE_START => DATEADD('HOUR', -24, CURRENT_TIMESTAMP)
    )
)
ORDER BY LAST_SUCCESS_TIME DESC;


-- =====================================
-- STREAM MONITORING
-- =====================================

-- Check if streams have pending data
SHOW STREAMS;

-- Stream lag check
SELECT
    STREAM_NAME,
    TABLE_NAME,
    STALE,
    STALE_AFTER
FROM INFORMATION_SCHEMA.STREAMS;


-- =====================================
-- DATA FLOW VERIFICATION
-- =====================================

-- Raw vs Bronze row counts
SELECT
    (SELECT COUNT(*) FROM RAW.RAW_CUSTOMER)    AS RAW_COUNT,
    (SELECT COUNT(*) FROM BRONZE.BRONZE_CUSTOMER) AS BRONZE_COUNT,
    (SELECT COUNT(*) FROM SILVER.SILVER_CUSTOMER) AS SILVER_COUNT;
