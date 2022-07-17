import streamlit as st
import joblib 
model=joblib.load('uber')
st.title("UBER:NO OF WEEKLY RIDES")
f=st.number_input("enter price per week",15.00,110.00,step=5.00)
s=st.number_input("enter population",1600000,1800000,step=10000)
t=st.number_input("monthly income",5800,16200,step=100)
ft=st.number_input("average parking per month",50,200,step=5)
op=model.predict([[f,s,t,ft]])
if st.button('PREDICT'):
  st.title("NO of weekly rides",op[0])
    
