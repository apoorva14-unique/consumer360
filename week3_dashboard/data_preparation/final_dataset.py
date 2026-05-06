import pandas as pd

# Load cleaned data
df = pd.read_csv('week2_analysis/data_pipeline/cleaned_data.csv')

# Load RFM data
rfm = pd.read_csv('week2_analysis/segmentation/rfm_output.csv')

# Merge datasets
final_df = df.merge(rfm, on='CustomerID', how='left')

# Save final dataset
final_df.to_csv('week3_dashboard/data_preparation/final_dataset.csv', index=False)

print("✅ Final dataset created for dashboard")