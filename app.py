import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


#Sets the layout to full width
st.set_page_config(layout= "wide")


#Web App Title
st.title('''
**Exploratory Data Analysis App**''')

# Upload data (CSV File Only)
with st.sidebar.header('Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])


#Pandas-Profiling Report
global df
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info("Awaiting for CSV file to be uploaded.")
