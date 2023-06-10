import streamlit as st
import requests as rq

st.title("Edit Item Form :hammer_and_wrench:")
st.subheader("Please use this form to edit an existing item by name:")

rs = rq.get("http://grocerylistapp-backend-1:8000/v2/grocery-items/").json()
if len(rs) == 0:
    st.write("Seems like your Grocery list is currently empty,")
    st.write("Please use the Create item form to add some items!")

name_list = []

for department,nested in rs.items():
        for name,quantity in nested.items():
            name_list.append(name)

with st.form("CreateItemForm"):
    name = st.selectbox(label="Name:",options=name_list)
    quantity = st.number_input(label="Quantity:",step=1,min_value=1)
    department = st.selectbox(label="Department:",options=["", 'Alcohol', 'Baby', 'Baked Goods', 'Baking', 'Beverages', 'Canned', 'Coffee & Tea', 'Condiments', 'Dairy', 'Deli', 'Frozen', 'Grains', 'Household', 'Meat', 'Misc', 'Personal Care', 'Pets', 'Produce', 'Snacks', 'Spices'])
    if department == "":
        department = "uncategorized"
    submit = st.form_submit_button("Submit")
    if submit:
        rs = rq.put("http://grocerylistapp-backend-1:8000/v2/grocery-items/",json={"name":name,"quantity":quantity,"department":department}).json()
        st.write(rs["message"])