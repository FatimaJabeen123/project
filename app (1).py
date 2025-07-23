import streamlit as st
import pickle
import numpy as np

# Load model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("diabetes Risk Prediction")

# Input fields
Pregnanices = st.number_input("Pregnanices", 0, 17)
Glucose = st.number_input("Gloucose",0,200)
BloodPressure =st.number_input("BloodPressure",0,122)
SkinThickness = st.number_input("SkinThickness", 0, 99)
Insulin = st.number_input("Insulin", 0, 846)
BMI=st.number_input("BMI",0.0,67.1)
DiabetesPedigreeFunction =st.number_input("DiabetesPedigreeFunction",0.078,2.42)
Age = st.number_input("Age",21,81)

# Prediction
features = np.array([[Pregnanices, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,
                      Age]])

if st.button("Predict"):
    result = model.predict(features)
    st.success(f"diabetes: {'Yes (1)' if result[0]==1 else 'No (0)'}")
