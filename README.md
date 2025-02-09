# Suspicious-Transaction-detection-using-ML
1. Introduction
1.1 Objective
The objective of this project is to build a machine learning model to detect suspicious financial transactions that may be linked to money laundering or other fraudulent activities. This will help financial institutions monitor and prevent illicit activities by identifying anomalous behavior in financial transactions. We will use the One-Class SVM algorithm to classify transactions as Suspicious or Normal, providing early detection of potentially fraudulent transactions.
1.2 Motivation
Money laundering is a major concern for financial institutions globally. With vast numbers of transactions being processed daily, manual monitoring for suspicious activities is impractical. Machine learning algorithms, particularly anomaly detection techniques, can help automate this process and flag potentially fraudulent transactions in real time, saving time and resources while enhancing fraud detection capabilities.
_______________________________________________________________________________________________________________________________________________________
2. Methodology
2.1 Data Collection
The dataset used in this project contains anti-money laundering transaction data. This dataset includes transaction records with various features that can help detect suspicious activities. The dataset is stored in a CSV format and contains the following fields:
●	Time: Timestamp of the transaction
●	Date: Date of the transaction
●	Sender Account: Unique identifier for the sender's account
●	Receiver Account: Unique identifier for the receiver's account
●	Amount: Transaction amount in the specified currency
●	Payment Currency: Currency used for payment (e.g., USD, EUR)
●	Received Currency: Currency received by the receiver
●	Sender Bank Location: Geographical location of the sender's bank
●	Receiver Bank Location: Geographical location of the receiver's bank
●	Payment Type: Type of payment (e.g., wire transfer, credit)
●	Is Laundering: Label for whether the transaction is suspected to be part of a money laundering scheme (1 = yes, 0 = no)
2.2 Data Preprocessing
The preprocessing steps included:
●	Handling Missing Values: Missing data was handled by either removing incomplete records or imputing with appropriate values.
●	Feature Selection: Only the relevant features were used for training the machine learning model. Features like Amount and Payment Type were chosen, while irrelevant columns (e.g., Receiver Bank Location) were removed to simplify the model.
●	Feature Scaling: The Amount feature was scaled using StandardScaler to normalize the data, ensuring that the model performed optimally by treating all features on the same scale.
●	Encoding Labels: The Is Laundering column was treated as the target variable for training purposes, while other features were used as input features.
 
2.3 Model Selection
We used the One-Class SVM (Support Vector Machine) algorithm for this project. One-Class SVM is particularly suitable for anomaly detection, where the goal is to identify instances that deviate from the normal pattern.
●	One-Class SVM Parameters:
○	nu (0.01): The upper bound on the fraction of margin errors and the lower bound on the fraction of support vectors.
○	kernel ('rbf'): Radial basis function kernel to capture non-linear relationships.
○	gamma ('scale'): The kernel coefficient, where 'scale' is automatically calculated from the input data.
_______________________________________________________________________________________________________________________________________________________
3. Exploratory Data Analysis (EDA)
3.1 Data Overview
We began by examining the dataset to understand its structure and the distribution of features. Key statistics such as the average transaction amount, frequency of different transaction types, and the overall balance between suspicious and non-suspicious transactions were examined.
3.2 Visualizing Transaction Types
The distribution of Suspicious vs Normal transactions was visualized using a count plot, which showed how many transactions were labeled as suspicious compared to normal transactions.
3.3 Money Range Comparison
We used a boxplot to compare the money range for suspicious and normal transactions. This helped us observe if suspicious transactions generally have higher amounts or if they span a different range compared to normal transactions.
3.4 Time-based Analysis
If the Date field was available, we performed a time-series analysis to examine how suspicious transactions evolve over time. This was represented using a wave graph (line chart) to track the count of transactions per day, which helped us identify trends and patterns.
________________________________________________________________________________________________________________________________________________________________
4. Model Training and Evaluation
4.1 Feature Scaling
We scaled the Amount feature using StandardScaler to bring the data into a similar range, ensuring that the SVM model could properly learn from the data.
4.2 Model Training
The One-Class SVM model was trained using the scaled Amount feature. After training, the model was able to predict whether a transaction was Suspicious or Normal. We used a small sample of the dataset to quickly evaluate the model's performance.
4.3 Model Evaluation
Since the dataset used for anomaly detection is highly imbalanced, traditional metrics such as accuracy are not effective. Instead, we focused on the following:
●	Suspicious Transaction Count: The model’s ability to identify suspicious transactions.
●	Transaction Amounts for Suspicious Transactions: The model’s detection of large or unusual transaction amounts.
The trained model was then evaluated by checking how well it detected suspicious transactions based on the Amount feature. 
______________________________________________________________________________________________________________________________________________________________
5. Streamlit Web Application
5.1 Overview
A Streamlit web application was created to allow users to interact with the model. Users can input transaction details, including Sender Account, Receiver Account, and Amount, and the model will predict if the transaction is suspicious or normal.
5.2 User Interface
●	Input Fields: Users can input transaction details (Sender and Receiver accounts, Amount).
●	Prediction Output: The app will predict whether the transaction is Suspicious or Normal, and provide reasons for the suspicion (e.g., abnormal transaction amount).
●	Visualizations: A dashboard with bar charts and wave graphs to compare suspicious and normal transactions, as well as the amount distribution.
________________________________________________________________________________________________________________________________________________________________
6. Results and Conclusion
6.1 Model Results
After training the One-Class SVM, the model was able to detect suspicious transactions based on the transaction amounts. We found that:
●	Suspicious transactions were typically higher in value compared to normal transactions.
●	The model identified a small fraction of transactions as suspicious, which is expected in an imbalanced dataset.
6.2 Summary of Findings
●	Suspicious Transactions Count:  will display Stremlit
●	Normal Transactions Count:  will display Stremlit
●	Total Suspicious Value:  will display Stremlit
●	The model was successful in detecting anomalies in transaction amounts, which likely represent fraudulent or money laundering activities.
6.3 Future Scope
While the One-Class SVM was effective in detecting anomalous transactions based on amounts, the following improvements can be made:
●	Incorporating additional features like geographical locations, time of transaction, and payment types could further enhance the detection capability.
●	Deep learning models such as autoencoders or LSTM (Long Short-Term Memory) networks can be explored for detecting more complex patterns and anomalies.
●	Real-time transaction monitoring systems can be implemented to detect and flag suspicious transactions as they happen.
6.4 Limitations
●	The model relies heavily on the Amount feature, so transactions that do not involve large amounts might be overlooked.
●	A more balanced dataset could help improve the model’s sensitivity and reduce false positives.
___________________________________________________________________________________________________________________________________________________________________

