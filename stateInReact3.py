import streamlit as st

st.title("State with object")
st.subheader("State in functional component")
st.code("""
function Car(){
    const [car, setCar] = useState(
        {
            team: "Oracle Redbull Racing",
            driver: "Max",
            number: 3,
            name: "RB22"
        }
    )

    function updateCar(){
        setCar({number: 33, name:"RB19"});
    }
    return(
        <>
            <h1>Car details</h1>
            <h2>Team name = {car.team}</h2>
            <h2>Driver name = {car.driver}</h2>
            <h2>Driver number = {car.number}</h2>
            <h2>Car = {car.name}</h2>

            <button onClick={updateCar}>Change Car</button>
        </>
    )
}
""",language='javascript')

st.error("The above snippet gives only the updated attributes (number and name) in the output. Other attributes are not shown")

st.write("To overcome this issue, we use a callback function within the setState function")
st.code("""
function updateCar(){
    //setCar({number: 33, name:"RB19"});
    setCar((previousState) => {
        return {...previousState, number:33, name:"RB19"};
    })
}
""", language='javascript')
st.success("""The "...previousState" snippet copies the data alongside any changes made in the state variable""")

st.subheader("State in a class component")

st.code("""
import React from "react";

class Bike extends React.Component{

    constructor(){
        super();
        this.state = {
            team:"Ducati Lenovo", 
            rider:"Marc", 
            number:93, 
            name:"Desmosedici GP26"
        }
    }

    changeRider = ()=>{
        this.setState((previousState) => {
            return {...previousState, team:"Repsol Honda", name:"Honda RC213V"}
        })
    }
    render(){
        return(
            <>
                <h1>Bike details</h1>
                <h2>Team name = {this.state.team}</h2>
                <h2>Rider name = {this.state.rider}</h2>
                <h2>Number = {this.state.number}</h2>
                <h2>Bike = {this.state.name}</h2>
                <button onClick={this.changeRider}>Change Team</button>
            </>
        );
    }
}

export default Bike;
""",language='javascript')
