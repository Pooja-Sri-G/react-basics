import streamlit as st

st.subheader("Props in react")
st.caption("Refer components in react-tutorial folder")

st.write("Parent component sending props")
st.code(open("./react-tutorial/src/props/Parent.jsx").read(), language="javascript")

st.write("Props in class component")
st.code(open("./react-tutorial/src/props/ClassChild.jsx").read(), language='javascript')  

st.write("Props in functional component")
st.code(open("./react-tutorial/src/props/FunctionChild.jsx").read(), language="javascript")
