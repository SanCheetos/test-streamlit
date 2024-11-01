import streamlit as st
import pandas as pd
import pytest

def calcRelatives(df, isSurvived):
    if (isSurvived == "Мужчина"):
        sex = df[df['Sex'] == "male"]
        
    else:
        sex = df[df['Sex'] == "female"]
    survivedPeople = sex[sex['Survived'] == 1]
    meanRelatives = round((survivedPeople["SibSp"] + survivedPeople["Parch"]).mean(), 2)
    output = []
    output.append(meanRelatives)
    diedPeople = sex[sex['Survived'] == 0]
    meanRelatives = round((diedPeople["SibSp"] + diedPeople["Parch"]).mean(), 2)
    output.append(meanRelatives)
    return output
    
st.image("titanic.jpg")
df = pd.read_csv('titanic_train.csv', delimiter = ',')
st.dataframe(df)
st.title("Подсчет среднего количества родственников, отдельно среди выживших и погибших")
isSurvived = st.radio(
    "Выберите пол",
    ["Мужчина", "Женщина"],
)
output = calcRelatives(df, isSurvived)
st.write("Среднее количество родственников у выживших: " + str(output[0]))
st.write("Среднее количество родственников у погибших: " + str(output[1]))


test1()
def test1():
    dfTest = pd.DataFrame(
        {
            'Sex': ['male', 'female', 'male', 'female'],
            'Survived': [1, 0, 0, 1], 
            'Sibsp': [2, 2, 1, 4], 
            'Parch': [0, 5, 1, 2]
        }
    )
    assert calcRelatives(dfTest, "Мужчина") == [2,2]
  
  
    
