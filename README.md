# 🛡️ FinTech Fraud Analytics & Risk Detection Pipeline

An end-to-end data engineering and business intelligence solution designed to process high-volume financial transaction datasets (~1.7 GB), identify complex fraud patterns, perform feature engineering, and surface executive-level risk intelligence through an interactive two-page Power BI report.

---

## 📌 Executive Summary
In high-throughput FinTech environments, real-time transaction monitoring and historical fraud analysis are critical to reducing operational loss and safeguarding customer accounts. This project establishes an automated Python ETL pipeline that ingests, cleans, enriches, and validates transaction logs. The processed data is modeled into Power BI to track fraud conversion rates, channel vulnerabilities, temporal fraud anomalies, and merchant risk exposure.

---

## 📂 Repository Structure

```text
fintech-fraud-analytics-powerbi/
│
├── dashboard/
│   └── Fintech_Fraud_Transactions_Analytics.pbix  # Production Power BI Report (Git LFS)
│
├── Dashboard_Images/
│   ├── page 1.jpg                                 # Executive Summary View
│   └── page 2.jpg                                 # Risk & Anomaly Deep Dive
│
├── data/
│   ├── financial_fraud_detection_dataset.csv      # Raw Ingestion Dataset (Git LFS)
│   └── processed_financial_fraud_data.csv        # Processed & Feature-Engineered CSV (Git LFS)
│
├── etl/
│   ├── run_fraud_etl.py                           # Python ETL Pipeline Script
│   └── final_pipeline.log                         # Automated Execution Logs
│
├── .gitattributes                                 # Git LFS Tracking Rules
├── .gitignore                                    # File Exclusion Rules
└── README.md                                      # Project Documentation
