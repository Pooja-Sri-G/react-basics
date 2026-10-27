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
        st.Page("./stateInReact3.py", title="State with objects"),
        st.Page("./stateInReact4.py", title="ArrayList updation"),
        st.Page("./stateInReact5.py", title="useEffect Hook")
    ],
    "Forms in React":[
        st.Page("./Forms.py", title="Getting input"),
        st.Page("./Forms2.py", title="Submitting a form"),
        st.Page("./Forms3.py", title="Example")
    ],
    "React Router":[
        st.Page("./react_router.py", title="Introduction")
    ]
    #"Advanced": [
      #  st.Page("pages/hooks.py", title="Hooks", icon="🪝"),
    #],
})
pg.run()   