-- ============================================================
-- TRANSFORMATION: Accelerometer Clean
--
-- Source schema : raw
-- Source table  : raw_data
-- Target schema : processed
-- Target table  : accelerometer_clean
--
-- Business logic:
-- 1. Remove records with NULL sensor values
-- 2. Compute acceleration magnitude
-- 3. Keep data analytics-ready
-- ============================================================

BEGIN;

-- ------------------------------------------------------------
-- 1. Create processed schema if it does not exist
-- ------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS processed;

-- ------------------------------------------------------------
-- 2. Recreate table for idempotent runs
-- ------------------------------------------------------------
DROP TABLE IF EXISTS processed.accelerometer_clean;

-- ------------------------------------------------------------
-- 3. Transform raw accelerometer data
-- ------------------------------------------------------------
CREATE TABLE processed.accelerometer_clean AS
SELECT
    "user",
    "timeStamp",
    x,
    y,
    z,
    SQRT(x*x + y*y + z*z) AS magnitude
FROM raw.raw_data
WHERE x IS NOT NULL
  AND y IS NOT NULL
  AND z IS NOT NULL;

-- ------------------------------------------------------------
-- 4. Indexes for query performance
-- ------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_accel_clean_user
    ON processed.accelerometer_clean ("user");

CREATE INDEX IF NOT EXISTS idx_accel_clean_timestamp
    ON processed.accelerometer_clean ("timeStamp");

COMMIT;
