import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load pre-trained One-Class SVM model and scaler
try:
    one_class_svm = joblib.load('one_class_svm_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")
    st.stop()

# Load the dataset (replace 'transactions.csv' with your actual dataset path)
df = pd.read_csv(r"C:/Users/arunr/OneDrive/Desktop/ML Mini Project/Data sets.csv")

# Streamlit UI elements
st.title('Suspicious Transaction Detection')

# Predict status for all transactions in the dataset
df['scaled_amount'] = scaler.transform(df[['Amount']])
df['is_suspicious'] = one_class_svm.predict(df[['scaled_amount']])

# Map the prediction to 'Suspicious' or 'Normal'
df['is_suspicious'] = df['is_suspicious'].map({-1: 'Suspicious', 1: 'Normal'})

# Count the number of Suspicious and Normal transactions
suspicious_count = df[df['is_suspicious'] == 'Suspicious'].shape[0]
normal_count = df[df['is_suspicious'] == 'Normal'].shape[0]
total_transactions = suspicious_count + normal_count

# Suspicious count and total value (sum)
suspicious_value = df[df['is_suspicious'] == 'Suspicious']['Amount'].sum()

# Display the counts and suspicious value
st.write(f"### Total Transactions: {total_transactions}")
st.write(f"### Suspicious Transactions: {suspicious_count}")
st.write(f"### Normal Transactions: {normal_count}")
st.write(f"### Total Suspicious Value: ${suspicious_value:.2f}")

# Display the suspicious transactions
suspicious_transactions = df[df['is_suspicious'] == 'Suspicious']
st.write("### Suspicious Transactions:")
st.dataframe(suspicious_transactions[['Sender_account', 'Receiver_account', 'Amount', 'is_suspicious']])

# Display reason for suspicion (anomaly in transaction amount)
st.write("### Reason for Suspicion:")
st.write("Anomaly detected in the transaction amount")

# Comparison bar graph (Suspicious vs Normal transactions)
st.write("### Suspicious vs Normal Transactions Comparison")

# Plot a bar graph for suspicious vs normal transaction count
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='is_suspicious', data=df, palette='Set2', ax=ax)
ax.set_title('Suspicious vs Normal Transactions')
ax.set_xlabel('Transaction Status')
ax.set_ylabel('Transaction Count')
st.pyplot(fig)

# Money Range Comparison Bar Graph
st.write("### Money Range Comparison: Suspicious vs Normal Transactions")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='is_suspicious', y='Amount', data=df, palette='Set2', ax=ax)
ax.set_title('Money Range Comparison: Suspicious vs Normal Transactions')
ax.set_xlabel('Transaction Status')
ax.set_ylabel('Transaction Amount')
st.pyplot(fig)

# Wave Graph (Time-based count of transactions)
st.write("### Time-based Transaction Count (Wave Graph)")
# Assuming 'Date' or 'Time' column exists for time-based comparison
if 'Date' in df.columns:
    # Convert Date to datetime if not already
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Group by date to get count of transactions per day
    daily_counts = df.groupby(df['Date'].dt.date).size()

    # Plot the wave graph (line graph)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(daily_counts.index, daily_counts.values, marker='o', linestyle='-', color='b')
    ax.set_title('Daily Transaction Count (Wave Graph)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Transaction Count')
    st.pyplot(fig)

else:
    st.write("### Date column not found for the wave graph analysis.")
