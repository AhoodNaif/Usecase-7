# Football Prediction Price App

This project is a **Football Prediction Price App** designed to provide predictions based on football player statistics. It consists of two main components:

1. A **FastAPI** backend hosted on Render for API-based predictions.
2. A **Streamlit** frontend app for an interactive user experience.

## Features

- **Prediction Model**: Predicts player-related outcomes using advanced statistical and machine learning techniques.
- **FastAPI Backend**: A RESTful API to access prediction functionalities programmatically.
- **Streamlit Frontend**: A user-friendly interface for non-technical users to interact with the app.
- **Data Visualizations**: Graphical insights into the prediction results.

## Project Structure

```plaintext
.
├── app/                     # Main application folder
│   ├── main.py              # FastAPI application
│   ├── models/              # ML models
│   ├── utils/               # Utility functions
│   └── ...                  # Other backend files
├── streamlit_app/           # Streamlit app folder
│   ├── app.py               # Streamlit frontend
│   ├── assets/              # Frontend assets (images, CSS, etc.)
│   └── ...                  # Other frontend files
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── ...                      # Additional project files

```

## Installation and Usage
**Prerequisites**
Python: Version 3.9 or higher
Pip: Python's package installer
Virtual Environment: Recommended for isolated dependency management

## Steps to Run Locally
**1.Clone the Repository:**
```
git clone <repository_url>
cd <repository_name>
```
**2.Set Up a Virtual Environment:**
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
**3.Install Dependencies:**
```
pip install -r requirements.txt
```
**4.Start the FastAPI Backend:**
```
uvicorn app.main:app --reload
```
**5.Run the Streamlit Frontend:**
```
streamlit run streamlit_app/app.py
```
**6.Access the Apps:**
```
FastAPI: Open http://127.0.0.1:8000/docs in your browser.
Streamlit: Open http://localhost:8501 in your browser.

```
## Live Demo

Explore the app online:

- **FastAPI Backend Documentation**: [FastAPI on Render](https://usecase-7uvicorn-main-app-host-0-0-0-0.onrender.com/docs#/default/predict_predict_post)
- **Streamlit App**: [Streamlit App on Streamlit Cloud](https://football-prediction-price.streamlit.app/)




