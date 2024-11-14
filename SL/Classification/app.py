import streamlit as st
import requests

# Set up the Streamlit app
st.title("Football Price Range Prediction")

# User inputs
age = st.number_input("Age", min_value=15, max_value=35, value=30)
assists = st.number_input("Assists", min_value=0, max_value=20, value=1)
days_injured = st.number_input("Days Injured", min_value=0, max_value=500, value=1)
award = st.number_input("Awards", min_value=0, max_value=500, value=1)
highest_value = st.number_input("Highest Value", min_value=0, max_value=50000000, value=1)

# Prediction button
if st.button("Predict Price Range"):
    # API request URL
    url = "https://usecase-7uvicorn-main-app-host-0-0-0-0.onrender.com/predict"
    
    # Data for the POST request
    data = {
        "age": age,
        "assists": assists,
        "days_injured": days_injured,
        "award": award,
        "highest_value": highest_value
    }

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for request errors
        
        # Check if 'pred' exists in the response JSON
        if "pred" in response.json():
            prediction = response.json()["pred"]
            
            # Interpret the prediction
            price_range = {0: "Cheap Price", 1: "Good Price", 2: "High Price"}
            st.write(f"Estimated Price: {price_range.get(prediction, 'Unknown Price Range')}")
        else:
            st.error("Prediction not found in API response.")
        
    except requests.exceptions.RequestException as e:
        st.error("Error requesting prediction from API. Please try again.")
        st.write(e)
    except KeyError as e:
        st.error("Unexpected response format.")
        st.write(f"Error: {e}")
