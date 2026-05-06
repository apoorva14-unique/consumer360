import pandas as pd
import numpy as np

# ---------------- LOAD DATA ----------------

df = pd.read_csv('data/raw/Retail.csv', encoding='ISO-8859-1')

print("Initial Shape:", df.shape)

# ---------------- CLEANING ----------------

# Remove missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove returns / invalid transactions
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

print("After Cleaning Shape:", df.shape)

# ---------------- RFM CALCULATION ----------------

snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'Revenue': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM Sample:")
print(rfm.head())

# ---------------- RFM SCORING ----------------

rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1], duplicates='drop')
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

rfm['RFM_Score'] = (
    rfm['R_score'].astype(str) +
    rfm['F_score'].astype(str) +
    rfm['M_score'].astype(str)
)

# ---------------- SEGMENTATION ----------------

def segment(row):
    if row['RFM_Score'] == '555':
        return 'Champions'
    elif int(row['F_score']) >= 4:
        return 'Loyal Customers'
    elif int(row['R_score']) >= 3:
        return 'Potential Loyalists'
    else:
        return 'At Risk'

rfm['Segment'] = rfm.apply(segment, axis=1)

# ---------------- CLV (BONUS) ----------------

rfm['CLV'] = rfm['Monetary'] * rfm['Frequency']

# ---------------- OUTPUT ----------------

print("\nSegment Distribution:")
print(rfm['Segment'].value_counts())

rfm.to_csv('week2_analysis/segmentation/rfm_output.csv')

print("\n✅ RFM Analysis Completed")