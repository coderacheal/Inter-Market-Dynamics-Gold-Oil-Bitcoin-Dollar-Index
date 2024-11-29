import streamlit as st
import yaml
from yaml.loader import SafeLoader
from utils import about


st.set_page_config(
    page_title='About',
    layout='wide',
    page_icon='🏠'
)


st.title('Risk Portfolio Management')
st.write(about)
st.write('### Documentation')
st.link_button('Repository on GitHub', url='https://github.com/coderacheal/Inter-Market-Dynamics-Gold-Oil-Bitcoin-Dollar-Index', type='primary')


