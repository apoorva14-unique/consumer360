import pandas as pd
import subprocess

print("🚀 Starting Data Pipeline...\n")

# ---------------- LOAD DATA ----------------
df = pd.read_csv('data/raw/Retail.csv', encoding='ISO-8859-1')

print("Raw Data Shape:", df.shape)

# ---------------- CLEANING ----------------
df = df.dropna(subset=['CustomerID'])
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Revenue'] = df['Quantity'] * df['UnitPrice']

print("Cleaned Data Shape:", df.shape)

# ---------------- SAVE CLEANED DATA ----------------
df.to_csv('week2_analysis/data_pipeline/cleaned_data.csv', index=False)

print("✅ cleaned_data.csv created!")

# ---------------- RUN RFM ----------------
print("\n🔄 Running RFM Analysis...")

subprocess.run(["python", "week2_analysis/rfm_analysis/rfm.py"])

print("\n✅ Pipeline Completed Successfully")