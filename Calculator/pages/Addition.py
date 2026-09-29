import streamlit as st

st.header("Addition")

num1 =st.number_input("Enter Number 1 ",min_value=0)
num2 =st.number_input("Enter Number 2 ",min_value=0)

btn =st.button("Add")

if btn:
    st.write("Sum :" ,num1+num2)