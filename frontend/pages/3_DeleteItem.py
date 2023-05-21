import streamlit as st
import requests as rq

st.title("Delete Item")

with st.form("CreateItemForm"):
    st.write("Please enter your item:")
    name = st.text_input(label="Name:")
    submit = st.form_submit_button("Submit")
    if submit:
        rs = rq.delete(f"http://grocerylistapp-backend-1:8000/v1/grocery-items/{name}").json()
        st.write(rs)