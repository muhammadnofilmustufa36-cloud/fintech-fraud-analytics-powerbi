# 🛡️ FinTech Fraud Analytics & Risk Detection Pipeline

An end-to-end data engineering and business intelligence solution designed to process high-volume financial transaction datasets (~1.7 GB), identify complex fraud patterns, perform feature engineering, and surface executive-level risk intelligence through an interactive two-page Power BI report.

---

## 📌 Executive Summary
In high-throughput FinTech environments, real-time transaction monitoring and historical fraud analysis are critical to reducing operational loss and safeguarding customer accounts. This project establishes an automated Python ETL pipeline that ingests, cleans, enriches, and validates transaction logs. The processed data is modeled into Power BI to track fraud conversion rates, channel vulnerabilities, temporal fraud anomalies, and merchant risk exposure.

---
⚙️ Data Pipeline & ETL Architecture
The automated Python pipeline (etl/run_fraud_etl.py) handles the full transformation lifecycle:

Data Ingestion & Cleaning: Reads raw multi-gigabyte transaction logs, handles missing values, cleans string formats, and enforces correct data types for timestamp and financial values.

Feature Engineering:

Temporal Extraction: Derives HourOfDay, DayOfWeek, and IsWeekend flags to isolate off-peak transaction bursts.

Balance Anomaly Detection: Calculates pre- and post-transaction balance disparities (OldBalance_Org vs. NewBalance_Org) to catch total account drain anomalies.

Risk Scoring: Assigns dynamic risk flags based on transaction channels and high-frequency transfer behaviors.

Validation & Logging: Logs row-level metrics, processing execution time, and data validation flags into final_pipeline.log.

📊 Dashboard Highlights & Key DAX Metrics
🖼️ Page 1: Executive Overview
KPI Header Cards: Tracks Total Transaction Volume, Total Fraud Count, Aggregate Financial Loss Exposure, and Overall Fraud Rate (%).

Merchant & Channel Breakdown: Identifies high-risk transaction channels (e.g., Transfer vs. Cash Out) and categorizes merchant risk profiles.

Loss Exposure Trends: Displays financial risk distribution across transaction size cohorts.

🖼️ Page 2: Risk Analysis & Anomaly Detection
Temporal Anomaly Heatmap: Maps peak fraud activity against hour-of-day distributions, pinpointing midnight to early-morning spikes.

Geographic & Transfer Hotspots: Visualizes location-based anomaly clusters and flags rapid multi-account transfer chains.

Customer Balance Metrics: Interactive matrix highlighting balance mismatch indicators before and after fraudulent transactions.

🛠️ Tech Stack & Methodologies
Business Intelligence: Power BI Desktop, DAX (Data Analysis Expressions), Star Schema Modeling, Data Visualization

Data Engineering: Python 3.x, Pandas, Automated Logging

Version Control: Git, Git LFS (Large File Storage tracking ~1.7 GB .pbix and .csv assets)

🚀 Getting Started & Local Setup
Prerequisites
Power BI Desktop

Git & Git LFS installed locally

Clone & Download Datasets
Bash
# Clone the repository
git clone [https://github.com/muhammadnofilmustufa36-cloud/fintech-fraud-analytics-powerbi.git](https://github.com/muhammadnofilmustufa36-cloud/fintech-fraud-analytics-powerbi.git)

# Move into project directory
cd fintech-fraud-analytics-powerbi

# Pull heavy Git LFS assets (.pbix & .csv files)
git lfs pull
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
