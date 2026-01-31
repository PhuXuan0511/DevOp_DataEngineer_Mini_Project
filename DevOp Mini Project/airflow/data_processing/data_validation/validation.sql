-- =====================================================
-- RAW DATA VALIDATION REPORT
-- =====================================================

WITH base AS (
    SELECT *
    FROM raw.raw_data
),
-- null check

null_check AS (
    SELECT
        COUNT(*) AS null_rows
    FROM base
    WHERE x IS NULL
       OR y IS NULL
       OR z IS NULL
       OR "timeStamp" IS NULL
       OR "user" IS NULL
),
--duplicate check

duplicate_check AS (
    SELECT
        COUNT(*) AS duplicate_rows
    FROM (
        SELECT "user", "timeStamp"
        FROM base
        GROUP BY "user", "timeStamp"
        HAVING COUNT(*) > 1
    ) d
),

row_count AS (
    SELECT COUNT(*) AS total_rows FROM base
)

SELECT
    r.total_rows,
    n.null_rows,
    d.duplicate_rows,
    CASE
        WHEN n.null_rows = 0 AND d.duplicate_rows = 0
        THEN 'PASS'
        ELSE 'FAIL'
    END AS validation_status
FROM row_count r
CROSS JOIN null_check n
CROSS JOIN duplicate_check d;
