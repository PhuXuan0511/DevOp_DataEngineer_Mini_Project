from sqlalchemy import create_engine, text
from pathlib import Path

DB_URL = "postgresql+psycopg2://airflow:airflow@localhost:5432/airflow"

SQL_FILE = Path("data_processing/data_transformation/transformation.sql")

def run_transformation():
    print(" Starting transformation pipeline...")

    engine = create_engine(DB_URL)

    with engine.begin() as conn:
        sql = SQL_FILE.read_text()
        conn.execute(text(sql))

    print(" Transformation completed successfully")

if __name__ == "__main__":
    run_transformation()
