import streamlit as st
import joblib
import pandas as pd
import os
import datetime


# Set page configurations
st.set_page_config(
    page_title='Prediction',
    layout='wide',
    page_icon='🤖'
)


st.cache_resource()
def load_forest_pipeline():
    # pipeline = joblib.load('./models/forest_pipeline.joblib')
    # return pipeline
    pass


st.cache_resource()
def load_scv_pipeline():
    # pipeline = joblib.load('./models/svc_pipeline.joblib')
    # return pipeline
    pass


st.cache_resource(show_spinner='Models Loading...')
def select_model():
    col1, col2 = st.columns(2)

    with col1:
        st.selectbox('Select a Model', options=['Random Forest', 'SVC'], key='selected_model')
    with col2:
        pass

    # if st.session_state['selected_model'] == 'Random Forest':
    #     pipeline = load_forest_pipeline()
    # else:
    #     pipeline = load_scv_pipeline()

    # encoder = joblib.load('./models/encoder.joblib')

    # return pipeline

st.session_state['data'] = ''


import streamlit as st

def display_form():
    with st.form('input-feature'):
        # Divide form into 2 columns
        # col1, col2 = st.columns(2)

        # with col1:
        st.write('#### Assets')
        st.number_input('GOLD PRICE ($)', key='gold_price', min_value=100, max_value=100, step=1) 
        st.number_input('OIL PRICE ($)', key='oil_price', min_value=80, max_value=200, step=1)
        st.number_input('BITCOIN PRICE ($)', key='bitcoin_price', min_value=10000, max_value=25000, step=1)

        # with col2:
        st.write('#### Meta Data')
        st.date_input("Select today's date", key='today_date')  
        st.checkbox('Is today a holiday?', key='is_holiday')    

        if st.form_submit_button('Submit'):
            st.success('Form submitted successfully!')

        
        # Collect all session state values for the form
        data = {
            "Gold Price ($)": [st.session_state['gold_price']],
            "Oil Price ($)": [st.session_state['oil_price']],
            "Bitcoin Price ($)": [st.session_state['bitcoin_price']],
            "Date": [st.session_state['today_date']],
            "Is Holiday": [st.session_state['is_holiday']]
        }

        st.session_state['data'] = data


        df = pd.DataFrame(st.session_state['data'])

        st.session_state['data'] = df



            
# Run the function to display the form
if __name__ == "__main__":
    st.markdown("### Predict Movement in DXY")

    col1, col2 = st.columns(2)
    
    with col1:
        display_form()
    with col2:
        # Convert to a dataframe

        # Display the dataframe
        st.write("### Submitted Data")
        st.dataframe(st.session_state['df'])


