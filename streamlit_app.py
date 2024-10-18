import streamlit as st
import pandas as pd

st.image("titanic.jpg")
df = pd.read_csv('titanic_train.csv', delimiter = ',')
st.dataframe(df, use_container_width=True)
