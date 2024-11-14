# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:26:54 2024

@author: ohoud
"""

# streamlit_app.py
import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Load your dataset
df = pd.read_csv('your_dataset.csv')  # Replace with actual dataset file

# Define target and features
y = df['price_range']
X = df[['age', 'goals', 'assists', 'yellow cards', 'red cards', 
        'goals conceded', 'clean sheets', 'minutes played', 'days_injured',
        'award', 'highest_value', 'winger'] + [col for col in df.columns if 'team_' in col]]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Streamlit App Layout
st.title("KNN Classification Model for Price Range Prediction")

# KNN Model Parameters
st.sidebar.header("KNN Model Parameters")
n_neighbors = st.sidebar.slider("Number of Neighbors (k)", 1, 15, 5)
metric = st.sidebar.selectbox("Distance Metric", ["euclidean", "manhattan", "minkowski"])

# Train and Predict
if st.sidebar.button("Train Model"):
    # Initialize and train KNN
    knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric=metric)
    knn.fit(X_train_scaled, y_train)
    
    # Predict and evaluate
    y_pred = knn.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    # Display Results
    st.subheader("Model Performance")
    st.write(f"Accuracy: {accuracy:.2f}")
    st.json(report)
