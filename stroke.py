# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 22:07:59 2021

@author: vishw
"""

import pickle
import streamlit as st

from PIL import image

pickle_in=open('randomforest.pkl','rb')
bc=pickle.load(pickle_in)

def welcome():
    return 'Welcome to Stroke prediction'

def predict_stroke(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status):
    """ We will predict here if you will get a heart disease or not.
    work
    ---
    
    parameters:
      - name: gender
        in: query
        type: number
        required: true
      - name: age
        in: query
        type: number
        required: true
      - name: hypertension
        in: query
        type: number
        required: true
      - name: heart_disease
        in: query
        type: number
        required: true
      - name: ever_married
        in: query
        type: number
        required: true
      - name: work_type
        in: query
        type: number
        required: true
      - name: Residence_type
        in: query
        type: number
        required: true
      - name: avg_glucose_level
        in: query
        type: number
        required: true
      - name: bmi
        in: query
        type: number
        required: true
      - name: smoking_status
        in: query
        type: number
        required: true
     
    responses:
        200:
            description: The output values
            
    """
    prediction=bc.pre([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
    print(prediction)
    return prediction


def main():
    st.title('Stroke Prediction')
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Stroke Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gender =  st.selectbox('Male(1)/ Female(0)', [1,0])
    age =  st.text_input('Age','Type here')
    hypertension =  st.selectbox('Yes(1)/ No(0)', [1,0])
    heart_disease =  st.selectbox('Yes(1)/ No(0)', [1,0])
    ever_married =  st.selectbox('Yes(1)/ No(0)', [1,0])
    work_type =  st.selectbox('Male(1)/ Female(0)', [1,0])
    Residence_type =  st.text_input("Urban(1) / Rural(0)","Type Here")
    avg_glucose_level =  st.text_input("Maximum Heart rate achieved","Type Here")
    bmi =  st.text_input("Exercise induced angina (1 = yes; 0 = no)","Type Here")
    smoking_status =  st.text_input("ST depression induced by exercise relative to rest","Type Here")
    
    result=''
    if st.button("Predict"):
        result=predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success('The output is {}'.format(result))
    
    
if __name__=='__main__':
    main()
     