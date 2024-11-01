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



def test1():
    dfTest = pd.DataFrame(
        {
            'Sex': ['male', 'male'],
            'Survived': [1, 0], 
            'SibSp': [2, 1], 
            'Parch': [0, 1]
        }
    )
    assert calcRelatives(dfTest, "Мужчина") == [2,2]

def test2():
    dfTest = pd.DataFrame(
        {
            'Sex': ['female', 'female','female', 'female'],
            'Survived': [0, 1, 0, 1], 
            'SibSp': [2, 4, 3, 3], 
            'Parch': [5, 2, 2, 5]
        }
    )
    assert calcRelatives(dfTest, "Женщина") == [7,6]

test1()
test2()
  
  
    
