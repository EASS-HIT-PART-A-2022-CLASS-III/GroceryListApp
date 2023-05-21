import streamlit as st
import requests as rq

st.title("Delete Item Form")
st.write("Please use this form to delete an existing item by name:")

with st.form("CreateItemForm"):
    name = st.text_input(label="Name:")
    submit = st.form_submit_button("Submit")
    if submit:
        rs = rq.delete(f"http://grocerylistapp-backend-1:8000/v1/grocery-items/{name}").json()
        st.write(rs)