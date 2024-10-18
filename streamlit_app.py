import streamlit as st
import pandas as pd

st.image("titanic.jpg")
df = pd.read_csv('titanic_train.csv', delimiter = ',')
st.title("Подсчет среднего количества родственников, отдельно среди выживших и погибших")
genre = st.radio(
    "Выберите, у кого считаем",
    ["Выжившие", "Погибшие"],
)





st.dataframe(df, use_container_width=True)
