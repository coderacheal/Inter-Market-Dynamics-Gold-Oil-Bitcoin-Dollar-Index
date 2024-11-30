relevant_features = ['btc_intraday_volatility', 'gold_rolling_volatility_30', 'gold_intraday_volatility',               'btc_yesterday_daily_percentage',
                     'oil_yesterday_monthly_avg_pct_change', 'gold_yesterday_daily_percentage', 'oil_rolling_volatility_30', 'gold_yesterday_monthly_avg_pct_change',
                     'oil_yesterday_intraday_volatility', 'gold_daily_percentage', 'Year', 'oil_daily_percentage', 'btc_rolling_volatility_30',
                     'oil_yesterday_daily_percentage', 'gold_yesterday_intraday_volatility', 'btc_rolling_volatility_7', 'btc_yesterday_monthly_avg_pct_change',
                     'is_holiday']

ratios_dict = {
    'btc_open_ratio': 0.9992841516093321,
    'btc_high_ratio': 1.0209240906816377,
    'btc_low_ratio': 0.9768006364434711,
    'gold_open_ratio': 1.0001144285525523,
    'gold_high_ratio': 1.006529422016887,
    'gold_low_ratio': 0.9935473402081573,
    'oil_open_ratio': 1.0010156851006673,
    'oil_high_ratio': 1.0179860364714555,
    'oil_low_ratio': 0.9824473583988186,
}

rolling_avg_ratios = {
    'btc_daily_pct_change': -0.0787452711656591,
    'btc_rolling_volatility_7': 3.083857647129608,
    'btc_rolling_volatility_30': 3.3424192562837685,
    'oil_daily_pct_change': 0.03858288777250957,
    'oil_rolling_volatility_7': 1.9349087273098502,
    'oil_rolling_volatility_30': 2.0762949295443183,
    'gold_daily_pct_change': -0.020424522246674473,
    'gold_rolling_volatility_7': 0.6872577842576097,
    'gold_rolling_volatility_30': 0.7306986805336596
}

yesterday_ratios = {'btc_yesterday_Daily_ocpercentage': 0.213,
 'btc_yesterday_intraday_volatility': 4.411,
 'btc_yesterday_daily_percentage': 0.213,
 'btc_yesterday_weekly_avg_pct_change': 0.156,
 'btc_yesterday_monthly_avg_pct_change': 0.148,
 'oil_yesterday_Daily_ocpercentage': 0.027,
 'oil_yesterday_intraday_volatility': 3.531,
 'oil_yesterday_daily_percentage': 0.027,
 'oil_yesterday_weekly_avg_pct_change': -0.0,
 'oil_yesterday_monthly_avg_pct_change': -0.002,
 'gold_yesterday_Daily_ocpercentage': 0.026,
 'gold_yesterday_intraday_volatility': 1.304,
 'gold_yesterday_daily_percentage': 0.026,
 'gold_yesterday_weekly_avg_pct_change': 0.024,
 'gold_yesterday_monthly_avg_pct_change': 0.023
 
 }

about = """
### About
This project investigates the inter-market dynamics between gold, crude oil, and Bitcoin, examining their collective influence on the U.S. Dollar Index (DXY). Using daily price data spanning the past decade (2014–2024), the study seeks to uncover critical patterns and dependencies among these assets and to construct a predictive model for the dollar index. 

### Key Features
- **Predict movement in the in the dollar price index**
- **Calculate the weight of every commodity in a portfolio**
- **Save portfolio Information**

### User Benefits
- **Data-driven Decisions:** Make informed decisions backed by data analytics.
- **Easy Machine Learning:** Utilize powerful machine learning algorithms effortlessly.

"""


