def apply_feature_engineering(df):
  
    # Define the columns for each asset
    assets = {
        'btc': ['btc_open', 'btc_close', 'btc_high', 'btc_low'],
        'oil': ['oil_open', 'oil_close', 'oil_high', 'oil_low'],
        'gold': ['gold_open', 'gold_close', 'gold_high', 'gold_low'],
        # 'dxy': ['dxy_open', 'dxy_close', 'dxy_high', 'dxy_low']
    }
    
    # Define the price columns for running averages
    price_cols = ['btc_open', 'btc_close', 'oil_open', 'oil_close', 'gold_open', 'gold_close']

    # Calculate running weekly and monthly averages
    for col in price_cols:
        df[f'{col}_weekly_avg'] = df[col].rolling(window=7, min_periods=1).mean()
        df[f'{col}_monthly_avg'] = df[col].rolling(window=30, min_periods=1).mean()
    
    # Calculate daily percentage changes
    for asset, cols in assets.items():
        open_col, close_col, high_col, low_col = cols
        df[f'{asset}_daily_percentage'] = ((df[close_col] - df[open_col]) / df[open_col]) * 100
        df[f'{asset}_daily_max_percentage'] = ((df[high_col] - df[open_col]) / df[open_col]) * 100
        df[f'{asset}_daily_min_percentage'] = ((df[low_col] - df[open_col]) / df[open_col]) * 100
    
    # Calculate intraday volatility
    for asset in assets.keys():
        df[f'{asset}_intraday_volatility'] = ((df[f'{asset}_high'] - df[f'{asset}_low']) / df[f'{asset}_open']) * 100
    
    # # Calculate rolling volatility of daily percentage changes
    # for asset in assets.keys():
    #     # Daily percentage change
    #     df[f'{asset}_daily_pct_change'] = df[f'{asset}_close'].pct_change() * 100
        
    #     # Rolling volatility (standard deviation of daily percentage changes)
    #     df[f'{asset}_rolling_volatility_7'] = df[f'{asset}_daily_pct_change'].rolling(window=7).std()
    #     df[f'{asset}_rolling_volatility_30'] = df[f'{asset}_daily_pct_change'].rolling(window=30).std()

    return df