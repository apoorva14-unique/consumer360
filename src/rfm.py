import pandas as pd

# Load dataset
df = pd.read_csv('data/raw/retail.csv', encoding='ISO-8859-1')

# Preview
print("Initial Data:")
print(df.head())

# ---------------- CLEANING ----------------

# Remove null CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove negative or zero quantity
df = df[df['Quantity'] > 0]

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ---------------- RFM ----------------

snapshot_date = df['InvoiceDate'].max()

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'count',
    'Revenue': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM Table:")
print(rfm.head())