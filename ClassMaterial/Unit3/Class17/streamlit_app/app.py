# -*- coding: utf-8 -*-
"""
Sample Script for Streamlit Application for Kickstarter dataset
"""

import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

@st.cache
def load_data(n_rows=3000):
    data = pd.read_csv('https://raw.githubusercontent.com/JonathanBechtel/dat-02-22/main/ClassMaterial/Unit3/data/ks2.csv', nrows=n_rows)
    return data

@st.cache
def group_data(x_axis, y_axis):
    result = data.groupby(x_axis)[y_axis].mean()
    return result

@st.cache
def load_model():
    with open('mod.pkl', 'rb') as mod:
        pipe = pickle.load(mod)
        
    return pipe

st.title("Understanding Kickstarter Applications")

section = st.sidebar.radio('Section', ['Data Explorer', 'Model Predictions'])

n_rows = st.sidebar.number_input("Enter Number of Rows To Load", min_value=1000, max_value=100000, step=1000)
data = load_data(n_rows)
if section == 'Data Explorer':
    chart_type = st.sidebar.selectbox('Chart Type', ['Bar', 'Line', 'Strip'])
    
    st.write(data)
    
    x_axis = st.sidebar.selectbox('Choose Column for X-Axis', ['category',  'main_category', 'country'])
    y_axis = st.sidebar.selectbox('Choose Column for y-axis', ['state', 'goal'])
    
    st.header(f"Average value for {y_axis} for column {x_axis}")

    if chart_type == 'Bar':
        result = group_data(x_axis, y_axis)
        st.bar_chart(result)
    elif chart_type == 'Line':
        result = group_data(x_axis, y_axis)
        st.line_chart(result)
    else:
        result = data[[x_axis, y_axis]]
        st.plotly_chart(px.strip(result, x=x_axis, y=y_axis, color=x_axis))
        
elif section == 'Model Predictions':
    with open('mod.pkl', 'rb') as mod:
        pipe = pickle.load(mod)
    print(pipe)
    category       = st.sidebar.selectbox('Select A Category', data['category'].unique().tolist())
    main_category  = st.sidebar.selectbox('Select a Main Category', data['main_category'].unique().tolist())
    funding_amount = st.sidebar.number_input('Enter Your Funding Amount', min_value=0, value=1000, step=500) 
    
    sample = pd.DataFrame({
        'category': [category],
        'main_category': [main_category],
        'funding_amount': [funding_amount]
        })
    
    
    prediction = pipe.predict_proba(sample)
    print(prediction)
    
    st.header(f"Predicted Probability of Campaign Successs: {prediction[0][1]:.2%}")