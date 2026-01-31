from sqlalchemy import create_engine, text
import pandas as pd
from pathlib import Path
import sys

DB_URL = "postgresql+psycopg2://airflow:airflow@localhost:5432/airflow"

SQL_FILE = Path("data_processing/data_validation/validation.sql")

def run_validation():
    engine = create_engine(DB_URL)

    with engine.connect() as conn:
        df = pd.read_sql(text(SQL_FILE.read_text()), conn)

    print("\n===== DATA VALIDATION RESULT =====")
    print(df)

    status = df.loc[0, "validation_status"]

    if status != "PASS":
        print("\n Validation FAILED — stopping pipeline")
        sys.exit(1)

    print("\n Validation PASSED — safe to continue")

if __name__ == "__main__":
    run_validation()
