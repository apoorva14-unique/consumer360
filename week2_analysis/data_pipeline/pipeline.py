# ---------------- DATA PIPELINE ----------------

import pandas as pd

print("🚀 Starting Data Pipeline...\n")

# ---------------- LOAD RAW DATA ----------------
df = pd.read_csv('data/raw/Retail.csv', encoding='ISO-8859-1')

print("Raw Data Shape:", df.shape)

# ---------------- BASIC CLEANING ----------------

# Remove missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove invalid transactions
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

print("Cleaned Data Shape:", df.shape)

# ---------------- SAVE CLEANED DATA ----------------

df.to_csv('week2_analysis/data_pipeline/cleaned_data.csv', index=False)

print("\n✅ Cleaned data saved successfully!")

# ---------------- RUN RFM ----------------

import subprocess

print("\n🔄 Running RFM Analysis...")

subprocess.run(["python", "week2_analysis/rfm_analysis/rfm.py"])

print("\n✅ Pipeline Completed Successfully")