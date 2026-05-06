# Pipeline script to run full analysis

import os

print("Running RFM Analysis...")

os.system("python week2_analysis/rfm_analysis/rfm.py")

print("Pipeline Completed")