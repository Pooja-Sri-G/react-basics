import streamlit as st

st.title("Submitting in forms")

st.write("Using \"onSubmit\" event listener we can submit and process the user input")

st.code("""
function MyForm(){
    const [name, setName] = useState("");
    console.log("Current state = ",name);

    function submission(){
        console.log("Form submitted");
        console.log("Current state = ",name);
    }
    return(
        <form onSubmit={submission}>
            <label>Enter your name = <input type="text" onChange={
                (eve) => {
                    setName(eve.target.value);
            }}/></label>
            <input type="submit"/>
        </form>
    )
}
""",language='javascript')

st.error("But default browser gets refreshed before we can view the actual output.")
st.write("To overcome the issue, we must stop the browser from getting refreshed.")

st.code("""
function submission(e){
    e.preventDefault();
    console.log("Form submitted");
    console.log("Current state = ",name);
}
""",language='javascript')

st.caption("OUTPUT")
st.image("./submission.png")