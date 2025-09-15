# nyc-taxi-etl
# NYC Taxi ETL Pipeline 🚖

## Overview
A beginner-friendly **ETL pipeline** that extracts, transforms, and loads NYC Taxi data into PostgreSQL.  
Built to run inside **GitHub Codespaces**.

## Steps

### 1. Setup Environment
```bash
pip install -r requirements.txt

2. Install PostgreSQL
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib -y
sudo service postgresql start

3. Create Database
sudo -u postgres psql


Inside psql:

CREATE USER airflow WITH PASSWORD 'airflow';
CREATE DATABASE nyc_taxi OWNER airflow;
GRANT ALL PRIVILEGES ON DATABASE nyc_taxi TO airflow;
\q

4. Run ETL
python scripts/extract.py
python scripts/transform.py
python scripts/load.py

5. Verify Data
psql -h localhost -U airflow -d nyc_taxi -W


Then inside SQL shell:

SELECT COUNT(*) FROM yellow_taxi_data;
SELECT * FROM yellow_taxi_data LIMIT 5;

Architecture
flowchart LR
    A[NYC Taxi API] --> B[Extract: Python]
    B --> C[Transform: Pandas]
    C --> D[Load: PostgreSQL]
