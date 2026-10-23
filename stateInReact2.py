import streamlit as st

st.title("Using state in class component")

st.write("""To use the state functionality inside class component, "constructor" and "this" keyword must be used""")
st.success("""Parent class "React.Component" provides "state" and "setState" functionalities by default""")
st.caption("FavoriteTeam.js")

st.code("""
import React from 'react';

class FavoriteTeam extends React.Component{
    constructor(){
        super();
        this.state = {team : "RedBull"}
    }
    render(){
        return (
            <>
                <h1>My Favorite Team is {this.state.team}</h1>
                <button onClick={()=> this.setState({team:"Mercedes"})}>Change team</button>
            </>
        )
    }
}

export default FavoriteTeam;
""",language='javascript')

st.subheader("Multiple state")
st.code("""
import { useState } from "react";

function Car(){
    const [team, setTeam] = useState("Mercedes AMG Petronas");
    const [driver, setDriver] = useState("Kimi");
    const [number, setNumber] = useState(12);
    const [name, setName] = useState("W17");

    return(
        <>
            <h1>Car details</h1>
            <h2>Team name = {team}</h2>
            <h2>Driver name = {driver}</h2>
            <h2>Driver number = {number}</h2>
            <h2>Car = {name}</h2>

            <button onClick={()=> {
                    setDriver("Lewis");
                    setNumber(44);
                    setName("W11");
                }}>Change driver</button>

        </>
    )
}

export default Car;
""", language='javascript')

