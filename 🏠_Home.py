import streamlit as st
import yaml
from yaml.loader import SafeLoader


st.set_page_config(
    page_title='About',
    layout='wide',
    page_icon='🏠'
)



col1, col2 = st.columns(2)
with col1:
    pass
    # column_1
with col2:
    st.write('### How to run application')
    st.code('''
    #activate virtual environment
    env/scripts/activate
    streamlit run 1_🏠_Home.py
    ''')
    # column_2
    st.link_button('Repository on GitHub', url='https://github.com/coderacheal/Inter-Market-Dynamics-Gold-Oil-Bitcoin-Dollar-Index', type='primary')


