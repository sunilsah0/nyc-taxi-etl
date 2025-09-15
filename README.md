README.md
# 🚖 NYC Taxi Data ETL Pipeline

A beginner-friendly **Data Engineering project** that builds an **ETL pipeline** to process **NYC Yellow Taxi data**.  
The pipeline extracts raw data (Parquet), transforms it (cleaning), and loads it into a **SQLite database** for analysis.  
This project runs directly in **GitHub Codespaces** — no local setup required.

---

## 📊 ETL Pipeline Flow

```mermaid
flowchart LR
    A[Extract] -->|Download Parquet| B[Transform]
    B -->|Clean + Save| C[Load]
    C -->|Insert| D[(SQLite Database)]
    D -->|Query| E[Analysis & Insights]

📂 Project Structure
nyc-taxi-etl/
│
├── data/                 # Extracted & transformed data
│   ├── raw_taxi.parquet  # Raw data
│   ├── raw_taxi.csv      # Sampled raw data
│   ├── clean_taxi.csv    # Cleaned data
│
├── scripts/              # ETL scripts
│   ├── extract.py        # Download raw data (Parquet)
│   ├── transform.py      # Clean and transform
│   ├── load.py           # Load into SQLite + analysis
│
├── etl.py                # Master script (runs all steps)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

🛠️ Tech Stack

Python → scripting & ETL

Pandas → data manipulation

PyArrow → Parquet file support

Requests → download data

SQLAlchemy → database connector

SQLite → lightweight relational database

GitHub Codespaces → cloud dev environment

⚙️ Setup & Installation
1. Clone Repository
git clone https://github.com/<your-username>/nyc-taxi-etl.git
cd nyc-taxi-etl

2. Install Dependencies
pip install -r requirements.txt


Contents of requirements.txt:

pandas
sqlalchemy
requests
pyarrow

🚀 Run the Pipeline

Option A – Run step by step:

python scripts/extract.py    # Extract raw taxi data
python scripts/transform.py  # Transform & clean data
python scripts/load.py       # Load into SQLite + analysis


Option B – Run everything in one go:

python etl.py

🛢️ Database

The pipeline creates a SQLite database (nyc_taxi.db) with a table:

yellow_taxi_data → cleaned NYC taxi trip data

Inspect the database:

sqlite3 nyc_taxi.db


Inside SQLite shell:

.tables
.schema yellow_taxi_data
SELECT COUNT(*) FROM yellow_taxi_data;
SELECT * FROM yellow_taxi_data LIMIT 5;
