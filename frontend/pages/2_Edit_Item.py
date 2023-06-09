import streamlit as st
import requests as rq

st.title("Edit Item Form")
st.write("Please use this form to edit an existing item by name:")

with st.form("CreateItemForm"):
    name = st.text_input(label="Name:")
    quantity = st.number_input(label="Quantity:",step=1,min_value=0)
    department = st.selectbox(label="Department:",options=["", "Produce", "Dairy", "Meat", "Baked Goods", "Baking", "Frozen", "Deli", "Beverages", "Coffee & Tea", "Snacks", "Alcohol", "Canned", "Condiments", "Spices", "Grains", "Personal Care", "Household", "Pets", "Baby", "Misc"])
    if department == "":
        department = "uncategorized"
    submit = st.form_submit_button("Submit")
    if submit:
        rs = rq.put("http://grocerylistapp-backend-1:8000/v2/grocery-items/",json={"name":name,"quantity":quantity,"department":department}).json()
        st.write(rs)