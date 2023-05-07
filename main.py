import streamlit as st
import pandas as pd

st.write ("Sentiment Analysis")

file = st.file_uploader("Pick a file")


df= pd.read_csv(file)

st.dataframe(df)
