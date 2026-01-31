from pathlib import Path

def test_sql_files_exist():
    sql_files = [
        "data_processing/data_validation/validation.sql",
        "data_processing/data_transformation/transformation.sql",
    ]

    for file in sql_files:
        assert Path(file).exists(), f"Missing {file}"
