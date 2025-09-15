import pandas as pd
from sqlalchemy import create_engine

def load_data():
    engine = create_engine("postgresql://airflow:airflow@localhost:5432/nyc_taxi")
    df = pd.read_csv("data/clean_taxi.csv")
    df.to_sql("yellow_taxi_data", engine, if_exists="replace", index=False)
    print("✅ Data loaded into PostgreSQL")

if __name__ == "__main__":
    load_data()
