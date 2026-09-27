# 🛡️ Financial Fraud & Risk Executive Analytics Pipeline

An end-to-end data engineering and business intelligence solution designed to process high-volume financial transaction datasets (~1.7 GB), identify systemic fraud patterns, perform root-cause risk decomposition, and surface executive-level risk metrics via an interactive two-page Power BI report.

---

## 📌 Executive Summary
In high-volume FinTech environments, real-time transaction monitoring and historical risk analysis are critical to mitigating financial exposure. This project utilizes an automated Python ETL pipeline to ingest, clean, feature-engineer, and validate multi-gigabyte transaction logs. The processed data feeds directly into a dynamic Power BI report to analyze **$1.8Bn in Total Transaction Volume**, tracking **$553M in Total Fraud Exposure** across global payment gateways and merchant categories.

---


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
