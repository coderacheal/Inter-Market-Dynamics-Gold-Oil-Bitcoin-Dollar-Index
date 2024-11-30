import streamlit as st
import joblib
import pandas as pd
from src.function import apply_feature_engineering
from src.utils import ratios_dict, rolling_avg_ratios

# Set page configurations
st.set_page_config(
    page_title='Prediction',
    layout='wide',
    page_icon='🤖'
)

# Load pipelines and encoder
st.cache_resource()
def load_forest_pipeline():
    pipeline = joblib.load('./models/random_forest.pkl')
    return pipeline

st.cache_resource()
def load_gradient_pipeline():
    pipeline = joblib.load('./models/gradient_boosting.pkl')
    return pipeline

st.cache_resource()
def load_encoder():
    encoder = joblib.load('./models/encoder.pkl')
    return encoder

def select_model():
    model_name = st.selectbox('Select a Model', options=['Random Forest', 'Gradient Boosting'], key='selected_model')
    if model_name == 'Random Forest':
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_gradient_pipeline()
    encoder = load_encoder()
    return pipeline, encoder

def make_a_prediction(pipeline, encoder):
    # Load the saved data
    saved_file_path = './src/input_data/submitted_data.csv'
    df = pd.read_csv(saved_file_path)

    # Apply feature engineering
    engineered_df = apply_feature_engineering(df)

    # Save engineered data for future use
    engineered_file_path = './src/input_data/engineered_data.csv'
    engineered_df.to_csv(engineered_file_path, index=False)

    # Make prediction
    pred = pipeline.predict(engineered_df)
    prediction = encoder.inverse_transform([int(pred[0])])

    # Get probabilities
    probability = pipeline.predict_proba(engineered_df)

    # Update session state
    st.session_state['prediction'] = prediction[0]
    st.session_state['probability'] = probability[0].tolist()

    return prediction[0], probability[0].tolist()

def display_form(pipeline, encoder):
    with st.form('input-feature'):
        st.write('#### Assets')
        st.number_input('GOLD PRICE ($)', key='gold_close', min_value=100, max_value=100, step=1)
        st.number_input('OIL PRICE ($)', key='oil_close', min_value=80, max_value=200, step=1)
        st.number_input('BITCOIN PRICE ($)', key='btc_close', min_value=10000, max_value=25000, step=1)

        st.write('#### Meta Data')
        st.date_input("Select today's date", key='today_date')
        st.checkbox('Is today a holiday?', key='is_holiday')

        submitted = st.form_submit_button('Calculate Portfolio')

        if submitted:
            # Collect form data
            data = {
                "gold_close": [st.session_state['gold_close']],
                "oil_close": [st.session_state['oil_close']],
                "btc_close": [st.session_state['btc_close']],
                "Date": [st.session_state['today_date']],
                "IS_HOLIDAY": [int(st.session_state['is_holiday'])]
            }

            st.session_state['data'] = data
            df = pd.DataFrame(st.session_state['data'])

            # Feature engineering
            df['Date'] = pd.to_datetime(df['Date'])
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.month
            df['Weekday'] = df['Date'].dt.weekday
            df['IS_WEEKDAY'] = df['Weekday'].apply(lambda x: int(x <= 5))
            df.drop('Date', axis=1, inplace=True)

            # Add ratios
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

            # Save to session and file
            st.session_state['df'] = df
            df.to_csv('./src/input_data/submitted_data.csv', index=False)

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
            st.write(f"##### Prediction: {st.session_state['prediction']}")
        else:
            st.info("Submit the form to see portfolio predictions.")
