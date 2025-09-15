import requests
import pandas as pd
import os

def extract_data():
    os.makedirs("data", exist_ok=True)
    url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv"
    df = pd.read_csv(url, nrows=10000)  # sample for demo
    df.to_csv("data/raw_taxi.csv", index=False)
    print("✅ Data extracted and saved to data/raw_taxi.csv")

if __name__ == "__main__":
    extract_data()
