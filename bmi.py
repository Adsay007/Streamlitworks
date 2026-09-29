import streamlit as st

st.header("BMI Calculator")
weight=st.number_input("Enter Weight in Kg",min_value=0)
height=st.number_input("Enter Height in Cm",min_value=0)



btn=st.button("BMI Calculate")
if btn:
     bmi=weight/((height/100)**2)
     st.write("Your BMI :",bmi)

     if (bmi<18.5):
        st.info("Underweight")

     elif (18.5<=bmi<25) :
        st.success("Normal") 

     elif (25<=bmi<30) :
        st.warning("Overweight")   

     elif (bmi>30):
        st.error("Obesity")   
        

