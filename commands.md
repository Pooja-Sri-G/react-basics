cdn links
babel cdn

node -v
npm -v
npx -v
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned   
npx create-react-app appName

npm start


THEORY:

node_modules :
    project uses the folders and libraries in this 

public:
    index.html => first and front page

src:
    contains html, css files (file name can be user defined)

package-lock.json:
    contains packages installed and required to run the project alongside VERSION NUMBERS

package.json:
    details of the project (dependencies and libraries being used to run the project)


HTML VS JSX:
<!-- HTML -->   DOES NOT REQUIRE SELF CLOSING TAGS
                USES class="aaa"
<div class="box" onclick="handle()">
  <p>Hello</p>
</div>   

// JSX          REQUIRES SELF CLOSING TAGS
                USES className="aaa"
<div className="box" onClick={handle}>
  <p>Hello</p>
</div>   

React gets confused with list items:
    
    const drivers = [
        {name: "Max", team:"RedBull"},
        {name: "Lewis", team:"Mercedes"},
        {name: "Charles", team:"Ferrari"},
        {name: "Fernando", team:"Aston Martin"}
    ]

    <ul>
        {drivers.map((drivers)=> <li><Drivers drivers={drivers}/></li>)}
    </ul>

    for example, 
        hi i am apple
        hi i am banana
        hi i am tomato

    if you intend to change only one list item, generally it affects all the others.
    so we must use LIST KEYS concept to make sure react knows that these are different items.

USING LIST KEYS:

    <ul>
        {drivers.map((drivers)=> <li key={drivers.team}><Drivers drivers={drivers}/></li>)}
    </ul>

