import streamlit as st
import requests as rq

st.title("Create Item Form :memo:")
st.subheader("Please use this form to add a new item to your list:")

with st.form("CreateItemForm"):
    name = st.text_input(label="Name:")
    quantity = st.number_input(label="Quantity:",step=1,min_value=1)
    department = st.selectbox(label="Department:",options=["",'Alcohol', 'Baby', 'Baked Goods', 'Baking', 'Beverages', 'Canned', 'Coffee & Tea', 'Condiments', 'Dairy', 'Deli', 'Frozen', 'Grains', 'Household', 'Meat', 'Misc', 'Personal Care', 'Pets', 'Produce', 'Snacks', 'Spices'])
    if department == "":
        department = "uncategorized"
    submit = st.form_submit_button("Submit")
    if submit:
       rs = rq.post("http://grocerylistapp-backend-1:8000/v2/grocery-items/",json={"name":name,"quantity":quantity,"department":department}).json()
       st.write(rs["message"])