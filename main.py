import streamlit as st
import pandas as pd

st.write ("Sentiment Analysis")

file = st.file_uploader("Pick a file")

if file is not None:
    df= pd.read_csv(file)
    st.write(df)

    st.selectbox(df.columns())
