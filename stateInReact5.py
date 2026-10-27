import streamlit as st

st.title("useEffect Hook")

st.subheader("What is hook?")
st.write("A Hook is a special function in React that lets you \"hook into\" React features — like state, lifecycle, and context — from inside a function component, without writing a class")

st.subheader("What is useEffect?")
st.write("""useEffect is a hook that lets you run code after your component renders — things that interact with the "outside world." """)

st.code("""
import { useEffect } from 'react';
import { useState } from 'react';

function Timer(){

    const [count, setCount] = useState(1);
    useEffect(() => {
        console.log("Screen rendered!");
    },[count]);
    function updateCount(){
        setCount((previousState)=>{
            return previousState +1;
        })
    }
    return(
        <>
            <h1>I have rendered {count} times!</h1>
            <button onClick={updateCount}>Render</button>
        </>
    )
}

export default Timer;
""",language='javascript')

st.caption("OUTPUT")
st.image("./renderImage.png")

st.write("Using the \"useEffect\" for the Team List example")
st.code("""
function Timer(){
    
    const teams = [
        "Oracle Redbull Racing", "Scuderia Ferrari HP", 
        "Mercedes AMG Petronas", "McLaren Mastercard", "Atlassian Williams", 
        "Aston Martin Aramco", "BWT Alpine", "Visa Cash App Racing Bulls",
        "Audi Revolut", "Cadillac", "TGR Haas"
    ]
    const [team, setTeam] = useState([])
    const [count, setCount] = useState(0);

    useEffect(() => {
        console.log("Currect State = ",team);

        if(count >= teams.length){
            console.log("All teams are added. Resetting teams");
            const timer = setTimeout(()=>{
                setTeam([]);
                setCount(0);
            },2000);
            return () => clearTimeout(timer);
        }
    },[count]);
    function addteam(){
        setCount((prev) => {
            return prev+1;
        });
        setTeam((previousState) => {
            return [...previousState, teams[count]];
        });
    }
    return (
        <>
            <h1>Team List</h1>
            <button onClick={addteam}>Add Team</button>
            <ul>
                {team.map((ele, index) => <li key={index}>{ele}</li>)}
            </ul>
        </>
    )
}
export default Timer;
""",language='javascript')

st.image("./teamsState.png")