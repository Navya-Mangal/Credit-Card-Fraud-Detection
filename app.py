import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(
    open('fraud_detection_model_new.pkl', 'rb')
)

# Title
st.title("💳 Credit Card Fraud Detection")

st.write("Enter the transaction details below.")

# User Inputs
time = st.number_input("Time", min_value=0.0)
amount = st.number_input("Amount", min_value=0.0)

v14 = st.number_input("V14")
v17 = st.number_input("V17")
v10 = st.number_input("V10")
v12 = st.number_input("V12")

st.info(
    "Note: V14, V17, V10 and V12 are PCA-transformed features. "
    "This application is for educational purposes."
)
# Prediction Button
if st.button("Predict"):

    input_data = [[
        time,
        amount,
        v14,
        v17,
        v10,
        v12
    ]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraud Transaction Detected")
    else:
        st.success("✅ Genuine Transaction")