import streamlit as st
import requests as rq

st.title("Delete Item Form :wastebasket:")
st.subheader("Please use this form to delete an existing item by name:")

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
    submit = st.form_submit_button("Submit")
    if submit:
        rs = rq.delete(f"http://grocerylistapp-backend-1:8000/v2/grocery-items/{name}").json()
        st.write(rs["message"])