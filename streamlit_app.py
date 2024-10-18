import streamlit as st
import pandas as pd

st.image("titanic.jpg")
df = pd.read_csv('titanic_train.csv', delimiter = ',')
st.title("Подсчет среднего количества родственников, отдельно среди выживших и погибших")
isSurvived = st.radio(
    "Выберите, у кого считаем",
    ["Выжившие", "Погибшие"],
)

if st.button("Рассчитать"):
    if (isSurvived == "Выжившие"):
        needPeople = df[df['Survived'] == 1]
    else:
        needPeople = df[df['Survived'] == 0]
    st.dataframe(df["SibSp"] + df["Parch"])
    st.dataframe(needPeople)
    st.write(df["SibSp"].sum() + df["Parch"].sum())
    st.write((df["SibSp"] + df["Parch"]).sum())

