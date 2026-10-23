import streamlit as st

st.title("Arrays in state")
st.code("""
import {useState} from 'react';

function List(){

    const [list, setList] = useState(["test 1", "test 2"]);
    const [count, setCount] = useState(1);

    function addItem(){
        const itemName = "Item" + count;
        setList((previousState) =>{
            //as we are returning list items, we must use [], if they are objects we must use {}
            return [...previousState, itemName];
        });

        setCount((previousState) =>{
            return previousState+1;
        });
    }
    return (
        <>
            <h1>Item List</h1>
            <button onClick={addItem}>Add Item</button>
            <ul>
                {list.map((ele, index) => <li key={index}>{ele}</li>)}
            </ul>
        </>
    )
}
export default List;
""",language='javascript')

st.code("""
import {useState} from 'react';
function List(){

    const [team, setTeam] = useState([]);
    const teams = [
        "Oracle Redbull Racing", "Scuderia Ferrari HP", 
        "Mercedes AMG Petronas", "McLaren Mastercard", "Atlassian Williams", 
        "Aston Martin Aramco", "BWT Alpine", "Visa Cash App Racing Bulls",
        "Audi Revolut", "Cadillac", "TGR Haas"
    ]
    const [count, setCount] = useState(0);
    function addItem(){
        const teamName = teams[count];

        setTeam((previousState) => {
            return [...previousState, teamName];
        });

        setCount((prev) => {
            return prev+1;
        });
    }
    return (
        <>
            <h1>Team List</h1>
            <button onClick={addItem}>Add Team</button>
            <ul>
                {team.map((tname, index) => <li key={index}>{tname}</li>)}
            </ul>
        </>
    )
}
export default List;
""", language='javascript')