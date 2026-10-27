import streamlit as st

st.title("Getting input from user")
st.write("We can use \"onChange\" as input listener")

st.code("""
const [name, setName] = useState("");
console.log("Current state = ",name);
return(
    <>
        <label>Enter your name = <input type="text" onChange={
            (eve) => {
                setName(eve.target.value);
            }}/></label>
    </>
)
""",language='javascript')
st.success("The above snippet helps to dynamically gather user information and process it using \"onChange\" even listener.")
st.caption("OUTPUT")
st.image("./onchange.png")