-- No NULL values
SELECT COUNT(*) AS null_count
FROM processed.accelerometer_clean
WHERE magnitude IS NULL;
