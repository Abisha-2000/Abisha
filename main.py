import pandas as pd
import streamlit as st
import streamlit as st
from textblob import TextBlob
from streamlit_extras.let_it_rain import rain

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
return str_p == str_q
if polarity < 0:
	
	st.warning("The entered text has negative sentiments associated with it"+str(polarity))
	rain(
	emoji="????",
	font_size=20, # the size of emoji
	falling_speed=3, # speed of raining
	animation_length="infinite", # for how much time the animation will happen
)
if polarity >= 0:
	
	st.success("The entered text has positive sentiments associated with it."+str(polarity))
	rain(
	emoji="????",
	font_size=20, # the size of emoji
	falling_speed=3, # speed of raining
	animation_length="infinite", # for how much time the animation will happen
	)
	
st.success(result)
