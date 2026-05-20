import streamlit as st
import requests

st.title("Student Placement Prediction")

st.write("Enter student details")

cgpa = st.number_input(
    "Enter CGPA",
    min_value=0.0,
    max_value=10.0
)

iq = st.number_input(
    "Enter IQ"
)

if st.button("Predict"):

    data = {
        "cgpa": cgpa,
        "iq": int(iq)
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.success(
        result["Prediction"]
    )