import streamlit as st
from Librarydb import BookListCreateRetrieveUpdateDelete

st.title("Delete Data")

i=st.number_input("Enter Id to Delete",min_value=0)

btn = st.button("DELETE")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    records=b.delete(i)

    if records :
     st.success("Record Deleted Succesfully")
    else:
     st.warning("No matching records found in the database.")