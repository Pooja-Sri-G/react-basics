import streamlit as st

st.title("Inline CSS")


st.write("CSS in jsx")
st.code("""<h1 style={{color:"white", backgroundColor:"maroon"}}> Inline styling </h1>""")

st.write("CSS in jsx using variable")
st.code("""
    
    const myStyle = {
        color:"white",
        backgroundColor:"gray"
    }
    """
)
st.code(""" <h1 style={myStyle}> Variable based </h1>""", language="javascript")

st.caption("OUTPUT")
st.image("inlineCss.png")
