import streamlit as st
from blooddb import BloodCRUD

st.title("Update Records")

i=st.number_input("id",min_value=0)

n=st.text_input("Name")
bl=st.text_input("BloodGroup")
p=st.text_input("Phone")
c=st.text_input("City")
ld=st.date_input("Last Donation")

btn=st.button("Update")

if btn:
    b=BloodCRUD()
    records = b.update(i,n,bl,p,c,ld)

    if records:
     st.success("Record Updated Succesfully")
    else:
       st.error("No ID Match Found")