import subprocess

print("🚀 Running Data Pipeline...\n")

# Run RFM analysis
subprocess.run(["python", "week2_analysis/rfm_analysis/rfm.py"])

print("\n✅ Pipeline Completed Successfully")