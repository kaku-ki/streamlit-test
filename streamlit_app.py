import streamlit as st
import pandas as pd


df = pd.read_csv('data/test.csv')
st.line_chart(df, x='target_datetime', y='green_gen_actual')
