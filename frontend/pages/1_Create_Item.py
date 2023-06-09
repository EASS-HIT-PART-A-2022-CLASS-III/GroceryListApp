import streamlit as st
import requests as rq

st.title("Create Item Form")
st.write("Please use this form to add a new item to your list:")

with st.form("CreateItemForm"):
    name = st.text_input(label="Name:")
    quantity = st.number_input(label="Quantity:",step=1,min_value=0)
    department = st.text_input(label="Department:")
    if department == "":
        department = "uncategorized"
    submit = st.form_submit_button("Submit")
    if submit:
       rs = rq.post("http://grocerylistapp-backend-1:8000/v2/grocery-items/",json={"name":name,"quantity":quantity,"department":department}).json()
       st.write(rs)