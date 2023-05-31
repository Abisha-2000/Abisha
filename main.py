import pandas as pd
import streamlit as st
import streamlit as st
from textblob import TextBlob


st.title("SENTIMENTAL ANALYSIS!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

if st.button("Analyze the Sentiment"):
	
blob = TextBlob(Twitter)
result = blob.sentiment
polarity = result.polarity
subjectivity = result.subjectivity


