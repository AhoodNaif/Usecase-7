
        
        
        
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

# Initialize FastAPI app
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

# Define the InputFeatures class for input data validation
class InputFeatures(BaseModel):
    age: int
    goals: int
    goals_conceded: int
    clean_sheets: int
    minutes_played: int
    winger: int
    red_cards: int
    yellow_cards: int
    assists: float
    days_injured: float
    award: float
    highest_value: float

# Preprocessing function
def preprocessing(input_features: InputFeatures):
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

        # Extract values, convert to a list, and reshape into a 2D array
        input_array = list(dict_f.values())
        input_reshaped = [input_array]  # Equivalent to np.array(input_array).reshape(1, -1)

        # Scale the input features
        scaled_features = scaler.transform(input_reshaped)
        return scaled_features
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during preprocessing: {e}")

# Prediction endpoint
@app.post("/predict")
async def predict(input_features: InputFeatures):
    try:
        # Preprocess the input
        data = preprocessing(input_features)

        # Make prediction
        y_pred = model.predict(data)

        # Return the prediction
        return {"pred": y_pred.tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

