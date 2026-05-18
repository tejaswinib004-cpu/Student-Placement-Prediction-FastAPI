from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app=FastAPI()

model=joblib.load("placement_model.pkl")

class Student(BaseModel):

    cgpa:float
    iq:int


@app.get("/")
def home():

    return {"message":"Placement Prediction API Running"}


@app.post("/predict")
def predict(data:Student):

    input_data=np.array([[
        data.cgpa,
        data.iq
    ]])

    prediction=model.predict(input_data)

    if prediction[0]==1:
        result="Placed"

    else:
        result="Not Placed"

    return {"Prediction":result}