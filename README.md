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
📁 fraud-detection-sql-python/
├── bank.sql               # SQL schema & dataset import
├── fraud detection.py     # Python script with detection logic
├── README.md              # Project documentation


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
```
The Python is defined in [`fraud detection.py`][(./fraud detection.py):
``` python
# Connecting sql and python
engine = create_engine("mysql+pymysql://root:newpassword123@localhost/bank_fraud_detetion")

# Load Data into Python
query = "SELECT * FROM transactions"
df = pd.read_sql(query, con=engine)

# Data Cleaning + Feature Engineering
df_clean=df.drop(['nameOrig','nameDest'], axis=1)

# One-hot encode transaction type
df_encoded=pd.get_dummies(df_clean,columns=['type'])

# Create new features to capture balance errors
df_encoded['error_balance_Org']=df['oldbalanceOrg']-df['newbalanceOrig']-df['amount']
df_encoded['error_balance_Dest']=df['newbalanceDest']-df['oldbalanceDest']-df['amount']

# Z-Score Anomaly Detection
df_numeric=df_encoded.drop('isFraud',axis=1).select_dtypes(include=[np.number])
z_score=np.abs(zscore(df_numeric))
threshold=3
anomalies_zscore=(z_score>threshold).any(axis=1)
df['anomalies_zscor']=anomalies_zscore.astype(int)

#Isolation Forest Detection
isf=IsolationForest(contamination=0.01,random_state=42)
df_encoded['anomination_isolation']=isf.fit_predict(df_encoded.drop(['isFraud'],axis=1))
df['anomination_isolation']=df_encoded['anomination_isolation'].apply(lambda x:1 if x==-1 else 0)

#Model Evaluation
print("z_score_report")
print(classification_report(df['isFraud'],df['anomalies_zscor']))
print("isolationForest_report")
print(classification_report(df['isFraud'],df['anomination_isolation']))

#Visualization
sns.countplot(data=df_encoded, x='isFraud', hue='anomination_isolation')
plt.title('Actual vs Predicted Fraud (Isolation Forest)')
plt.show()
```
## About Me
Rithika R
📌 Data Analyst | SQL | Python | Tableau | Power BI | Excel
🔗 LinkedIn • GitHub


