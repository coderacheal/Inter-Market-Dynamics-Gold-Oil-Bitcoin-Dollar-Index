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



def display_form():

    # with st.spinner('Models Loading..'):
    #     # pipeline, encoder = select_model()

    with st.form('input-feature'):

        #Divide form into 3 columns
        col1, col2 = st.columns(2)

        with col1:
            st.write('#### Personal Info 👩🏿')
            st.number_input('Enter your age', key='age', min_value=18, max_value=60, step=1)
            st.selectbox('Select your marital status', options=['Single', 'Married', 'Divorced'], key='marital_status')
            st.number_input('What is you distance from home', key='distancefromhome', max_value=25, min_value=1)
            st.number_input('Enter your salary per month', key='monthly_income', min_value=1000, step=100)
            st.number_input('Enter your education in years: (1-High School, 2- College, 3-Bachelor, 4-Master, 5-PhD)', key='education', min_value=1, max_value=5, step=1)
            st.number_input('How many companies have you worked for?', min_value=1, max_value=20, step=1, key='number_of_companies_worked')

        with col2:
            st.write('#### Work Info 💼')
            st.selectbox('Select your department', options=['Sales', 'Research & Development', 'Human Resources'], key='department')
            st.selectbox('Enter what field of Education you have', options=['Life Sciences', 'Other', 'Medical', 'Marketing','Technical Degree','Human Resources'], key='education_field')
            
            st.number_input('Rate your satisfaction with the environement', max_value=4, min_value=1, step=1, key='environment_satisfaction')
            st.number_input('Rate your job satisfaction', max_value=4, min_value=1, step=1, key='job_satisfaction')
            st.number_input('Rate your work-life balance', max_value=4, step=1, key='work_life_balance', min_value=1)
            st.number_input('How many years have you worked in this company', key='years_at_company', min_value=1, step=1)

                
        st.form_submit_button('Submit')



if __name__ == "__main__":
    st.markdown("### Predict Attrition")
    display_form()

  