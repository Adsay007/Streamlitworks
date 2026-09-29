import streamlit as st
from Librarydb import BookListCreateRetrieveUpdateDelete

st.title("All Books")

btn = st.button("SHOW ALL BOOKS")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    records = b.list()
    
    if records :
     st.table(records)
     st.success("Record Readed Succesfully")
    else:
     st.warning("No records found in the database.")