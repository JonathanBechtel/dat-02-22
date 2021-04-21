# -*- coding: utf-8 -*-
"""
Sample streamlit file
"""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/JonathanBechtel/dat-02-22/main/ClassMaterial/Unit3/data/ks2.csv', nrows=2000)

st.header("Exploring Kickstart Campaigns")

st.write(df)
