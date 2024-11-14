# knn_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

app = FastAPI()

# Load your dataset and model initialization
df = pd.read_csv('your_dataset.csv')  # Replace with actual dataset file
y = df['price_range']
X = df[['age', 'goals', 'assists', 'yellow cards', 'red cards', 
        'goals conceded', 'clean sheets', 'minutes played', 'days_injured',
        'award', 'highest_value', 'winger'] + [col for col in df.columns if 'team_' in col]]

# Split the data and scale it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Save scaler and model to avoid retraining
joblib.dump(scaler, "scaler.joblib")
joblib.dump(knn, "knn_model.joblib")

# Define request model
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
             request.goals_conceded, request.clean_sheets, request.minutes_played, request.days_injured,
             request.award, request.highest_value, request.winger] + list(request.team_features.values())]

    # Load scaler and model
    scaler = joblib.load("scaler.joblib")
    knn = joblib.load("knn_model.joblib")

    # Scale data and predict
    data_scaled = scaler.transform(data)
    prediction = knn.predict(data_scaled)
    return {"price_range": prediction[0]}
