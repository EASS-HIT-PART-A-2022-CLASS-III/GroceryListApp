import streamlit as st
import requests as rq

st.title("Create Item")

with st.form("CreateItemForm"):
    st.write("Please enter your item:")
    name = st.text_input(label="Name:")
    quantity = st.number_input(label="Quantity:",step=1,min_value=0)
    department = st.text_input(label="Department:")
    if department == "":
        department = "uncategorized"
    submit = st.form_submit_button("Submit")
    if submit:
       rs = rq.post("http://grocerylistapp-backend-1:8000/v1/grocery-items/",json={"name":name,"quantity":quantity,"department":department}).json()
       st.write(rs)