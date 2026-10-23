import streamlit as st

st.set_page_config(page_title="React Basics", layout="wide")

pg = st.navigation({
    "Basics": [
        st.Page("./basics.py", title="Introduction"),
        st.Page("./htmlvsjsx.py", title="HTML vs JSX"),
        st.Page("./propsInReact.py", title="Props"),
        st.Page("./listsInReact.py", title="Lists")
    ],
    "Styling": [
        st.Page("./inlineCss.py", title="Inline CSS"),
        st.Page("./filebasedCSS.py", title="File based CSS")
    ],
    "State in React":[
        st.Page("./stateInReact.py", title="Introduction"),
        st.Page("./stateInReact2.py",title="State in class component"),
        st.Page("./stateInReact3.py", title="State with objects")
    ]
    #"Advanced": [
      #  st.Page("pages/hooks.py", title="Hooks", icon="🪝"),
    #],
})
pg.run()   