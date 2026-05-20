import pandas as pd

# Load data
df = pd.read_csv('data/raw/retail.csv', encoding='ISO-8859-1')

# Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]

# Date conversion
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Month columns
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')

# First purchase month
df['CohortMonth'] = df.groupby('CustomerID')['InvoiceMonth'].transform('min')

# Display sample
print(df[['CustomerID', 'InvoiceMonth', 'CohortMonth']].head())

# Save
df.to_csv('week4_advanced_analytics/cohort_analysis/cohort_output.csv', index=False)

print("✅ Cohort Analysis Completed")