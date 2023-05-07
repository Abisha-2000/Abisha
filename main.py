import streamlit as st
import pandas as pd
import numpy as np

st.write ("Sentiment Analysis")

file = st.file_uploader("Pick a file")

if file is not None:
    df= pd.read_csv(file)
    st.write(df)
    
    column = st.selectbox("Select a column name : ",np.array(df.columns))

    st.write(df[column].describe)
