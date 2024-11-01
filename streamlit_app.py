import streamlit as st
import pandas as pd


def calcRelatives(df, isSurvived):
    if (isSurvived == "Мужчина"):
        sex = df[df['Sex'] == "male"]
        
    else:
        sex = df[df['Sex'] == "female"]
    survivedPeople = sex[sex['Survived'] == 1]
    meanRelatives = round((survivedPeople["SibSp"] + survivedPeople["Parch"]).mean(), 2)
    st.write("Среднее количество родственников у выживших: " + str(meanRelatives))
    diedPeople = sex[sex['Survived'] == 0]
    meanRelatives = round((diedPeople["SibSp"] + diedPeople["Parch"]).mean(), 2)
    st.write("Среднее количество родственников у погибших: " + str(meanRelatives))
    
st.image("titanic.jpg")
df = pd.read_csv('titanic_train.csv', delimiter = ',')
st.dataframe(df)
st.title("Подсчет среднего количества родственников, отдельно среди выживших и погибших")
isSurvived = st.radio(
    "Выберите пол",
    ["Мужчина", "Женщина"],
)
calcRelatives(df, isSurvived)


    
