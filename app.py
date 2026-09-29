import streamlit as st

#number_input()
#text_input()
#date_input()
#button

num1=st.number_input("Enter Number1 : ", min_value=0)
num2=st.number_input("Enter Number2 : ",min_value=0)
#st.write(num1)
#st.write(num2)


name=st.text_input("Enter Your Name")
#st.write(name)

date=st.date_input("Enter Date")
#st.write(date)

btn=st.button("Click")
print(btn)

if btn:
    st.write(num1)
    st.write(num2)
    st.write(name)
    st.write(date)

#Radio button 
g=st.radio("Gender",["Male","Female"])
st.write(g)

#Check box
l=st.checkbox("Python")
st.write(l)

#Select
s=st.selectbox("Places",["Ekm","Thrissur","Trivandrum"])
st.write(s)