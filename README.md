# DevOps Mini Data Pipeline

##  Project Scope
This project implements an **end-to-end data pipeline** designed to demonstrate **Data Engineering and DevOps practices** in a realistic, production-style setup.

The pipeline:
- Ingests raw JSON sensor data
- Validates data quality using SQL
- Transforms data into analytics-ready tables
- Orchestrates tasks with Apache Airflow
- Runs fully containerized using Docker
- Includes automated testing and CI/CD integration

The main goal is to showcase how data pipelines are built, validated, automated, and monitored in real-world environments.

---

##  Project Architecture
Raw JSON Files
↓
Python Ingestion Script
↓
PostgreSQL (raw schema)
↓
SQL Data Validation
↓
SQL Data Transformation
↓
PostgreSQL (processed schema)
↓
Apache Airflow DAG

All components are deployed using **Docker Compose**, ensuring consistency across environments.

---

##  Project Components

### 1️ Data Ingestion
- Implemented in Python
- Reads newline-delimited JSON files
- Loads data into PostgreSQL (`raw` schema)
- Uses Pandas and SQLAlchemy

### 2️ Data Validation
- SQL-based validation logic
- Checks for:
  - Null values
  - Duplicate records
  - Row count integrity
- Acts as a **quality gate**
- Pipeline stops automatically if validation fails

### 3️ Data Transformation
- SQL-driven transformations
- Cleans validated data
- Adds derived metrics (e.g. accelerometer magnitude)
- Stores results in a processed schema

### 4️ Orchestration (Apache Airflow)
- DAG controls execution order:
  1. Ingestion
  2. Validation
  3. Transformation
- Accessible via Airflow Web UI

### 5️ Infrastructure & DevOps
- Docker & Docker Compose for containerization
- PostgreSQL as the metadata and data warehouse
- CI pipeline using GitLab CI
- Automated testing with Pytest

---

## Instructions (How to Run)

### Prerequisites
- Docker & Docker Compose installed
- Git
- Python 3.10+ (for local development/testing)

## ▶️ Run the Pipeline

Start all services using Docker Compose:

```bash
docker compose up -d
🌐 Access Airflow UI
Open your browser and go to:

http://localhost:8080
🧪 Run Tests Locally
Execute all unit, SQL, and DAG tests:

pytest
 Future Enhancements
Incremental and partitioned data ingestion

Advanced data validation using Great Expectations

Cloud deployment (AWS)

Monitoring with Prometheus & Grafana

Alerting on pipeline failures

Data versioning and lineage tracking

 Author
Phu Nguyen Xuan
Aspiring Data Engineer / DevOps Engineer
