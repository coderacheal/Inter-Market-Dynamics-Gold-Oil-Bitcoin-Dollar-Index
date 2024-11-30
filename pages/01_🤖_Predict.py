import streamlit as st
import joblib
import pandas as pd
from src.function import apply_feature_engineering, calculate_portfolio_weights
from src.utils import ratios_dict, rolling_avg_ratios, yesterday_ratios



# Set page configurations
st.set_page_config(
    page_title='Prediction',
    layout='wide',
    page_icon='🤖'
)

# Load pipelines and encoder
st.cache_resource()
def load_forest_pipeline():
    pipeline = joblib.load('./models/random_forest.joblib')
    print(pipeline)
    return pipeline

st.cache_resource()
def load_gradient_pipeline():
    pipeline = joblib.load('./models/stacking_classifier.joblib')
    # print(pipeline)
    return pipeline

st.cache_resource()
def load_encoder():
    encoder = joblib.load('./models/label_encoder.joblib')
    return encoder

def select_model():
    model_name = st.selectbox('Select a Model', options=['Random Forest', 'Stacking Classifier'], key='selected_model')
    if model_name == 'Random Forest':
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_gradient_pipeline()
    encoder = load_encoder()
    return pipeline, encoder

def make_a_prediction(pipeline, encoder):
    # Load the saved data
    saved_file_path = './src/submitted_data.csv'
    df = pd.read_csv(saved_file_path)

    df = apply_feature_engineering(df)

    # print("Available columns:", df.columns)
    st.session_state['df`'] = df

    # Make prediction
    pred = pipeline.predict(df)
    prediction = encoder.inverse_transform([int(pred[0])])

    # Get probabilities
    probability = pipeline.predict_proba(df)

    # Update session state
    st.session_state['prediction'] = prediction[0]
    # st.session_state['df'] = df
    st.session_state['probability'] = probability[0].tolist()

    return prediction[0], probability[0].tolist()



def display_form(pipeline, encoder):
    with st.form('input-feature'):
        st.write('#### Assets')
        st.number_input('GOLD PRICE ($)', key='gold_close', min_value=1050, max_value=3000, step=10)
        st.number_input('OIL PRICE ($)', key='oil_close', min_value=11, max_value=150, step=10)
        st.number_input('BITCOIN PRICE ($)', key='btc_close', min_value=25000, max_value=90000, step=100)
        st.date_input("Select today's date", key='today_date')
        st.checkbox('Is today a holiday?', key='is_holiday')
        st.write('#### Investment Amount')
        # Ensure investment_amt is initialized as a number
        if 'investment_amt' not in st.session_state:
            st.session_state['investment_amt'] = 1000  # Default value
        st.number_input('Investment Amt ($)', key='investment_amt', min_value=1000, max_value=1000000, step=1000)

        submitted = st.form_submit_button('Calculate Portfolio')
        # submitted = st.form_submit_button('Submit')  # Add the submit button

        if submitted:

            # Collect form data
            data = {
                "gold_close": [st.session_state['gold_close']],
                "oil_close": [st.session_state['oil_close']],
                "btc_close": [st.session_state['btc_close']],
                "Date": [st.session_state['today_date']],
                "is_holiday": [int(st.session_state['is_holiday'])]
            }

            st.session_state['data'] = data
            df = pd.DataFrame(st.session_state['data'])

            # Feature engineering
            df['Date'] = pd.to_datetime(df['Date'])
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.month


            #  Add ratios
            df['btc_open'] = ratios_dict['btc_open_ratio'] * st.session_state['btc_close']
            df['btc_high'] = ratios_dict['btc_high_ratio'] * st.session_state['btc_close']
            df['btc_low'] = ratios_dict['btc_low_ratio'] * st.session_state['btc_close']
            df['gold_open'] = ratios_dict['gold_open_ratio'] * st.session_state['gold_close']
            df['gold_high'] = ratios_dict['gold_high_ratio'] * st.session_state['gold_close']
            df['gold_low'] = ratios_dict['gold_low_ratio'] * st.session_state['gold_close']
            df['oil_open'] = ratios_dict['oil_open_ratio'] * st.session_state['oil_close']
            df['oil_high'] = ratios_dict['oil_high_ratio'] * st.session_state['oil_close']
            df['oil_low'] = ratios_dict['oil_low_ratio'] * st.session_state['oil_close']

            # Rolling average & pct change
            df['btc_daily_pct_change'] = rolling_avg_ratios['btc_daily_pct_change']
            df['btc_rolling_volatility_7'] = rolling_avg_ratios['btc_rolling_volatility_7']
            df['btc_rolling_volatility_30'] = rolling_avg_ratios['btc_rolling_volatility_30']
            df['oil_daily_pct_change'] = rolling_avg_ratios['oil_daily_pct_change']
            df['oil_rolling_volatility_7'] = rolling_avg_ratios['oil_rolling_volatility_7']
            df['oil_rolling_volatility_30'] = rolling_avg_ratios['oil_rolling_volatility_30']
            df['gold_daily_pct_change'] = rolling_avg_ratios['gold_daily_pct_change']
            df['gold_rolling_volatility_7'] = rolling_avg_ratios['gold_rolling_volatility_7']
            df['gold_rolling_volatility_30'] = rolling_avg_ratios['gold_rolling_volatility_30']

            
            df['gold_yesterday_intraday_volatility'] = yesterday_ratios['gold_yesterday_intraday_volatility']
            df['oil_yesterday_monthly_avg_pct_change'] =  yesterday_ratios['oil_yesterday_monthly_avg_pct_change']
            df['gold_yesterday_daily_percentage'] =  yesterday_ratios['gold_yesterday_daily_percentage']
            df['btc_yesterday_daily_percentage'] =  yesterday_ratios['btc_yesterday_daily_percentage']
            df['oil_yesterday_daily_percentage'] =  yesterday_ratios['oil_yesterday_daily_percentage']
            df['oil_yesterday_intraday_volatility'] =  yesterday_ratios['oil_yesterday_intraday_volatility']
            df['gold_yesterday_monthly_avg_pct_change'] =  yesterday_ratios['gold_yesterday_monthly_avg_pct_change']

            #  Add ratios
            df['btc_intraday_volatility'] = ratios_dict['btc_intraday_volatility'] 
            df['gold_intraday_volatility'] = ratios_dict['gold_intraday_volatility'] 
            df['oil_intraday_volatility'] = ratios_dict['oil_intraday_volatility'] 

            # Drop unneeded columns
            df.drop(['Date'], axis=1, inplace=True)


            # Save to session and file
            st.session_state['df'] = df
            df.to_csv('./src/submitted_data.csv', index=False)

            # Make prediction
            prediction, probability = make_a_prediction(pipeline, encoder)

            return prediction, probability


# Main script
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'probability' not in st.session_state:
    st.session_state['probability'] = None

if __name__ == "__main__":
    st.markdown("### Portfolio Management - Movement in DXY")

    col1, col2 = st.columns(2)

    with col1:
        pipeline, encoder = select_model()
        display_form(pipeline, encoder)

    with col2:
        # Show predictions only if a form is submitted and prediction exists
        if st.session_state['prediction'] is not None:
            st.success("Prediction completed!")
            st.write(st.session_state['df'])
            st.write(f"##### Movement in DXY: {st.session_state['prediction']}")
            
            # Step 1: Predict DXY Movement
            dxy_prediction = st.session_state['prediction']

            portfolio_weights = calculate_portfolio_weights(st.session_state['df'], dxy_prediction, st.session_state['investment_amt'])
            # st.write(portfolio_weights)
        
            st.write((portfolio_weights["Explanation"]))
            st.write("##### Investment Allocation (USD):")
            for asset, allocation in portfolio_weights["Investment Allocation"].items():
                st.write(f"- {asset}: ${allocation}")
                    # st.write(f"##### Prediction: {st.session_state['probability']}")

            st.write("##### Investment Weights")
            for asset, weight in portfolio_weights["Weights"].items():
                st.write(f"- {asset}: {round(weight, 2) * 100}%")

            st.write("##### Sharpe Ratios (Higher = Better Risk-Adjusted Returns):")
            for asset, sharpe in portfolio_weights["Sharpe Ratios"].items():
                st.write(f"- {asset}: {sharpe}")

        else:
            st.info("Submit the form to see portfolio predictions.")
