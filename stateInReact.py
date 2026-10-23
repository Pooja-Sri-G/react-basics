import streamlit as st

st.title("State in React")

st.header("What is state?")
st.write("""State is a component's own memory — data it owns that can change over time.  
When state changes, React automatically re-renders the component.""")

st.code("""
function FavoriteColor(){
    let color="Blue";
    return(
        <>
            <h1 style={{backgroundColor:color}}>Favorite Color</h1>
            <button onClick={()=> {color = "maroon"}}>Change color</button>
        </>
    )
}

export default FavoriteColor;
""", language='javascript')

st.warning("The above program doesn't change the color actively because React still doesn't know that the color has been changed.")
st.success("So we have to convert the usual variable \"color\" into a state variable." \
" To achieve this we can use \"useState\" inorder to dynamically change state")

st.write("""useState("Blue") returns an array of exactly 2 items. You "unpack" them with []:""")
st.code("""const [color, setColor] = useState("Blue");
//      1st       2nd        ↑ initial value   """)

st.write("""1. The current value (starts as "Blue") 
\n2. A function to update that value""")

st.code("""
import {useState} from 'react';

function FavoriteColor(){
    // let color="Blue";
    const [color, setColor] = useState("blue")
    return(
        <>
            <h1 style={{backgroundColor:color}}>Favorite Color = {color}</h1>
            <button onClick={()=> setColor("Red")}>Change color</button>
        </>
    )
}

export default FavoriteColor;
""", language='javascript')