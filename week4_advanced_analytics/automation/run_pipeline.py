import os

print("🚀 Starting Full Consumer360 Pipeline")

# Week 2
os.system("python week2_analysis/data_pipeline/pipeline.py")

# Week 4
os.system("python week4_advanced_analytics/market_basket/market_basket.py")

os.system("python week4_advanced_analytics/cohort_analysis/cohort_analysis.py")

print("✅ Full Pipeline Completed")