# Student Placement Prediction Frontend

## Project Overview

This project is the frontend interface for Student Placement Prediction using Streamlit.

Users can enter student details and receive placement predictions through a FastAPI backend connected to a Logistic Regression model.

## Technologies Used

- Python
- Streamlit
- Requests
- FastAPI (Backend API)

## Input Features

- CGPA
- IQ

## Workflow

1. User enters CGPA and IQ
2. Streamlit sends data to FastAPI
3. FastAPI loads trained model
4. Logistic Regression predicts placement
5. Result displayed on screen

## Project Structure

frontend/
│
├── app.py
├── requirements.txt
└── README.md

## Run Project

Install dependencies:

```bash
pip install -r requirements.txt