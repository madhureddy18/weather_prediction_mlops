# Weather Prediction
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

## 🛠️ Tech Stack

**Programming & Libraries**
- Python 3.x  
- pandas, numpy  
- scikit-learn  
- XGBoost (`XGBClassifier`)  
- pickle / joblib (for saving artifacts)

**Web / API**
- Flask (for serving the prediction API and web UI)

**MLOps & DevOps**
- Docker (containerization)  
- Kubernetes (Google Kubernetes Engine - GKE)  
- GitHub Actions (CI/CD pipeline)  
- Google Cloud Platform (GCP)

**Others**
- Jupyter Notebook (experiments & testing)
- Logging & custom exception handling (from `logger.py` and `custom_exception.py`)

# 📊 Dataset & Features  

The project uses **Historical weather** data to predict if it will rain the next day.

1. 🎯 Target Variable
```
RainTomorrow   →   Yes / No
```
2. 📥 Input Features Used
```
[
    'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
    'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
    'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
    'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
    'Temp3pm', 'RainToday', 'Year', 'Month', 'Day'
]
```
These include:

1. Temperature readings

2. Humidity and pressure levels

3. Wind direction & speed

4. Rainfall & evaporation

5. Cloud coverage

6. Date features (Year, Month, Day)

7. RainToday indicator

Your processed dataset and artifacts live inside:
```
artifacts/raw/
artifacts/processed/
artifacts/models/
```

# 📁 Project Folder Structure
The project is organized into clear modules for data processing, model training, artifact storage, logging, UI, and deployment.
```
WEATHER_PREDICTION/
│
├── .github/workflows/
│   └── deploy.yaml               # CI/CD pipeline using GitHub Actions
│
├── artifacts/
│   ├── models/
│   │   └── model.pkl             # Trained XGBoost model
│   ├── processed/
│   │   ├── X_train.pkl
│   │   ├── X_test.pkl
│   │   ├── y_train.pkl
│   │   └── y_test.pkl
│   └── raw/
│       └── data.csv              # Original dataset
│
├── notebook/
│   └── testing.ipynb             # EDA & testing notebook
│
├── src/
│   ├── __init__.py
│   ├── custom_exception.py       # Custom exception class
│   ├── data_processing.py        # Data cleaning, feature engineering
│   ├── logger.py                 # Logging setup
│   └── model_training.py         # ML training pipeline (XGBoost)
│
├── static/                       # Static assets for web UI (CSS/images)
├── templates/                    # HTML templates for prediction UI
│
├── app.py                        # Main application (API + UI)
├── Dockerfile                    # Docker image setup
├── kubernetes-deployment.yaml    # Kubernetes deployment manifest
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation

```

# ▶️ How to Run the Project Locally
Follow these simple steps to run the model and prediction app on your system.
1. 1️⃣ Clone the Repository
```
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

```
2. 2️⃣ Install Dependencies
```
pip install -r requirements.txt

```
3. 3️⃣ Run the Application
```
python app.py

```
# 🔁 CI/CD Pipeline (GitHub Actions → Artifact Registry → GKE)

This project uses a fully automated CI/CD pipeline built with GitHub Actions.
Whenever code is pushed to the main branch, the pipeline automatically:

1. 1️⃣ Builds the Docker image

GitHub Actions builds a fresh Docker image of the application.

2. 2️⃣ Pushes the image to Artifact Registry

The Docker image is pushed to:

```<region>-docker.pkg.dev/<GCP_PROJECT_ID>/<REPO_NAME>/australia-weather:latest```

This is your GCP Artifact Registry repository.

3. 3️⃣ Deploys the new image to GKE

After pushing the image, the pipeline:

1. Connects to your GKE cluster

2. Updates the **kubernetes-deployment.yaml** with the new image

3. Applies it using kubectl apply

. Triggers a rolling update in Kubernetes

This means your application is automatically redeployed on Google Cloud whenever you update your code.

## 📌 GitHub Secrets Required

Your GitHub Actions workflow uses the following secrets:

1. **GCP_PROJECT_ID**

2. **GCP_SA_KEY (Service Account JSON)**

These allow GitHub to authenticate with your GCP account.

## 📁 Workflow File Location

Your CI/CD config is inside:

```.github/workflows/deploy.yaml```

This file contains:

1. Docker build steps

2. Artifact Registry authentication

3. Image push

4. GKE authentication

5. Deployment commands

## 🚀 Final Result

Once CI/CD is set up:

1. Push code → GitHub Actions runs

2. New Docker image → Automatically stored in Artifact Registry

3. GKE → Automatically updated with the new version

4. Your app redeploys with zero manual work

5. This gives you a complete production-style MLOps workflow.

# 🧠 Model Training & Artifacts
The model is trained using XGBoostClassifier, which performs well on tabular weather data.
All steps of the ML pipeline are handled inside your src/ folder.

### ✔️ Data Preprocessing
Performed in:
```src/data_processing.py```
This includes:

1. Handling missing values

2. Encoding categorical features

3. Scaling numerical features (if required)

4. Creating date-based features (Year, Month, Day)

5. Splitting into train/test sets

Processed datasets are stored in:

```artifacts/processed/```

### ✔️ Model Training

Handled in:

```src/model_training.py```

Model workflow:

1. Load processed train data

2. Train XGBoostClassifier

3. Evaluate performance

4. Save trained model

The final model is saved at:

```artifacts/models/model.pkl```

✔️ Predictions

Once deployed, the app loads the trained model from the artifacts/models/ folder and predicts RainTomorrow based on user inputs.

# ✅ Results
1. Accuracy : 0.862 
2. Precision : 0.854
3. Recall : 0.8621
4. F1-Score : 0.8546
   



