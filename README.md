# Consumer360 – Customer Segmentation & CLV Engine

## 📌 Project Overview
Consumer360 is a retail analytics project designed to identify high-value customers and churn risks using data-driven techniques such as RFM segmentation.

---

## 🎯 Objective
- Identify "Champion" customers for premium engagement  
- Detect "At Risk" customers for retention strategies  
- Build a scalable analytics pipeline  

---

## 🗂️ Dataset
- Online Retail Dataset (Transactional data)
- Each row represents a product within a transaction
- File used: data/raw/retail.csv

---

## ⚙️ Tech Stack
- Python (Pandas)
- SQL
- Power BI (Upcoming)

---

## 📊 Work Completed

### 🔹 Week 1 – Data Engineering
- Data inspection and understanding dataset structure  
- Data cleaning (removed null CustomerID, invalid transactions)  
- Created Revenue column  
- Basic schema design  

---

### 🔹 Week 2 – Customer Segmentation
- Calculated Recency, Frequency, Monetary (RFM) metrics  
- Applied scoring (1–5 scale using quantiles)  
- Generated RFM Score  
- Classified customers into segments:
  - Champions  
  - Loyal Customers  
  - Potential Loyalists  
  - At Risk  

- Exported results to:
  - `rfm_output.csv`

---

## 📁 Project Structure

consumer360/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── week1_data_engineering/
├── week2_analysis/
├── dashboard/
└── README.md

---

## 📈 Key Insights
- Champions represent high-value customers  
- At Risk customers indicate potential churn  
- Segmentation helps in targeted marketing  

---

## 🚀 Next Steps
- Build Power BI Dashboard (Week 3)  
- Implement Market Basket Analysis  
- Perform Cohort Analysis  
- Automate pipeline (Week 4)   