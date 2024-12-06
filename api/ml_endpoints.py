from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List

# Define FastAPI app with metadata
app = FastAPI(
    title="Machine Learning API for Financial Prediction",
    description="""
This API provides predictions using two machine learning models:
- **Random Forest**: A robust model for classification.
- **Stacking Classifier**: A more complex ensemble model for improved accuracy.

You can send input features for prediction and get both the predicted class and probabilities for each class.
    """,
    version="1.0.0",
)

# Load models and encoders
forest_pipeline = joblib.load('./models/random_forest.joblib')
stacking_pipeline = joblib.load('./models/stacking_classifier.joblib')
encoder = joblib.load('./models/label_encoder.joblib')

# Define the response model
class PredictionResponse(BaseModel):
    prediction: str
    probabilities: List[float]


# Input data schema
class PredictionInput(BaseModel):
    dxy_open: float = 104.2
    btc_open: float = 34000.0
    btc_high: float = 35500.0
    btc_low: float = 33000.0
    gold_open: float = 1805.0
    gold_high: float = 1810.0
    gold_low: float = 1795.0
    oil_open: float = 71.0
    oil_high: float = 72.0
    oil_low: float = 69.5

    is_holiday: int = 0
    Year: int = 2024
    Month: int = 10

    btc_daily_pct_change: float = 0.05
    btc_rolling_volatility_7: float = 0.000000	
    btc_rolling_volatility_30: float = 1.648916	

    oil_daily_pct_change: float = 0.04
    oil_rolling_volatility_7: float = 1.914805	
    oil_rolling_volatility_30: float = 2.124083	

    gold_daily_pct_change: float = 0.01
    gold_rolling_volatility_7: float = 0.455859	
    gold_rolling_volatility_30: float = 0.604741	

    gold_intraday_volatility: float = 0.692659	
    gold_daily_percentage: float = 1.155735
    gold_yesterday_intraday_volatility: float = 1.130454
    gold_yesterday_daily_percentage: float = 0.468087	
    gold_yesterday_monthly_avg_pct_change: float = 0.131705
    gold_yesterday_weekly_avg_pct_change: float = 0.046791

    btc_intraday_volatility: float = 3.753015
    btc_daily_percentage: float = 0.0	
    btc_yesterday_daily_percentage: float = 0.02
    btc_yesterday_weekly_avg_pct_change: float = 0.000000	
    btc_yesterday_monthly_avg_pct_change: float = 0.097158	
    btc_yesterday_intraday_volatility: float = 3.753015	
    
    oil_intraday_volatility: float = 2.754700	
    oil_daily_percentage: float = 0.03
    oil_yesterday_daily_percentage: float = -0.252300	
    oil_yesterday_intraday_volatility: float = 2.678173
    oil_yesterday_monthly_avg_pct_change: float = -0.024568
    oil_yesterday_weekly_avg_pct_change: float = -0.993142	
    
 


@app.get("/", summary="Welcome to the API")
def home():
    """
    Welcome to the Financial Prediction API! 

    This API provides predictions using our top 2 models after training:
    - **Random Forest**: A robust model for classification.
    - **Stacking Classifier**: A more complex ensemble model for improved accuracy.

    ## Input Variables:
    - **gold_close**: Gold's closing price (float).
    - **oil_close**: Oil's closing price (float).
    - **btc_close**: Bitcoin's closing price (float).
    - **is_holiday**: Whether it's a holiday (0 = No, 1 = Yes) (int).
    - **Year**: Year of the observation (int).
    - **Month**: Month of the observation (int).
    - **dxy_open**: DXY (US Dollar Index) opening price (float).
    - **btc_open**: Bitcoin's opening price (float).
    - **btc_high**: Bitcoin's highest price (float).
    - **btc_low**: Bitcoin's lowest price (float).
    - **gold_open**: Gold's opening price (float).
    - **gold_high**: Gold's highest price (float).
    - **gold_low**: Gold's lowest price (float).
    - **oil_open**: Oil's opening price (float).
    - **oil_high**: Oil's highest price (float).
    - **oil_low**: Oil's lowest price (float).
    - Additional features such as daily percentage changes, rolling volatilities, and intraday volatilities are calculated during prediction using the previous days values (Concept)

    ## Usage:
    - Use `/predict/random_forest` for predictions with the Random Forest model.
    - Use `/predict/stacking_classifier` for predictions with the Stacking Classifier model.
    - Both endpoints return:
      - Predicted class
      - Probabilities for each class
    """
    return {
        "message": "Welcome to the Financial Prediction API! Check /docs for detailed documentation."
    }



@app.post(
    "/predict/random_forest",
    # tags=["Prediction"],
    summary="Predict with Random Forest Model",
    description="""
    Use this endpoint to get predictions using the Random Forest model. 
    This model is robust and suitable for classification tasks.
    """,
    response_model=PredictionResponse
)
async def predict_random_forest(input_data: PredictionInput):
   
    data_dict = input_data.dict()
    df = pd.DataFrame([data_dict])

    # Use Random Forest pipeline
    pred = forest_pipeline.predict(df)
    prediction = encoder.inverse_transform([int(pred[0])])

    # Get probabilities
    probabilities = forest_pipeline.predict_proba(df)

    return {
        "model": "Random Forest",
        "prediction": prediction[0],
        "probabilities": probabilities[0].tolist()
    }


@app.post(
    "/predict/stacking_classifier",
    # tags=["Prediction"],
    summary="Predict with Stacking Classifier Model",
    description="""
    Use this endpoint to get predictions using the Stacking Classifier model.
    This model combines multiple models for improved accuracy.
    """,
    response_model=PredictionResponse
)
async def predict_stacking_classifier(input_data: PredictionInput):

    data_dict = input_data.dict()
    df = pd.DataFrame([data_dict])

    # Use Stacking Classifier pipeline
    pred = stacking_pipeline.predict(df)
    prediction = encoder.inverse_transform([int(pred[0])])

    # Get probabilities
    probabilities = stacking_pipeline.predict_proba(df)

    return {
        "model": "Stacking Classifier",
        "prediction": prediction[0],
        "probabilities": probabilities[0].tolist()
    }
