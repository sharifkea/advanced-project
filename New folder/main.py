from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib  # or use pickle if you saved with pickle
import numpy as np
import pandas as pd
from typing import Dict, Any

# Initialize FastAPI app
app = FastAPI(title="Cardiovascular Risk Prediction API", description="API for predicting cardiovascular risk using XGBoost model")

# Load the trained model and scaler
# Assuming you saved them as 'xgboost_model.pkl' and 'scaler.pkl' using joblib.dump(model, 'xgboost_model.pkl')
try:
    model = joblib.load('xgboost_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("Model and scaler loaded successfully!")
except FileNotFoundError:
    raise Exception("Model or scaler file not found. Please ensure 'xgboost_model.pkl' and 'scaler.pkl' are in the same directory.")

# Define input schema using Pydantic for validation
class PredictionInput(BaseModel):
    gender: int  # 1: female, 2: male (or as per your encoding)
    height: int  # in cm
    ap_hi: int   # systolic blood pressure
    ap_lo: int   # diastolic blood pressure
    cholesterol: int  # 1: normal, 2: above normal, 3: well above normal
    gluc: int    # 1: normal, 2: above normal, 3: well above normal
    smoke: int   # 0: no, 1: yes
    alco: int    # 0: no, 1: yes
    active: int  # 0: no, 1: yes
    age_years: int  # age in years (engineered from age)
    BMI: float   # body mass index
    BMI_category_num: float  # numerical encoding of BMI category
    weight: float  # in kg

# Define output schema
class PredictionOutput(BaseModel):
    risk_probability: float  # Probability of cardiovascular disease (0-1)
    risk_class: int  # 0: low risk, 1: high risk
    message: str  # Interpretive message

# Prediction endpoint
@app.post("/predict", response_model=PredictionOutput)
async def predict_risk(input_data: PredictionInput):
    try:
        # Convert input to DataFrame for consistency with training
        input_dict = input_data.dict()
        input_df = pd.DataFrame([input_dict])
        
        # Ensure column order matches training (adjust if your feature order differs)
        feature_columns = ['gender', 'height', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 
                           'smoke', 'alco', 'active', 'age_years', 'BMI',]
        input_df = input_df[feature_columns]
        
        # Scale the input features (assuming scaler was fit on these exact features)
        input_scaled = scaler.fit_transform(input_df)
        
        # Make prediction: probability for class 1 (cardio risk)
        prob = model.predict_proba(input_scaled)[0][1]  # [prob_class0, prob_class1]
        pred_class = 1 if prob > 0.5 else 0  # Binary threshold; adjust as needed
        
        # Generate message
        if pred_class == 1:
            message = "High risk of cardiovascular disease detected. Consult a physician immediately."
        else:
            message = "Low risk of cardiovascular disease. Continue monitoring health."
        
        return PredictionOutput(
            risk_probability=round(prob, 4),
            risk_class=pred_class,
            message=message
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": "XGBoost loaded"}

# Run the app with: uvicorn main:app --reload (save this as main.py)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)