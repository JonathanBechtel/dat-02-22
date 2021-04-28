# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

@st.cache
def load_data(number_input):
    df = pd.read_csv('childrendata.csv', nrows=number_input)
    return df


# df = pd.read_csv('childrendata.csv', nrows=2000)
# st.header("Exploring Kickstart Campaigns")
# st.write(df)

# @st.cache
def group_data(x_val, y_val):
    grouping = df.groupby(x_val)[y_val].mean()
    return grouping

# @st.cache
# def filter_strip_data(x_val, y_val):
#     strip_data
    

def load_model():
    with open('mod.pkl', 'rb') as mod:
        pipe = pickle.load(mod)
    return pipe

section = st.sidebar.radio('App Section', ['Data Explorer', 'Model Explorer'])

num_rows = st.sidebar.number_input('Number of rows to load', min_value=100,value=100, step=100)

df = load_data(num_rows)


if section == 'Data Explorer':
    chart_type = st.sidebar.selectbox('Chart type', ['Bar', 'Line', 'Strip'])
    x_axis = st.sidebar.selectbox('Choose Column for X-Axis', ['YEAR', 'ISO'])
    y_axis = st.sidebar.selectbox('Choose Column for y-axis', ['CMR', 'MMR', 'MNR', 'IMR'])

    st.header("World Child Mortality (CMR) data")
    st.write(df)

    if chart_type == 'Bar':
        grouped_data = group_data(x_axis, y_axis)
        st.bar_chart(grouped_data)
    if chart_type == 'Line':
        grouped_data = group_data(x_axis, y_axis)
        st.line_chart(grouped_data)
    if chart_type == 'Strip':
        result = df[[x_axis, y_axis]]
        fig = px.strip(result, x=x_axis, y=y_axis, color=x_axis)
        st.plotly_chart(fig)
        st.strip_chart(grouped_data) 
elif section == 'Model Explorer':
    st.header('Make Predictions With Your Model')
    mod = load_model()
    
    IMR =  st.sidebar.selectbox('IMR', df['IMR'].unique())
    MMR =  st.sidebar.selectbox('MMR', df['MMR'].unique())
    #goal =  st.sidebar.number_input('Fundraising Amount', value = 1000, step=500)
    
    sample = pd.DataFrame({
        'IMR' : ['IMR'],
        'MMR' : ['MMR']
    })
    #prediction = mod.predict(sample)  
    prediction = loaded_mod.predict(X)  
#     positive_prob = prediction[0][1]
    
#     st.title(f"Odds of a Successful Campaign Are: {positive_prob: .2%}")
# if section == 'Data Explorer':
#     chart_type = st.sidebar.selectbox('Chart type', ['Bar', 'Line', 'Strip'])
#     x_axis = st.sidebar.selectbox('Choose Column for X-Axis', ['category', 'main_category', 'country'])
#     y_axis = st.sidebar.selectbox('Choose Column for y-axis', ['state', 'goal'])
    
#     st.header("Exploring Kickstart Campaigns heroku")
#     st.write(df)
    
#     if chart_type == 'Bar':
#         grouped_data = group_data(x_axis, y_axis)
#         st.bar_chart(grouped_data)
#     if chart_type == 'Line':
#         grouped_data = group_data(x_axis, y_axis)
#         st.line_chart(grouped_data)
#     if chart_type == 'Strip':
#         result = df[[x_axis, y_axis]]
#         fig = px.strip(result, x=x_axis, y=y_axis, color=x_axis)
#         st.plotly_chart(fig)
#         st.strip_chart(grouped_data)    
        
# elif section == 'Model Explorer':
#     st.header('Make Predictions With Your Model')
#     mod = load_model()
    
#     category =  st.sidebar.selectbox('Category', df['category'].unique())
#     main_category =  st.sidebar.selectbox('Main Category', df['main_category'].unique())
#     goal =  st.sidebar.number_input('Fundraising Amount', value = 1000, step=500)
    
#     sample = pd.DataFrame({
#         'category' : ['category'],
#         'main_category' : ['main_category'],
#         'goal' : [2450]
#     })
#     prediction = mod.predict_proba(sample)    
#     positive_prob = prediction[0][1]
    
#     st.title(f"Odds of a Successful Campaign Are: {positive_prob: .2%}")
        
    
    
    
    
    