import pandas as pd
import os

def transform_data():
    df = pd.read_csv("data/raw_taxi.csv")

    # Basic cleaning
    df = df.dropna(subset=["passenger_count", "trip_distance"])
    df = df[df["passenger_count"] > 0]
    df = df[df["trip_distance"] > 0]

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/clean_taxi.csv", index=False)
    print("✅ Data transformed and saved to data/clean_taxi.csv")

if __name__ == "__main__":
    transform_data()
