import streamlit as st
from datetime import date
st.title("Student Registration Form ")

name=st.text_input("Enter Your Name")
age =st.number_input("Enter Age",min_value=0)

dob=st.date_input("Enter DOB", 
                  min_value=date(1990,1,1),
                  max_value=date.today(),
                  value=date(2006,1,1))

email=st.text_input("Enter Your Email")

gender=st.radio("Gender",["Male","Female"])
course=st.selectbox("Courses",["Python","Dotnet","Testing"])

btn =st.button("Submit")

if btn:
    st.write ("Name : ",name)
    st.write ("Age : ",age)
    st.write ("DOB : ",dob)
    st.write ("Email : ",email)
    st.write ("Gender : ",gender)
    st.write ("Course : ",course)