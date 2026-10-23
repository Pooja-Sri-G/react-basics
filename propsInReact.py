import streamlit as st

st.subheader("Props in react")
st.caption("Refer components in react-tutorial folder")

st.write("Parent component sending props")
st.code("""
import FunctionChild from './FunctionChild';
import ClassChild from './ClassChild';

function Parent() {
  const name = "Pooja";
  const age = 25;

  return (
    <>
      <FunctionChild name={name} />
      <ClassChild name={name} age={age} />
    </>
  );
}
export default Parent;   
""", language='javascript')

st.write("Props in class component")
st.code("""
import React from 'react';

class ClassChild extends React.Component {
  render() {
    return <h2>Class child: {this.props.name}, age: {this.props.age}</h2>;
  }
}
export default ClassChild;   
""",language='javascript')

st.write("Props in functional component")
st.code("""
function FunctionChild(props) {
  return <h2>Function child: {props.name}</h2>;
}
export default FunctionChild;   
""",language='javascript')
