# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:43:56 2024

@author: ohoud
"""

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return "Welcome To Tuwaiq Academy Ahood"

import joblib
model = joblib.load(r"SL/Classification/knn_model.joblib")
scaler = joblib.load(r"SL/Classification/scaler.joblib")

from pydantic import BaseModel
 # Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    age: int
    assists: float
    days_injured: float
    award: float
    highest_value: float
    
    
    
def preprocessing(input_features: InputFeatures):
    dict_f = {
            'age': input_features.age,
            'assists': input_features.assists, 
            'days_injured': input_features.days_injured, 
            'award': input_features.award,
            'highest_value': input_features.highest_value,
            
        }
    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]
    
    # Scale the input features
    scaled_features = scaler.transform([list(dict_f.values
 ())])
    return scaled_features


# get request
@app.get("/items/")
def create_item(item: dict):
    return {"item": item}

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}