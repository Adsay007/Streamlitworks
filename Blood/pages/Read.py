import streamlit as st
from blooddb import BloodCRUD

st.title("All Books")

btn = st.button("SHOW ALL DONOR LIST")

if btn:
    b = BloodCRUD()
    records = b.list()
    
    if records :
     st.table(records)
     st.success("Record Readed Succesfully")
    else:
     st.warning("No records found in the database.")