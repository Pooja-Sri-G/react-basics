import streamlit as st

st.subheader("HTML VS JSX")

var = """
HTML VS JSX:
<!-- HTML -->  \n DOES NOT REQUIRE SELF CLOSING TAGS 
\n USES class="aaa"


"""
st.write(var)
st.code('<div class="box" onclick="handle()">'
        '\n  <p>Hello</p>'
        '\n</div>', language='html')   

var = """
 JSX     =>    \n REQUIRES SELF CLOSING TAGS
                \nUSES className="aaa"
 
"""
st.write(var)

st.code('<div className="box" onClick={handle}>'
        '\n <p>Hello</p>'
        '\n</div>', language='jsx')

st.image("htmlvsjsx.jpg")