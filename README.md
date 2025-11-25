# Australia Weather Prediction
Machine Learning project that predicts whether it will rain tomorrow or not, using historical weather data.

This project builds a complete end-to-end ML pipeline — from data preprocessing, feature engineering, and model training to saving artifacts,
deploying a prediction API, containerizing the app with Docker, and finally deploying it on Google Cloud Platform (GKE) using CI/CD with GitHub Actions

# 🧩 Project Overview

This project predicts RainTomorrow (Yes/No) using Australia’s historical weather data.
It implements a full end-to-end machine learning + MLOps pipeline:

Cleaning and preprocessing raw weather data

Feature engineering (temperature, humidity, wind, pressure, date-based features, etc.)

Training an XGBoostClassifier for high accuracy and robustness

Saving processed train/test splits and the trained model as artifacts

Building a prediction API using Python (Flask/FastAPI)

Containerizing the application with Docker

Automating deployment using GitHub Actions (CI/CD)

Deploying the ML app on Google Kubernetes Engine (GCP GKE)

The goal is to showcase a complete MLOps workflow — from data to deployment — integrating ML, Docker, Kubernetes, cloud deployment, and CI/CD.
