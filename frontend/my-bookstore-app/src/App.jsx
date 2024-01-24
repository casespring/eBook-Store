import { useState, useEffect } from 'react'
import { Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import "./App.css";

function App() {

  const [cartPrice, setCartPrice] = useState(0.00);

  return (
    <>
      <header className = "header">
        <NavBar />
          <div>
            <Outlet context={{ cartPrice, setCartPrice }}/>
          </div>
      </header>
    </>
  )
}

export default App
