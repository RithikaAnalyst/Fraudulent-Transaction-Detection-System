import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt


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

