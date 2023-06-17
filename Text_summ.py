pip install openai


import openai
import streamlit as st

st.header("summrize app")
article_text = st.text_area("Enter text here which you want to summrize")
