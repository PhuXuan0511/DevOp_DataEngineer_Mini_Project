import os
import sys

print("\n Starting Data Pipeline...\n")

steps = [
    "py ingestion/ingestion_raw_data.py",
    "py data_processing/data_validation/validation.py",
    "py transformation/transformation.py",
]

for step in steps:
    print(f"▶ Running: {step}")
    exit_code = os.system(step)

    if exit_code != 0:
        print(" Pipeline failed. Stopping.")
        sys.exit(1)

print("\n Pipeline completed successfully!")
