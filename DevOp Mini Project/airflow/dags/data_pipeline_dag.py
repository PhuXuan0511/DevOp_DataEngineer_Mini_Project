from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from ingestion.ingestion_raw_data import main as ingest_main
from data_processing.data_validation.validation import main as validate_main
from data_processing.data_transformation.transformation import main as transform_main

with DAG(
    dag_id="accelerometer_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",   
    catchup=False,                
    tags=["etl", "accelerometer", "postgres"],
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_raw_data",
        python_callable=ingest_main,
    )

    validate_task = PythonOperator(
        task_id="validate_data",
        python_callable=validate_main,
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_main,
    )

    ingest_task >> validate_task >> transform_task
