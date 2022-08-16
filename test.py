pip install matplotlib.pyplot
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     #bytes_data = uploaded_file.read()
     #st.write("filename:", uploaded_file.name)
     #st.write(bytes_data)
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)



df=pd.DataFrame(pd.read_csv("C:/Users/soprusty/Desktop/UoH_CODE/word_cloud/android-games.csv"))
text = " ".join(cat.split()[1] for cat in df.category)
#text2 = " ".join(cat.split()[1] for cat in df.title)
#st.dataframe(df.category)
st.set_option('deprecation.showPyplotGlobalUse', False)

word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
