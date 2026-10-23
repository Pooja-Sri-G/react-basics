import streamlit as st


st.subheader("Lists in react")
st.caption("Refer react-tutorial/src/components/Garage.js")

st.code('const drivers = ['
        '\n\t{name: "Max", team:"RedBull"},'
        '\n\t{name: "Lewis", team:"Mercedes"},'
        '\n\t{name: "Charles", team:"Ferrari"},'
        '\n\t{name: "Fernando", team:"Aston Martin"}'
    '\n]',language='javascript')

st.caption("The above list items can be sent to another component using the below structure")
st.code('<ul>'
    '\n\t{drivers.map((drivers)=> <li><Drivers drivers={drivers}/></li>)}'
    '\n</ul>')

var = """
    for example, 
        \nhi i am apple
        \nhi i am banana
        \nhi i am tomato

    \nif you intend to change only one list item, generally it affects all the others.
    \nso we must use "LIST KEYS" concept to make sure react knows that these are different items.
"""

st.write(var)

st.subheader("USING LIST KEYS")

st.code('<ul>'
        '\n\t{drivers.map((drivers)=> <li key={drivers.team}><Drivers drivers={drivers}/></li>)}'
    '\n</ul>')

st.write("If there are no identifiers in the list")

st.code('const dummy = [1,2,2,3,4,5,6,7,8,9]'
    '\n<ul>'
        '\n\t{dummy.map((num, index) => <li key={index}><p>{p}</p></li>)}'
        '\n</ul>')

