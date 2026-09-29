import streamlit as st
from Librarydb import BookListCreateRetrieveUpdateDelete

st.title("Retrieve Data")

i=st.number_input("Enter Id to Find",min_value=0)

btn = st.button("Retrieve")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    records = b.retrieve(i)

    if records:
     st.write(f"Title : {records[1]}")
     st.write(f"Author : {records[2]}")
     st.write(f"Price : {records[3]}")
     st.write(f"Pages : {records[4]}")
     st.write(f"Language : {records[5]}")
     st.success("Record Retrieved Succesfully")
    else:
     st.warning("No records found in the database.")