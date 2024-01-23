import { useState, useEffect } from 'react'
import { Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import "./App.css";

function App() {
  return (
    <>
      <header className = "header">
        <NavBar />
          <div>
            <Outlet />
          </div>
      </header>
    </>
  )
}

export default App
