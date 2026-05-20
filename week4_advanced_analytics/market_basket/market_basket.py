import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Load dataset
df = pd.read_csv('data/raw/retail.csv', encoding='ISO-8859-1')

# Cleaning
df = df.dropna(subset=['Description'])
df = df[df['Quantity'] > 0]

# Group products by Invoice
transactions = df.groupby('InvoiceNo')['Description'].apply(list).tolist()

# Convert to basket format
te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)

basket = pd.DataFrame(te_data, columns=te.columns_)

# Apply Apriori
frequent_items = apriori(basket, min_support=0.02, use_colnames=True)

# Generate Rules
rules = association_rules(frequent_items, metric="lift", min_threshold=1)

# Show top rules
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())

# Save output
rules.to_csv('week4_advanced_analytics/market_basket/market_basket_output.csv', index=False)

print("✅ Market Basket Analysis Completed")