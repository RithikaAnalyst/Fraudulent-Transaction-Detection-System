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

LOAD DATA INFILE '/path/to/PS_20174392719_1491204439457_log.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
