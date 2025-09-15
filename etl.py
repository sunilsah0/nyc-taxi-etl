# etl.py
import os

print("🚀 Starting ETL pipeline...")

print("📥 Extracting data...")
os.system("python scripts/extract.py")

print("🔧 Transforming data...")
os.system("python scripts/transform.py")

print("💾 Loading data into SQLite...")
os.system("python scripts/load.py")

print("✅ ETL pipeline completed successfully!")
