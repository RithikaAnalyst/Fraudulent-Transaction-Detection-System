# 🛡️ Bank Transaction Fraud Detection System

A complete project that detects fraudulent transactions using anomaly detection methods like **Z-Score** and **Isolation Forest**, integrating **SQL + Python** for end-to-end data handling, analysis, and visualization.

---

## Project Objective

The goal is to identify fraudulent transactions in a financial dataset using unsupervised anomaly detection techniques. The project simulates a real-world fraud detection pipeline using:

- MySQL for data storage
- Python (pandas, scikit-learn) for preprocessing and analysis
- Matplotlib & Seaborn for visualization

---

## 🗃️ Dataset

- **Source**: [PaySim Kaggle Dataset](https://www.kaggle.com/datasets/ntnu-testimon/paysim1)
- **Format**: CSV → Imported into MySQL
- **Size**: 1 million+ rows
- **Key Features**:
  - `step`, `type`, `amount`
  - `oldbalanceOrg`, `newbalanceOrig`
  - `oldbalanceDest`, `newbalanceDest`
  - `isFraud`, `isFlaggedFraud`

---

## 🧱 Database Setup

SQL file: [`bank.sql`](./bank.sql)

```sql
-- Create database
CREATE DATABASE bank_fraud_detetion;
USE bank_fraud_detetion;

-- create table
CREATE TABLE transactions (
    step INT,
    type VARCHAR(20),
    amount FLOAT,
    nameOrig VARCHAR(50),
    oldbalanceOrg FLOAT,
    newbalanceOrig FLOAT,
    nameDest VARCHAR(50),
    oldbalanceDest FLOAT,
    newbalanceDest FLOAT,
    isFraud TINYINT,
    isFlaggedFraud TINYINT
);


