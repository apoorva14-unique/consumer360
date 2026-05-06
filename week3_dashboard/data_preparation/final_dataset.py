import pandas as pd

print("📊 Preparing final dataset for dashboard...")

# Load cleaned data
df = pd.read_csv("week2_analysis/data_pipeline/cleaned_data.csv")

# Load RFM output
rfm = pd.read_csv("week2_analysis/segmentation/rfm_output.csv")

# Merge datasets
final = df.merge(rfm, on="CustomerID", how="left")

# Select important columns (clean dashboard dataset)
final = final[[
    "CustomerID",
    "Country",
    "Revenue",
    "Recency",
    "Frequency",
    "Monetary",
    "Segment"
]]

# Save final dataset
final.to_csv("week3_dashboard/data_preparation/final_dataset.csv", index=False)

print("✅ Final dataset created!")
print("Shape:", final.shape)