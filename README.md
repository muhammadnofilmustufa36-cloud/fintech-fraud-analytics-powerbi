# 🛡️ Financial Fraud & Risk Executive Analytics Pipeline

An end-to-end data engineering and business intelligence solution designed to process high-volume financial transaction datasets (~1.7 GB), identify systemic fraud patterns, perform root-cause risk decomposition, and surface executive-level risk metrics via an interactive two-page Power BI report.

---

## 📌 Executive Summary
In high-volume FinTech environments, real-time transaction monitoring and historical risk analysis are critical to mitigating financial exposure. This project utilizes an automated Python ETL pipeline to ingest, clean, feature-engineer, and validate multi-gigabyte transaction logs. The processed data feeds directly into a dynamic Power BI report to analyze **$1.8Bn in Total Transaction Volume**, tracking **$553M in Total Fraud Exposure** across global payment gateways and merchant categories.

---

## 📊 Dashboard Pages & Visual Highlights🖼️ 
## Page 1: Executive Risk Overview
## 💳 KPI Header CardsTotal

Transaction Volume ($): $1.8Bn   
Total Fraud Exposure ($): $553M   
Fraud Rate %: 11%   
High Risk Senders: 409K   
Critical Risk Transactions: 128K  

## 🌳 Root Cause Risk Breakdown
Decomposition tree breaking down risk factors across Risk Category $\rightarrow$ Payment Channel $\rightarrow$ Merchant Category.

## 📈 Total Fraud Exposure ($) by YearMonth
Monthly trendline isolating loss spikes across 2023–2024

## 📊 Gateway Risk Matrix
Matrix aggregating High Risk vs. Normal transaction volumes across ACH, card, UPI, and wire_transfer.

## 🍩 Transaction Volume by Merchant Category
Donut breakdown across travel, retail, entertainment, grocery, online, utilities, and restaurant.

## 🖼️ Page 2: Geographical Risk & Gateway Deep-Dive
## 💳 KPI Header Cards
Average Fraud Probability %: 36.6%
Average Velocity Score: 10
Avg Spending Deviation: 14%   
Fraud Loss Share %: 30.8% 

## 🌍 Global Risk Hotspots
Interactive map pinpointing geographical risk concentrations in key markets (Berlin, Dubai, London, New York, Singapore, Sydney, Tokyo).

## 📊 Gateway Risk Breakdown
Comparative bar visual showing Avg Fraud Probability % (High Risk ~77.8% vs. Normal ~31.4%) across all major payment gateways.

## 🗺️ Geographical Exposure by Gateway
Comprehensive matrix mapping cross-border financial exposure per location against each transaction gateway.

---

## 🛠️ Tech Stack & MethodologiesBusiness Intelligence & Analytics: 
1) Power BI Desktop, DAX Metrics, Dimensional Modeling, Root Cause Analysis, Heatmaps   
2) Data Engineering & ETL: Python 3.x, Pandas, Automated Logging & Error Handling   
3) Version Control & LFS: Git, Git LFS (Large File Storage tracking ~1.7 GB .pbix and .csv assets)   


## 📂 Repository Structure

```text
fintech-fraud-analytics-powerbi/
│
├── dashboard/
│   └── Fintech_Fraud_Transactions_Analytics.pbix  # Interactive Power BI Report (Git LFS)
│
├── Dashboard_Images/
│   ├── page 1.jpg                                 # Executive Risk Overview Preview
│   └── page 2.jpg                                 # Geographical Risk & Gateway Deep-Dive Preview
│
├── data/
│   ├── financial_fraud_detection_dataset.csv      # Raw Ingestion Dataset (Git LFS)
│   └── processed_financial_fraud_data.csv        # Processed & Feature-Engineered CSV (Git LFS)
│
├── etl/
│   ├── run_fraud_etl.py                           # Python ETL Pipeline Script
│   └── final_pipeline.log                         # Execution Logs
│
├── .gitattributes                                 # Git LFS Configuration Rules
├── .gitignore                                    # File Exclusion Rules
└── README.md                                      # Documentation
