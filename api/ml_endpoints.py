from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Define FastAPI app
app = FastAPI()

# Load models and encoders
forest_pipeline = joblib.load('./models/random_forest.joblib')
stacking_pipeline = joblib.load('./models/stacking_classifier.joblib')
encoder = joblib.load('./models/label_encoder.joblib')

# Input data schema
class PredictionInput(BaseModel):
    gold_close: float
    oil_close: float
    btc_close: float
    is_holiday: int
    Year: int
    Month: int
    dxy_open: float
    btc_open: float
    btc_high: float
    btc_low: float
    gold_open: float
    gold_high: float
    gold_low: float
    oil_open: float
    oil_high: float
    oil_low: float

    btc_daily_pct_change: float
    btc_rolling_volatility_7: float
    btc_rolling_volatility_30: float
    oil_daily_pct_change: float
    oil_rolling_volatility_7: float
    oil_rolling_volatility_30: float
    gold_daily_pct_change: float
    gold_rolling_volatility_7: float

    gold_rolling_volatility_30: float
    gold_yesterday_intraday_volatility: float
    oil_yesterday_monthly_avg_pct_change: float
    gold_yesterday_daily_percentage: float
    btc_yesterday_daily_percentage: float
    oil_yesterday_daily_percentage: float

    oil_yesterday_intraday_volatility: float
    gold_yesterday_monthly_avg_pct_change: float
    btc_intraday_volatility: float
    gold_intraday_volatility: float
    oil_intraday_volatility: float

    oil_daily_percentage: float
    btc_yesterday_intraday_volatility: float  
    btc_yesterday_intraday_volatility: float

    btc_daily_percentage: float
    oil_yesterday_weekly_avg_pct_change: float
    btc_yesterday_weekly_avg_pct_change: float
    gold_yesterday_weekly_avg_pct_change: float
    btc_yesterday_monthly_avg_pct_change: float
    gold_daily_percentage: float
    # Add other features as required

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/predict")
async def predict(input_data: PredictionInput, model: str = "Random Forest"):
    # Convert input data to DataFrame
    data_dict = input_data.dict()
    df = pd.DataFrame([data_dict])

    # Select model
    pipeline = forest_pipeline if model == "Random Forest" else stacking_pipeline

    # Make prediction
    pred = pipeline.predict(df)
    prediction = encoder.inverse_transform([int(pred[0])])

    # Get probabilities
    probabilities = pipeline.predict_proba(df)

    return {
        "prediction": prediction[0],
        "probabilities": probabilities[0].tolist()
    }
