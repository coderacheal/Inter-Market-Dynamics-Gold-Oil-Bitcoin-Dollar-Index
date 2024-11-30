relevant_features = ['btc_intraday_volatility', 'gold_rolling_volatility_30', 'gold_intraday_volatility', 'btc_yesterday_daily_percentage',
                     'oil_yesterday_monthly_avg_pct_change', 'gold_yesterday_daily_percentage', 'oil_rolling_volatility_30', 'gold_yesterday_monthly_avg_pct_change',
                     'oil_yesterday_intraday_volatility', 'gold_daily_percentage', 'Year', 'oil_daily_percentage', 'btc_rolling_volatility_30',
                     'oil_yesterday_daily_percentage', 'gold_yesterday_intraday_volatility', 'btc_rolling_volatility_7', 'btc_yesterday_monthly_avg_pct_change',
                     'is_holiday']

def apply_feature_engineering(df):

    # List of price columns
    # price_cols = ['btc_close', 'oil_close', 'gold_close']

    # Define the price columns for running averages
    price_cols = ['btc_open', 'btc_close', 'oil_open', 'oil_close', 'gold_open', 'gold_close']

    # Calculate running weekly and monthly averages
    for col in price_cols:
        df[f'{col}_weekly_avg'] = df[col].rolling(window=7, min_periods=1).mean()
        df[f'{col}_monthly_avg'] = df[col].rolling(window=30, min_periods=1).mean()
    

    # Calculate running weekly and monthly averages
    for asset in price_cols:
        df[f'{asset}_weekly_avg'] = df[asset].rolling(window=7, min_periods=1).mean()
        df[f'{asset}_monthly_avg'] = df[asset].rolling(window=30, min_periods=1).mean()


    # Calculate rolling avg of daily percentage changes over 7-day and 30-day windows

    for asset in price_cols:
        df[f'{asset}_weekly_avg_pct_change'] = df[f'{asset}_weekly_avg'].pct_change() * 100
        df[f'{asset}_monthly_avg_pct_change'] = df[f'{asset}_monthly_avg'].pct_change() * 100


    # Asset categories and their respective price types
    assets = {
        'btc': ['btc_open', 'btc_close', 'btc_high', 'btc_low'],
        'oil': ['oil_open', 'oil_close', 'oil_high', 'oil_low'],
        'gold': ['gold_open', 'gold_close', 'gold_high', 'gold_low'],
        # 'dxy': ['dxy_open', 'dxy_close', 'dxy_high', 'dxy_low']
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

        # # Calculate yesterday's ocpercentage for each asset
        # df[f'{asset}_yesterday_Daily_ocpercentage'] = df[f'{asset}_daily_percentage'].shift(1)

        # # Calculate yesterday's intraday volatility for each asset
        # df[f'{asset}_yesterday_intraday_volatility'] = df[f'{asset}_intraday_volatility'].shift(1)

        # # Calculate yesterday's daily percentage change for each asset
        # df[f'{asset}_yesterday_daily_percentage'] = df[f'{asset}_daily_percentage'].shift(1)

        # # Calculate yesterday's percent change of weekly and monthly rolling averages for each asset
        # df[f'{asset}_yesterday_weekly_avg_pct_change'] = df[f'{asset}_close_weekly_avg_pct_change'].shift(1)
        # df[f'{asset}_yesterday_monthly_avg_pct_change'] = df[f'{asset}_close_monthly_avg_pct_change'].shift(1)

        # df = df[[relevant_features]]

    return df
