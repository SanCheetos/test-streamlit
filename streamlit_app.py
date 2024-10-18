import streamlit as st
import pandas as pd

st.image("titanic.jpg")
df = pd.read_csv('titanic_train.csv', delimiter = ',')
st.title("Подсчет среднего количества родственников, отдельно среди выживших и погибших")
isSurvived = st.radio(
    "Выберите, у кого считаем",
    ["Выжившие", "Погибшие"],
)

if (isSurvived == "Выжившие"):
    needPeople = df[df['Survived'] == 1]
    relatives = needPeople["SibSp"] + needPeople["Parch"]
    meanRelatives = round(relatives.mean(), 2)
    st.success("Среднее количество родственников: " + str(meanRelatives))
else:
    needPeople = df[df['Survived'] == 0]
    relatives = needPeople["SibSp"] + needPeople["Parch"]
    meanRelatives = round(relatives.mean(), 2)
    st.error("Среднее количество родственников: " + str(meanRelatives))



