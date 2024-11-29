import streamlit as st
import joblib
import pandas as pd
import os
from src.function import apply_feature_engineering
from src.ratio_values import ratios_dict, rolling_avg_ratios


# Set page configurations
st.set_page_config(
    page_title='Prediction',
    layout='wide',
    page_icon='🤖'
)


st.cache_resource()
def load_forest_pipeline():
    pipeline = joblib.load('./models/random_forest.pkl')
    return pipeline


st.cache_resource()
def load_gradient_pipeline():
    pipeline = joblib.load('./models/gradient_boosting.pkl')
    return pipeline


st.cache_resource(show_spinner='Models Loading...')
def select_model():
    col1, col2 = st.columns(2)

    with col1:
        st.selectbox('Select a Model', options=['Random Forest', 'Gradient Boosting'], key='selected_model')
    with col2:
        pass

    if st.session_state['selected_model'] == 'Random Forest':
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_gradient_pipeline()

    encoder = joblib.load('./models/encoder.pkl')

    return pipeline, encoder

def make_a_prediction(pipeline, encoder):
    # Load the data saved in the previous step
    saved_file_path = './submitted_data.csv'
    df = pd.read_csv(saved_file_path)

    # Apply the feature engineering function
    engineered_df = apply_feature_engineering(df)

    # Save the engineered DataFrame for future use
    engineered_file_path = './engineered_data.csv'
    engineered_df.to_csv(engineered_file_path, index=False)

    # Load the selected model and encoder
    # pipeline, encoder = select_model()

    # Ensure input columns match the model requirements
    model_input = engineered_df
    try:
        # Make predictions
        predictions = pipeline.predict(model_input)
        # Decode predictions if using an encoder
        decoded_predictions = encoder.inverse_transform(predictions) if encoder else predictions

        # Add predictions to the DataFrame
        engineered_df['Prediction'] = decoded_predictions

        return engineered_df
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return engineered_df


# def make_a_prediction():
#     # Load the data saved in the previous step
#     saved_file_path = './submitted_data.csv'
#     df = pd.read_csv(saved_file_path)

#     # Apply the feature engineering function
#     engineered_df = apply_feature_engineering(df)

#     # Save the engineered DataFrame for future use
#     engineered_file_path = './engineered_data.csv'
#     engineered_df.to_csv(engineered_file_path, index=False)

#     return engineered_df


st.session_state['data'] = ''
st.session_state['df'] = ''


def display_form():
    with st.spinner('Models Loading..'):
        pipeline, encoder = select_model()

    with st.form('input-feature'):

        st.write('#### Assets')
        st.number_input('GOLD PRICE ($)', key='gold_close', min_value=100, max_value=100, step=1)
        st.number_input('OIL PRICE ($)', key='oil_close', min_value=80, max_value=200, step=1)
        st.number_input('BITCOIN PRICE ($)', key='btc_close', min_value=10000, max_value=25000, step=1)

        st.write('#### Meta Data')
        st.date_input("Select today's date", key='today_date')
        st.checkbox('Is today a holiday?', key='is_holiday')

        submitted = st.form_submit_button('Submit')

        if submitted:
            # Collect all session state values for the form
            data = {
                "gold_close": [st.session_state['gold_close']],
                "oil_close": [st.session_state['oil_close']],
                "btc_close": [st.session_state['btc_close']],
                "Date": [st.session_state['today_date']],
                "IS_HOLIDAY": [int(st.session_state['is_holiday'])]  # Convert True/False to 1/0
            }

            st.session_state['data'] = data
            df = pd.DataFrame(st.session_state['data'])

            # Convert 'Date' column to datetime
            df['Date'] = pd.to_datetime(df['Date'])

            # Extract additional date features
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.month
            df['Weekday'] = df['Date'].dt.weekday
            df['IS_WEEKDAY'] = df['Weekday'].apply(lambda x: int(x <= 5))  # Convert True/False to 1/0
            df.drop('Date', axis=1, inplace=True)

            # Add additional features using ratios
            df['btc_open'] = ratios_dict['btc_open_ratio'] * st.session_state['btc_close']
            df['btc_high'] = ratios_dict['btc_high_ratio'] * st.session_state['btc_close']
            df['btc_low'] = ratios_dict['btc_low_ratio'] * st.session_state['btc_close']

            df['gold_open'] = ratios_dict['gold_open_ratio'] * st.session_state['gold_close']
            df['gold_high'] = ratios_dict['gold_high_ratio'] * st.session_state['gold_close']
            df['gold_low'] = ratios_dict['gold_low_ratio'] * st.session_state['gold_close']

            df['oil_open'] = ratios_dict['oil_open_ratio'] * st.session_state['oil_close']
            df['oil_high'] = ratios_dict['oil_high_ratio'] * st.session_state['oil_close']
            df['oil_low'] = ratios_dict['oil_low_ratio'] * st.session_state['oil_close']

            #Rolling Average & Pct Change
            df['btc_daily_pct_change'] = rolling_avg_ratios['btc_daily_pct_change']
            df['btc_rolling_volatility_7'] = rolling_avg_ratios['btc_rolling_volatility_7']
            df['btc_rolling_volatility_30'] = rolling_avg_ratios['btc_rolling_volatility_30']
            df['oil_daily_pct_change'] = rolling_avg_ratios['oil_daily_pct_change']
            df['oil_rolling_volatility_7'] = rolling_avg_ratios['oil_rolling_volatility_7']
            df['oil_rolling_volatility_30'] = rolling_avg_ratios['oil_rolling_volatility_30']
            df['gold_daily_pct_change'] = rolling_avg_ratios['gold_daily_pct_change']
            df['gold_rolling_volatility_7'] = rolling_avg_ratios['gold_rolling_volatility_7']
            df['gold_rolling_volatility_30'] = rolling_avg_ratios['gold_rolling_volatility_30']


            # Save the DataFrame to the session state
            st.session_state['df'] = df

            # Save the DataFrame to a CSV file
            output_path = './submitted_data.csv'
            df.to_csv(output_path, index=False)

            # Call the make_a_prediction function
            engineered_df = make_a_prediction()

            # Display success message and show the engineered data
            # st.success("Feature engineering and prediction pipeline completed.")
            # st.write("### Sample of Engineered Data")
            # st.dataframe(engineered_df)


# Run the function to display the form
if __name__ == "__main__":
    st.markdown("### Predict Movement in DXY")

    col1, col2 = st.columns(2)
    
    with col1:
        select_model()
        display_form()
    with col2:
        # Display the dataframe
        st.write("### Submitted Data")
        # st.dataframe(st.session_state['df'])
        st.write(st.session_state)

    st.write(st.session_state)
    # st.write(st.dataframe(st.session_state['df']))
