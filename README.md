# Consumer360 – Customer Segmentation & CLV Engine

## 📌 Project Overview
Consumer360 is a retail analytics project designed to identify high-value customers and churn risks using data-driven techniques such as RFM (Recency, Frequency, Monetary) segmentation. The goal is to enable targeted marketing and improve customer retention.

---

## 🎯 Objective
- Identify "Champion" customers for premium engagement  
- Detect "At Risk" customers for retention strategies  
- Build a scalable analytics pipeline for business insights  

---

## 🗂️ Dataset
- Online Retail Dataset (Transactional data)
- Each row represents a product within a transaction  
- File used: `data/raw/retail.csv`

---

## ⚙️ Tech Stack
- Python (Pandas)
- SQL (Schema Design)
- Power BI (Upcoming)

---

## 📊 Work Completed

### 🔹 Week 1 – Data Engineering
- Performed data inspection to understand dataset structure  
- Identified issues such as:
  - Missing Customer IDs  
  - Negative quantities (returns/cancellations)  
- Cleaned dataset:
  - Removed null CustomerID  
  - Filtered invalid transactions  
- Created derived column:
  - Revenue = Quantity × UnitPrice  
- Designed basic schema for analytics  

---

### 🔹 Week 2 – Customer Segmentation (RFM Analysis)
- Calculated:
  - Recency (days since last purchase)  
  - Frequency (number of transactions)  
  - Monetary (total spending)  

- Applied scoring:
  - Used quantile-based scoring (1–5 scale)  
  - Generated RFM Score  

- Implemented segmentation:
  - Champions  
  - Loyal Customers  
  - Potential Loyalists  
  - At Risk  

- Validated results:
  - Champions represent high-spending, frequent customers  
  - At Risk customers show low recency  

- Exported output:
  - `data/processed/rfm_output.csv`

---

## 📁 Project Structure

```
consumer360/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   │   └── Retail.csv
│   └── processed/
│
├── week1_data_engineering/
│   ├── data_cleaning/
│   ├── data_inspection/
│   ├── data_transformation/
│   ├── performance_optimization/
│   └── star_schema_design/
│       └── schema.sql
│
├── week2_analysis/
│   ├── rfm_analysis/
│   │   └── rfm.py
│   ├── segmentation/
│   │   └── rfm_output.csv
│   ├── validation/
│   └── market_basket/
│
└── README.md
```

---

## 📈 Key Insights
- Champions are high-value customers with frequent and recent purchases  
- At Risk customers indicate potential churn and require retention strategies  
- Segmentation enables targeted marketing and better decision-making  

---

## 🚀 Next Steps
- Build interactive dashboard using Power BI (Week 3)  
- Perform Market Basket Analysis  
- Conduct Cohort Analysis  
- Automate pipeline for weekly updates (Week 4)   