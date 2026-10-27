import streamlit as st

st.title("React Router")
st.subheader("What is react router?")
st.write("""React Router is a library that lets you show different components based on the URL — without reloading the page.""")

st.code("""
if URL is "/"        -> show Home
if URL is "/about"   -> show About
if URL is "/contact" -> show Contact   
""")

st.write("Install the below package to use BrowserRouter, Routes, Route")
st.code("npm install react-router-dom")
