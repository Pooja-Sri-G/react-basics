import streamlit as st

st.title("CSS file")

st.caption("Header.css")

st.code("""
body{
    background-color: blue;
    color: white;
    padding: 5px;
}"""
)

st.write("Import the css file to the component file")
st.caption("Header.js")
st.code("import './Header.css'")

st.caption("OUTPUT")
st.image("filebasedcss.png")

st.subheader("Changing particular elements")
st.write("Using classes and id")

st.caption("Header.module.css")
st.code("""

.bigBlue{
    color:dodgerblue;
    padding:40px;
    font-family: 'Times New Roman';
    text-align: center;
    background-color: beige;
}

#bigRed{
    color:lightcoral;
    padding:40px;
    font-family: 'Franklin Gothic Medium';
    text-align: center;
    background-color: aqua;
}
"""
)

st.caption("Header.js")
st.code("""
<h1 className={styles.bigBlue}>Header module - Class</h1>
<h1 id={styles.bigRed}>Header module - ID</h1>
""")

st.caption("OUTPUT")
st.image("headermodule.png")