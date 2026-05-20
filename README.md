# Student Placement Prediction using Logistic Regression, FastAPI and Streamlit

## Project Overview

This project predicts whether a student will be placed based on academic information using a Logistic Regression machine learning model.

The application is built using:

- Logistic Regression for prediction
- FastAPI for backend API
- Streamlit for frontend user interface

Users enter details through Streamlit, data is sent to FastAPI, and the trained model returns placement predictions.

---

## Problem Statement

Educational institutions often need to identify students who are likely to be placed based on academic performance and aptitude factors.

This project builds a machine learning system that predicts placement status and provides a simple user interface for interaction.

---

## Dataset

Features:

- CGPA
- IQ

Target:

- placement

Values:

- 1 → Placed
- 0 → Not Placed

Sample:

| CGPA | IQ | Placement |
|-------|-----|-----------|
| 6.8 | 123 | 1 |
| 5.9 | 106 | 0 |
| 7.4 | 132 | 1 |

---

## Technologies Used

- Python
- Scikit-learn
- Logistic Regression
- FastAPI
- Uvicorn
- Streamlit
- Pandas
- NumPy
- Joblib

---

## Project Structure

```text
Project-2
│
├── README.md
├── requirements.txt
│
├── backend
│   ├── train_model.py
│   ├── app.py
│   ├── placement.csv
│   └── placement_model.pkl
│
└── frontend
    └── app1.py