import streamlit as st
import requests

# Set up the Streamlit app
st.title("Football Price range Prediction")

# User inputs
age = st.number_input("age", min_value=15, max_value=35, value=30)
assists = st.number_input("assists", min_value=0, max_value=20, value=1)
days_injured = st.number_input("days_injured", min_value=0, max_value=500, value=1)
award = st.selectbox("award", min_value=0, max_value=500, value=1)  
highest_value = st.selectbox("highest_value", min_value=0, max_value=50000000, value=1)  # Add other makes as needed

# Prediction button
if st.button("Predict Price range"):
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
        prediction = response.json()  # Parse JSON response
        # {'Cheap_Price': 0, 'Good_Price': 1, 'High_Price': 2}

        if prediction['pred'] == 0:
            prediction = "Cheap Price"
        elif prediction['pred'] == 1:
            prediction = "Good Price"
        elif prediction['pred'] == 2:
            prediction = "High Price"
            
        st.write(f"Estimated Price: {prediction}")
    except requests.exceptions.RequestException as e:
        st.error("Error requesting prediction from API. Please try again.")
        st.write(e)