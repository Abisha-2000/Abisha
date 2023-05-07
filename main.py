import streamlit as st
import pandas as pd
import numpy as np

st.write ("Sentiment Analysis")

file = st.file_uploader("Pick a file")

if file is not None:
    df= pd.read_csv(file)
    st.write(df)


    st.write("The Description of the file selected")
    st.write(df.describe())
    
    column = st.selectbox("Select a column name : ",np.array(df.columns))
    
    st.write("Description of the selected column")
    st.write(df[column].describe())

    if(len(df[column].unique()) < 10):
        st.write("The Unique Values in the selected column")
        st.write(df[column].unique())
