import streamlit as st
import requests as rq
import pandas as pd

st.title("Welcome to the Grocery List App :shopping_trolley:")

rs = rq.get("http://grocerylistapp-backend-1:8000/v2/grocery-items/").json()
if len(rs) == 0:
    st.write("Seems like your Grocery list is currently empty,")
    st.write("Please use the Create item form to add some items!")
else:
    st.subheader("Here is your current Grocery list:")
    name_list = []
    quantity_list = []
    dep_list = []
    for department,nested in rs.items():
        for name,quantity in nested.items():
            dep_list.append(department)
            name_list.append(name)
            quantity_list.append(quantity)
    df = pd.DataFrame({"Name": name_list, "Quantity": quantity_list,"Department":dep_list})
    st.dataframe(df, hide_index=True)