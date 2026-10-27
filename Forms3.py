import streamlit as st

st.title("Forms example")
st.caption("MyForm.js")
st.code("""
import { useState } from "react";
import Details from './Details';

function MyForm(){
    const [name, setName] = useState("");
    const [age, setAge] = useState();
    const [dept, setDept] = useState();
    const [cgpa, setCgpa] = useState();
    const [isSubmitted, setSubmitted] = useState(false);
    
    function submission(e){
        e.preventDefault();
        console.log("Form submitted");
        setSubmitted(true);
    }
    if(isSubmitted){
        return <Details name={name} age={age} dept={dept} cgpa={cgpa} onBack={handleBack}/>;
    }
    function handleBack(){
        setSubmitted(false);
    }
    return(
        <form onSubmit={submission}>
            <label>Enter your name = <input type="text" onChange={
                (eve) => {
                    setName(eve.target.value);
            }}/></label><br/>

            <label>Enter your age = <input type="number" onChange={(e)=>{
                setAge(e.target.value);
            }}/></label><br/>

            <label>Enter your Department = <input type="text" onChange={(e)=>{
                setDept(e.target.value);
            }}/></label><br/>

            <label>Enter you CGPA = <input type="number" onChange={(e) => {
                setCgpa(e.target.value);
            }}/> </label><br/>

            <input type="submit"/>
        </form>
    )
}

export default MyForm;
""",language='javascript')

st.caption("Details.js")
st.code("""
import React from 'react';

class Details extends React.Component{
    render(){
        return (
            <>
                <h1>Your details</h1>
                <h3>Your Name = {this.props.name}</h3>
                <h3>Your Age = {this.props.age}</h3>
                <h3>Your Department = {this.props.dept}</h3>
                <h3>Your CGPA = {this.props.cgpa}</h3>
                <button onClick={this.props.onBack}>Back</button>
            </>
        )
    }
}

export default Details;
""",language='javascript')
st.caption("OUTPUT")
st.image("./myform.png")
st.image("./details.png")
st.success("Clicking the back button brings you back to MyForm")