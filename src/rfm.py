import pandas as pd

# Load dataset
df = pd.read_csv('data/raw/retail.csv', encoding='ISO-8859-1')

# Preview
print("Initial Data:")
print(df.head())

# ---------------- CLEANING ----------------

df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]

df['Revenue'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ---------------- RFM CALCULATION ----------------

snapshot_date = df['InvoiceDate'].max()

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'count',
    'Revenue': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM Table:")
print(rfm.head())

# ---------------- RFM SCORING ----------------

rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1], duplicates='drop')
rfm['F_score'] = pd.qcut(rfm['Frequency'], 5, labels=[1,2,3,4,5], duplicates='drop')
rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5], duplicates='drop')

rfm['RFM_Score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)

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

print("\nRFM with Segments:")
print(rfm.head())

print("\nSegment Distribution:")
print(rfm['Segment'].value_counts())