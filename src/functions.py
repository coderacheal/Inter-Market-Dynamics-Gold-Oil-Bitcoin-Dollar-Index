import pandas as pd
import random

'''
yesterday_ratios = {'btc_yesterday_Daily_ocpercentage': 0.002,
 'btc_yesterday_intraday_volatility': 4.452,
 'btc_yesterday_daily_percentage': 0.012,
 'btc_yesterday_weekly_avg_pct_change': 0.0004,
 'btc_yesterday_monthly_avg_pct_change': 0.41,
 'oil_yesterday_Daily_ocpercentage': 0.045,
 'oil_yesterday_intraday_volatility': 3.77,
 'oil_yesterday_daily_percentage': 0.027,
 'oil_yesterday_weekly_avg_pct_change': -0.0,
 'oil_yesterday_monthly_avg_pct_change': -0.00008,
 'gold_yesterday_Daily_ocpercentage': 0.25,
 'gold_yesterday_intraday_volatility': 1.007,
 'gold_yesterday_daily_percentage': 0.7852,
 'gold_yesterday_weekly_avg_pct_change': 0.245,
 'gold_yesterday_monthly_avg_pct_change': 0.1425
 }
'''

def randomize_yesterday_ratios():
    # Original values
    yesterday_ratios = {
        'btc_yesterday_Daily_ocpercentage': 0.213,
        'btc_yesterday_intraday_volatility': 4.411,
        'btc_yesterday_daily_percentage': 0.213,
        'btc_yesterday_weekly_avg_pct_change': 0.156,
        'btc_yesterday_monthly_avg_pct_change': 0.148,
        'oil_yesterday_Daily_ocpercentage': 0.027,
        'oil_yesterday_intraday_volatility': 3.531,
        'oil_yesterday_daily_percentage': 0.027,
        'oil_yesterday_weekly_avg_pct_change': 0.0,
        'oil_yesterday_monthly_avg_pct_change': -0.002,
        'gold_yesterday_Daily_ocpercentage': 0.026,
        'gold_yesterday_intraday_volatility': 1.304,
        'gold_yesterday_daily_percentage': 0.26,
        'gold_yesterday_weekly_avg_pct_change': 0.24,
        'gold_yesterday_monthly_avg_pct_change': 0.23
    }

    randomized_values = list(yesterday_ratios.values())
    random.shuffle(randomized_values)

    # Create a new dictionary with randomized values
    randomized_ratios = dict(zip(yesterday_ratios.keys(), randomized_values))

    return randomized_ratios




# Generate the randomized values
yesterday_ratios = randomize_yesterday_ratios()

relevant_features = ['btc_intraday_volatility', 'gold_rolling_volatility_30', 'gold_intraday_volatility', 'btc_yesterday_daily_percentage',
                     'oil_yesterday_monthly_avg_pct_change', 'gold_yesterday_daily_percentage', 'oil_rolling_volatility_30', 'gold_yesterday_monthly_avg_pct_change',
                     'oil_yesterday_intraday_volatility', 'gold_daily_percentage', 'Year', 'oil_daily_percentage', 'btc_rolling_volatility_30',
                     'oil_yesterday_daily_percentage', 'gold_yesterday_intraday_volatility', 'btc_rolling_volatility_7', 'btc_yesterday_monthly_avg_pct_change',
                     'is_holiday']

# Original values
returns = {
    'btc_annualized_return': -0.1961,
    'gold_annualized_return': -0.0503,
    'oil_annualized_return': 0.0856,
    'btc_monthly_return': -0.7186,
    'gold_monthly_return': -0.1747,
    'oil_monthly_return': 0.0165,
    'btc_quarterly_return': -0.9965,
    'gold_quarterly_return': -0.5572,
    'oil_quarterly_return': -0.1052
}

# Set ranges for randomization (you can adjust these as needed)
ranges = {
    'btc_annualized_return': (-0.5, 0.5),
    'gold_annualized_return': (-0.2, 0.2),
    'oil_annualized_return': (-0.4, 0.4),
    'btc_monthly_return': (-0.5, 0.5),
    'gold_monthly_return': (-0.3, 0.3),
    'oil_monthly_return': (-0.2, 0.2),
    'btc_quarterly_return': (-1, 0.3),
    'gold_quarterly_return': (-0.6, 0.2),
    'oil_quarterly_return': (-0.3, 0.3)
}
randomized_returns = {key: random.uniform(*ranges[key]) for key in ranges}
# Randomize the values based on specified ranges
btc_annualized_return = randomized_returns['btc_annualized_return']
gold_annualized_return = randomized_returns['gold_annualized_return']
oil_annualized_return = randomized_returns['oil_annualized_return']

def apply_feature_engineering(df):

    # Define the price columns for running averages
    price_cols = ['btc_open', 'btc_close', 'oil_open', 'oil_close', 'gold_open', 'gold_close']

    # Calculate running weekly and monthly averages
    for col in price_cols:
        df[f'{col}_weekly_avg'] = df[col].rolling(window=7, min_periods=1).mean()
        df[f'{col}_monthly_avg'] = df[col].rolling(window=30, min_periods=1).mean()

    # Asset categories and their respective price types
    assets = {
        'btc': ['btc_open', 'btc_close', 'btc_high', 'btc_low'],
        'oil': ['oil_open', 'oil_close', 'oil_high', 'oil_low'],
        'gold': ['gold_open', 'gold_close', 'gold_high', 'gold_low'],
    }

    # Calculate daily percentage changes
    for asset, cols in assets.items():
        open_col, close_col, high_col, low_col = cols
        df[f'{asset}_Daily_ocpercentage'] = ((df[close_col] - df[open_col]) / df[open_col] * 100)
        df[f'{asset}_Daily_max_percentage'] = ((df[high_col] - df[open_col]) / df[open_col] * 100)
        df[f'{asset}_Daily_min_percentage'] = ((df[low_col] - df[open_col]) / df[open_col] * 100)

        # Calculate intraday volatility as the percentage difference between high and low prices
        df[f'{asset}_intraday_volatility'] = ((df[f'{asset}_high'] - df[f'{asset}_low']) / df[f'{asset}_close']) * 100

        # Calculate rolling volatility of daily percentage changes over 7-day and 30-day windows
        df[f'{asset}_daily_percentage'] = df[f'{asset}_close'].pct_change() * 100

        # Calculate rolling volatilities
        df[f'{asset}_rolling_volatility_7'] = df[f'{asset}_daily_percentage'].rolling(window=7).std()
        df[f'{asset}_rolling_volatility_30'] = df[f'{asset}_daily_percentage'].rolling(window=30).std()

    # Add yesterday's ratios
    df['btc_yesterday_intraday_volatility'] = yesterday_ratios['btc_yesterday_intraday_volatility']
    df['btc_yesterday_weekly_avg_pct_change'] = yesterday_ratios['btc_yesterday_weekly_avg_pct_change']
    df['btc_yesterday_monthly_avg_pct_change'] = yesterday_ratios['btc_yesterday_monthly_avg_pct_change']
    df['btc_yesterday_daily_percentage'] = yesterday_ratios['btc_yesterday_daily_percentage']

    df['oil_yesterday_intraday_volatility'] = yesterday_ratios['oil_yesterday_intraday_volatility']
    df['oil_yesterday_weekly_avg_pct_change'] = yesterday_ratios['oil_yesterday_weekly_avg_pct_change']
    df['oil_yesterday_monthly_avg_pct_change'] = yesterday_ratios['oil_yesterday_monthly_avg_pct_change']
    df['oil_yesterday_daily_percentage'] = yesterday_ratios['oil_yesterday_daily_percentage']

    df['gold_yesterday_intraday_volatility'] = yesterday_ratios['gold_yesterday_intraday_volatility']
    df['gold_yesterday_weekly_avg_pct_change'] = yesterday_ratios['gold_yesterday_weekly_avg_pct_change']
    df['gold_yesterday_monthly_avg_pct_change'] = yesterday_ratios['gold_yesterday_monthly_avg_pct_change']
    df['gold_yesterday_daily_percentage'] = yesterday_ratios['gold_yesterday_daily_percentage']

    return df

def calculate_portfolio_weights(df, predicted_movement, investment_amount):

    # Set expected returns based on hardcoded values
    btc_expected_return = btc_annualized_return
    gold_expected_return = gold_annualized_return
    oil_expected_return = oil_annualized_return

    # Risk-free rate (market neutral: 2%)
    risk_free_rate = 0.02

    # Extract intraday volatilities for the specified date
    btc_volatility = df.get('btc_intraday_volatility', pd.Series([None][0]))
    gold_volatility = df.get('gold_intraday_volatility', pd.Series([None][0]))
    oil_volatility = df.get('oil_intraday_volatility', pd.Series([None][0]))
    
    # Check for missing data in volatilities
    if pd.isna(btc_volatility).any() or pd.isna(gold_volatility).any() or pd.isna(oil_volatility).any():
        raise ValueError("Missing volatility values. Ensure all required features are present.")

    # Calculate Sharpe Ratios
    sharpe_ratios = {
        "Bitcoin": abs((btc_expected_return - risk_free_rate) / btc_volatility),
        "Gold": abs((gold_expected_return - risk_free_rate) / gold_volatility),
        "Oil": abs((oil_expected_return - risk_free_rate) / oil_volatility),
    }

    # Normalize Sharpe Ratios to derive weights
    total_sharpe = sum(sharpe_ratios.values())
    weights = {asset: sharpe / total_sharpe for asset, sharpe in sharpe_ratios.items()}

    # Adjust weights based on predicted movement
    if predicted_movement == "Positive":
        strategy = "Maximizing Returns"
        explanation = "Allocating more to assets with higher Sharpe ratios to maximize risk-adjusted returns."
    elif predicted_movement == "Negative":
        strategy = "Minimizing Risk"
        explanation = "Allocating based on inverse volatilities to prioritize lower-risk assets."
        weights = {asset: 1 / vol for asset, vol in zip(weights.keys(), [btc_volatility, gold_volatility, oil_volatility])}
        total_inverse_vol = sum(weights.values())
        weights = {asset: weight / total_inverse_vol for asset, weight in weights.items()}
    elif predicted_movement == "Stable":
        strategy = "Equal Weighting"
        explanation = "Allocating equally across all assets for balanced exposure."
        num_assets = len(weights)
        weights = {asset: 1 / num_assets for asset in weights}

    # Calculate investment allocation
    investment_allocation = {asset: weight * investment_amount for asset, weight in weights.items()}

    return {
        "Strategy": strategy,
        "Explanation": explanation,
        "Sharpe Ratios": sharpe_ratios,
        "Weights": weights,
        "Investment Allocation": investment_allocation,
    }