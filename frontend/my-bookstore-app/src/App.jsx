import { useState, useEffect } from 'react'
import { Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import "./App.css";
import Login from "./components/Login"

function App() {

  const [user, setUser] = useState(null);
  const [cartPrice, setCartPrice] = useState(0.00);

  useEffect(() => {
    fetch(`api/check_session`).then((res) => {
        if (res.ok) {
            res.json().then((user) => setUser(user));
        }
    });
}, []);

  // AUTHENTICATION //

  function attemptLogin(userInfo) {
    fetch(`api/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Accepts: "application/json",
        },
        body: JSON.stringify(userInfo),
    })
        .then((res) => {
            if (res.ok) {
                return res.json();
            }
            throw res;
        })
        .then((data) => setUser(data))
        .catch((e) => console.log(e));
}

function logout() {
  fetch(`api/logout`, { method: "DELETE" }).then((res) => {
      if (res.ok) {
          setUser(null);
      }
  });
}

  return (
    <>
      <header className = "header">
        <NavBar user={user}/>
        {user ? 
                  <div>
                    <h1>Hello {user.name}</h1>
                  <Outlet context={{ cartPrice, setCartPrice, logout }}/>
                </div>:
                <Login attemptLogin={attemptLogin} />
                }
        

      </header>
    </>
  )
}

export default App
