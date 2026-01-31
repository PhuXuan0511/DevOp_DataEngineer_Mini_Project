This project demonstrates an end-to-end data engineering pipeline built with DevOps best practices.
It ingests raw JSON data, validates data quality, applies SQL-based transformations, and orchestrates execution using Apache Airflow, all running in Dockerized services with CI/CD integration.

The project is designed to showcase data engineering + DevOps skills suitable for real-world production pipelines.

🏗 Architecture Overview
Raw JSON Files
      ↓
Python Ingestion
      ↓
PostgreSQL (raw schema)
      ↓
SQL Validation (quality checks)
      ↓
SQL Transformation
      ↓
PostgreSQL (processed schema)
      ↓
Apache Airflow (orchestration)
      ↓
CI/CD Testing & Monitoring

🧰 Tech Stack

Programming: Python, SQL

Database: PostgreSQL

Orchestration: Apache Airflow

Containerization: Docker, Docker Compose

Data Processing: Pandas, SQLAlchemy

CI/CD: GitLab CI

Testing: Pytest (unit, SQL, DAG integrity)

📂 Project Structure
DevOp Mini Project/
│
├── ingestion/
│   └── ingestion_raw_data.py
│
├── data_processing/
│   ├── data_validation/
│   │   ├── validation.sql
│   │   └── validation.py
│   │
│   └── data_transformation/
│       ├── transformation.sql
│       └── transformation.py
│
├── airflow/
│   └── dags/
│       └── data_pipeline_dag.py
│
├── tests/
│   ├── unit/
│   ├── sql/
│   └── dag/
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitlab-ci.yml

🔄 Pipeline Steps
1️⃣ Data Ingestion

Reads multiple newline-delimited JSON files from a local folder

Loads raw data into PostgreSQL (raw schema)

Handles large files using batch inserts

2️⃣ Data Validation

Executes SQL-based quality checks:

Null value detection

Duplicate record detection

Row count validation

Pipeline fails automatically if validation does not pass

3️⃣ Data Transformation

Cleans validated data

Generates analytics-ready tables

Adds derived metrics (e.g. magnitude from accelerometer readings)

Writes results into a processed schema

4️⃣ Orchestration (Airflow)

Tasks:

Ingestion

Validation

Transformation

Enforces task dependencies

Supports retries and logging

Visualized and monitored via Airflow UI

 Running the Project (Local)
Prerequisites

Docker Desktop

Python 3.10+

Git

Start Services
docker compose up -d

Access Airflow UI
http://localhost:8080


Default credentials:

Username: airflow
Password: airflow

// Testing

This project includes automated tests:

Unit tests for ingestion, validation, and transformation logic

SQL tests to verify table creation and row counts

DAG integrity tests to ensure Airflow DAGs load correctly

Run tests locally:

pytest

// CI/CD (GitLab)

GitLab CI pipeline automatically:

Installs dependencies

Runs all tests

Validates DAG integrity

Ensures pipeline reliability before deployment

// Monitoring & Alerting

Task-level monitoring via Airflow UI

Failure alerts via task status and logs

Pipeline stops automatically on validation failure

// Key Learnings & Best Practices

Data quality checks are enforced before transformation

SQL used for heavy data logic to improve performance

Clear separation of raw, staging, and processed layers

Containerized environment ensures reproducibility

CI/CD ensures safe and reliable pipeline changes

// Future Improvements

Add Great Expectations for advanced data validation

Implement incremental ingestion

Deploy to cloud (AWS/GCP)

👤 Author

Phu Nguyen Xuan
DevOps / Data Engineering Enthusiast