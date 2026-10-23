import streamlit as st

st.title("REACT BASICS")

st.subheader("React within html:")
st.code(open("reactHtml.html").read(), language='html')   

st.subheader("Commands:")
st.code("node -v", language='bash')
st.code("npm -v", language='bash')
st.code("npx -v", language='bash')
st.code("Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned", language='powershell')
st.code("npx create-react-app appName", language='bash')
st.code("npm start", language='bash')

st.header("Theory")
var = """    
node_modules :
    \n\tproject uses the folders and libraries in this 

public:
    \n\tindex.html => first and front page

src:
    \n\tcontains html, css files (file name can be user defined)

package-lock.json:
    \n\tcontains packages installed and required to run the project alongside VERSION NUMBERS

package.json:
    \n\tdetails of the project (dependencies and libraries being used to run the project)    
"""

st.write(var)

