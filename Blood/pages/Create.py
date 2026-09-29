import streamlit as st
from blooddb import BloodCRUD

st.title("Add New Donor")

n=st.text_input("Name")
bl=st.text_input("BloodGroup")
p=st.text_input("Phone")
c=st.text_input("City")
ld=st.date_input("Last Donation")


btn=st.button("Add")
if btn:
    b=BloodCRUD()
    b.create(n,bl,p,c,ld)
    st.success("Record Created Succesfully")