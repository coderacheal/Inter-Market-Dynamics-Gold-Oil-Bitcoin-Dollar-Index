import streamlit as st
import pandas as pd
# Set page configurations
st.set_page_config(
    page_title='Model Features',
    layout='wide',
    page_icon='📈'
)

# Path to the engineered data file
engineered_file_path = './src/input_data/engineered_data.csv'

# Load and display the data
st.markdown("## Data Preview")
# try:
    # Read the CSV file
engineered_df = pd.read_csv(engineered_file_path)
st.dataframe(engineered_df)

