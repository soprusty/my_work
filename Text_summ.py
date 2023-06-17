pip3.10 install openai
#pip install openai --user
#pip3 uninstall openai
#pip3 install --upgrade pip
#pip3 install openai

import openai
import streamlit as st

st.header("summrize app")
article_text = st.text_area("Enter text here which you want to summrize")
