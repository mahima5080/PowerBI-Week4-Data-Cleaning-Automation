"""
Power BI Internship — Week 4
Data Cleaning & Reporting Automation Script
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_raw_messy_dataset(num_records=500):
    """Generates a raw dataset with intentional data quality issues."""
    np.random.seed(42)
    start_date = datetime(2026, 1, 1)
    
    categories = ["  Electronics ", "ELECTRONICS", "Furniture", " clothing", "Clothing", None]
    regions = ["North America", "Europe ", "ASIA-PACIFIC", "Asia-Pacific", None]
    
    data = []
    for i in range(num_records):
        # Create intentional duplicates
        txn_id = f"TXN-{1000 + (i % 450)}"
        
        # Intentional dirty values
        category = np.random.choice(categories)
        region = np.random.choice(regions)
        
        # Missing or invalid numerical data
        revenue = np.random.choice([round(np.random.uniform(50, 1500), 2), np.nan], p=[0.88, 0.12])
        units = np.random.choice([np.random.randint(1, 10), np.nan], p=[0.90, 0.10])
        
        # Inconsistent date formats
        if i % 15 == 0:
            date_val = "2026/13/45" # Invalid date
        elif i % 5 == 0:
            date_val = (start_date + timedelta(days=i)).strftime("%d-%m-%Y")
        else:
            date_val = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
            
        data.append({
            "TransactionID": txn_id,
            "Date": date_val,
            "Region": region,
            "Category": category,
            "UnitsSold": units,
            "Revenue": revenue
        })
        
    df = pd.DataFrame(data)
    df.to_csv("raw_messy_data.csv", index=False)
    print("[*] Raw messy dataset 'raw_messy_data.csv' created.")
    return df

def run_automated_cleaning_pipeline():
    print("[*] Ingesting raw dataset...")
    df = create_raw_messy_dataset()
    
    initial_rows = len(df)
    
    # 1. Deduplication
    df.drop_duplicates(subset=["TransactionID"], keep="first", inplace=True)
    dedup_count = initial_rows - len(df)
    print(f"[✔] Removed {dedup_count} duplicate records.")
    
    # 2. Text & Categorical Standardization
    df["Category"] = df["Category"].fillna("Unassigned").astype(str).str.strip().str.title()
    df["Region"] = df["Region"].fillna("Unknown").astype(str).str.strip().str.title()
    
    # Standardize specific misspellings / variations
    category_map = {"Electronics": "Electronics", "Furniture": "Furniture", "Clothing": "Clothing"}
    df["Category"] = df["Category"].map(lambda x: category_map.get(x, x))
    
    # 3. Handle Missing Numerical Values (Imputation)
    median_units = df["UnitsSold"].median()
    df["UnitsSold"].fillna(median_units, inplace=True)
    
    median_revenue = df["Revenue"].median()
    df["Revenue"].fillna(median_revenue, inplace=True)
    
    # 4. Datetime Standardization & Invalid Date Filtering
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", format="mixed")
    invalid_dates = df["Date"].isna().sum()
    df["Date"].fillna(pd.to_datetime("2026-01-01"), inplace=True)
    print(f"[✔] Standardized dates ({invalid_dates} invalid dates handled).")
    
    # 5. Calculated Metric Columns
    df["UnitPrice"] = np.round(df["Revenue"] / df["UnitsSold"], 2)
    
    # 6. Export Cleaned Telemetry
    df.to_csv("cleaned_sales_report.csv", index=False)
    df.to_excel("cleaned_sales_report.xlsx", index=False)
    
    print("\n==========================================")
    print(" AUTOMATED DATA CLEANING REPORT SUMMARY")
    print("==========================================")
    print(f"Total Initial Records : {initial_rows}")
    print(f"Final Cleaned Records : {len(df)}")
    print(f"Duplicates Dropped   : {dedup_count}")
    print(f"Missing Values Fixed : Imputed with Medians")
    print(f"Status               : SUCCESS ✔")
    print("==========================================\n")

if __name__ == "__main__":
    run_automated_cleaning_pipeline()