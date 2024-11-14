# knn_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib
import os

app = FastAPI()

# Load your dataset and define target and features
dataset_path = "final_data.csv"  # Replace with the actual path to your dataset
if os.path.exists(dataset_path):
    df = pd.read_csv(dataset_path)
else:
    raise FileNotFoundError(f"The dataset file at {dataset_path} was not found.")

# Ensure that df is loaded correctly
y = df['price_range']
X = df[['age', 'goals', 'assists', 'yellow cards', 'red cards', 
        'goals_conceded', 'clean_sheets', 'minutes_played', 'days_injured',
        'award', 'highest_value', 'winger'] + [col for col in df.columns if 'team_' in col]]

# Split the data and scale it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and save KNN model and scaler
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
joblib.dump(scaler, "scaler.joblib")
joblib.dump(knn, "knn_model.joblib")

# Define request model for prediction input
class PredictionRequest(BaseModel):
    age: float
    goals: float
    assists: float
    yellow_cards: float
    red_cards: float
    goals_conceded: float
    clean_sheets: float
    minutes_played: float
    days_injured: float
    award: float
    highest_value: float
    winger: float
    team_features: dict  # For team-related one-hot encoded features

# Prediction endpoint
@app.post("/predict")
def predict_price_range(request: PredictionRequest):
    # Convert request to DataFrame
    data = [[request.age, request.goals, request.assists, request.yellow_cards, request.red_cards,
             request.goals_conceded, request.clean_sheets, request.minutes_played, request.days_injured,]]
       
