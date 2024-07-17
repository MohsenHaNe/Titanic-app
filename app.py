import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('model.joblib')
st.title('who will survive from Titanic? ')

# inputs --> columns 
columns = [ 'Pclass',  'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']

Pclass = st.selectbox("Choose class", [1,2,3])
Sex = st.select_slider("Whats your gender?", [0,1])
Age = st.slider("Choose age",0,80)
Sibsp = st.slider("Choose siblings",0,8)
Parch = st.slider("Choose parch",0,9)
Fare = st.number_input("Input Fare Price", 0.0,512.3292)
Cabin = st.text_input("Input Cabin",0,185) 
Embarked = st.select_slider("Did they Embark(S:1,C:2,Q:3)?", [0,1,2])


# Perdict
def predict():  
    row = np.array([Pclass,Sex,Age,Sibsp,Parch,Fare,Cabin,Embarked])
    inputs = pd.DataFrame([row], columns = columns)
    prediction = model.predict(inputs)
    if prediction[0] == 1: 
        st.success('Passenger Survived')
    else: 
        st.error('Passenger did not Survive') 

trigger = st.button('Predict', on_click=predict)

