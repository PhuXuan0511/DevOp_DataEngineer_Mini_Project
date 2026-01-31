from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "raw_data" / "accelerometer"

engine = create_engine(
    "postgresql://airflow:airflow@localhost:5432/airflow"
)

json_files = list(data_path.glob("*.json"))

if not json_files:
    raise ValueError("No JSON files found")

df_list = []
bad_files = []

for file in json_files:
    try:
        temp_df = pd.read_json(file, lines=True)
        if not temp_df.empty:
            df_list.append(temp_df)
        else:
            bad_files.append((file.name, "empty file"))
    except ValueError as e:
        bad_files.append((file.name, str(e)))

if not df_list:
    raise ValueError("No valid JSON data found in any files")

df = pd.concat(df_list, ignore_index=True)

df.to_sql(
    "raw_data",
    engine,
    schema="raw",
    if_exists="replace",
    index=False
)

print(f"Ingested {len(df)} rows")
print(f"Skipped {len(bad_files)} bad files")

for f, reason in bad_files:
    print(f"  - {f}: {reason}")
