import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import pickle

model=pickle.load(open('model.pkl','rb'))
df= pd.read_csv("heart_failure_clinical_records_dataset.csv")
st.line_chart(df)
st.bar_chart(df)

st.sidebar.header("les parametres d'entrées")
st.sidebar.write('''
# Application prédiction de crise cardique
Cette Application prédite si le patient aura une crise cardiaque lors des analyses  
Auteur: Parfait Tanoh N'goran
''')


st.title("Application de prédiction :ship:")
age = st.text_input("Entrer l'age", '52') 
anaemia = st.selectbox("Entrer une Valeur", [0,1])
creatinine_phosphokinase  = st.text_input("creatinine_phosphokinase",'582')
diabetes = st.text_input("diabetes",'0')
ejection_fraction = st.text_input("ejection_fraction",'20')
high_blood_pressure = st.text_input("high_blood_pressure",'1')
platelets = st.text_input("Platelets",'265000')
serum_creatinine = st.text_input("serum_creatinine",'1.0') 
serum_sodium = st.text_input("serum_sodium",'130')
sex = st.selectbox("sexe", [0,1]) 
smoking = st.selectbox("Smoking",[0,1])
time = st.text_input(" Time",'8')

def predict():
    data={'age':age,
    'anaemia':anaemia,
    'creatinine_phosphokinase':creatinine_phosphokinase,
    'diabetes':diabetes,
    'ejection_fraction':ejection_fraction,
    'high_blood_pressure':high_blood_pressure,
    'platelets':platelets,
    'serum_creatinine':serum_creatinine,
    'serum_sodium':serum_sodium,
    'sex':sex,
    'smoking':smoking,
    'time':time,
    }
    X = pd.DataFrame(data,index=[0])
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success("Le patient aura une crise Cardiaque:thumbsup:")
    else: 
        st.error("Le patient n'aura pas de crise Cardiaque :thumbsdown:") 

trigger = st.button('Predict', on_click=predict)


