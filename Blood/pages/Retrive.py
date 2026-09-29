import streamlit as st
from blooddb import BloodCRUD

st.title("Retrieve Data")

i=st.number_input("Enter Id to Find",min_value=0)

btn = st.button("Retrieve")

if btn:
    b = BloodCRUD()
    records = b.retrieve(i)

    if records:
     st.write(f"Name : {records[1]}")
     st.write(f"Blood Group : {records[2]}")
     st.write(f"Phone : {records[3]}")
     st.write(f"City : {records[4]}")
     st.write(f"Last Donation : {records[5]}")
     st.success("Record Retrieved Succesfully")
    else:
     st.warning("No records found in the database.")