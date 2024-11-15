# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:43:56 2024

@author: Ahood
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI()

try:
    # Load model and scaler
    model = joblib.load(r"knn_model.joblib")
    scaler = joblib.load(r"scaler.joblib")
except Exception as e:
    raise RuntimeError(f"Error loading model or scaler: {e}")

@app.get("/")
def root():
    return "Welcome To Tuwaiq Academy Ahood"

# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    age: int
    assists: float
    days_injured: float
    award: float
    highest_value: float

def preprocessing(input_features):
    try:
        # Convert input features to a dictionary
        dict_f = {
            'age': input_features.age,
            'goals': input_features.goals,
            'goals conceded': input_features.goals_conceded,
            'clean sheets': input_features.clean_sheets,
            'minutes played': input_features.minutes_played,
            'days_injured': input_features.days_injured,
            'award': input_features.award,
            'highest_value': input_features.highest_value,
            'winger': input_features.winger,
            'assists': input_features.assists,
            'red cards': input_features.red_cards,
            'yellow cards': input_features.yellow_cards
        }
        return dict_f
    except AttributeError as e:
        print(f"An error occurred: {e}")

        
        # Scale the input features
        scaled_features = scaler.transform([list(dict_f.values())])
        return scaled_features
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during preprocessing: {e}")

@app.post("/predict")
async def predict(input_features: InputFeatures):
    try:
        data = preprocessing(input_features)
        y_pred = model.predict(data)
        return {"pred": y_pred.tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
