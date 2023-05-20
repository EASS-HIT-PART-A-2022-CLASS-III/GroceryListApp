import streamlit as st
import requests as rq

st.title("This is the homepage")

rs = rq.get("http://grocerylistapp-backend-1:8000/").json()
st.write(rs)