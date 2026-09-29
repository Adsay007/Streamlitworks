import streamlit as st
from Librarydb import BookListCreateRetrieveUpdateDelete

st.title("Update Records")

i=st.number_input("id",min_value=0)
t=st.text_input("Title")
a=st.text_input("Author")
p=st.number_input("Price",min_value=0)
pg=st.number_input("Pages",min_value=0)
l=st.text_input("Language")

btn=st.button("Update")

if btn:
    b=BookListCreateRetrieveUpdateDelete()
    records = b.update(i,t,a,p,pg,l)

    if records:
     st.success("Record Updated Succesfully")
    else:
       st.error("No ID Match Found")