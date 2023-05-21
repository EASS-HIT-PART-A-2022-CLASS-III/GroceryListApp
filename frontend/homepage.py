import streamlit as st
import requests as rq
import numpy as np
import pandas as pd

st.title("This is the homepage")

rs = rq.get("http://grocerylistapp-backend-1:8000/v1/grocery-items/").json()
if len(rs) == 0:
    st.write("seems like your grocery list is currently empty")
else:
    name_list = []
    quantity_list = []
    dep_list = []
    for department,nested in rs.items():
        for name,quantity in nested.items():
            dep_list.append(department)
            name_list.append(name)
            quantity_list.append(quantity)
    df = pd.DataFrame({"name": name_list, "quantity": quantity_list,"department":dep_list})
    st.dataframe(df)