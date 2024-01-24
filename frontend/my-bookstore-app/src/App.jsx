import { useState, useEffect } from 'react'
import { Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import "./App.css";
import Login from "./components/Login"

function App() {

  const [cartPrice, setCartPrice] = useState(0.00);

  // AUTHENTICATION //

  function attemptLogin(userInfo) {
    fetch(`/login`, {
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

  return (
    <>
      <header className = "header">
        <NavBar />
        <Login attemptLogin={attemptLogin} />
          <div>
            <Outlet context={{ cartPrice, setCartPrice }}/>
          </div>
      </header>
    </>
  )
}

export default App
