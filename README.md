# 🛡️ Bank Transaction Fraud Detection System

A complete data analysis and machine learning project to detect fraudulent financial transactions using **SQL + Python**. The solution applies **Z-Score** and **Isolation Forest** anomaly detection methods, with robust **feature engineering**, **data visualization**, and **SQL integration**.

---

## 📌 Objective

The objective of this project is to identify potential fraud in a bank’s transaction data by:

- Importing real-world-style data into **MySQL**
- Performing **data preprocessing** and **feature engineering**
- Applying **Z-Score** and **Isolation Forest** algorithms for anomaly detection
- Evaluating models using classification metrics
- Visualizing actual vs predicted fraud

---

## 🧠 Key Concepts

- Anomaly Detection
- Z-Score Method
- Isolation Forest (unsupervised ML)
- SQL + Python Integration
- Feature Engineering (balance error)
- Class Imbalance Handling
- Data Visualization

---

## 🗃️ Dataset

- **Source**: [PaySim Dataset on Kaggle](https://www.kaggle.com/datasets/ntnu-testimon/paysim1)
- **Type**: Synthetic financial transaction data (CSV)
- **Rows**: Over 1 million
- **Target**: `isFraud` column (1 = fraudulent, 0 = legitimate)

---

## 🧱 Database Setup

The SQL schema is defined in [`bank.sql`](./bank.sql):

```sql
CREATE DATABASE bank_fraud_detetion;
USE bank_fraud_detetion;

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


