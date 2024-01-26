import { useState, useEffect } from 'react'
import UserContext from './components/UserContext.jsx';
import { Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import Profile from './components/Profile.jsx';
import "./App.css";
import Login from "./components/Login"

function App() {
  const [user, setUser] = useState(null);
  const [cartPrice, setCartPrice] = useState(0.00);
  const [searchTerm, setSearchTerm] = useState(''); // add searchTerm state here

  useEffect(() => {
    fetch(`api/check_session`).then((res) => {
        if (res.ok) {
            res.json().then((user) => setUser(user));
        }
    });
  }, []);

  // AUTHENTICATION //

  async function attemptLogin(userInfo) {
    try {
      const response = await fetch(`http://127.0.0.1:5555/api/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accepts: "application/json",
        },
        body: JSON.stringify(userInfo),
      });
  
      if (!response.ok) {
        throw response;
      }
  
      const data = await response.json();
      setUser(data);
      return true; // login was successful
    } catch (e) {
      console.log(e);
      return false; // login failed
    }
  }

  const handleSearchTerm = (term) => { // move handleSearchTerm function here
    setSearchTerm(term);
  }

  function logout() {
    fetch(`/api/logout`, { method: "DELETE" }).then((res) => {
        if (res.ok) {
            setUser(null);
        }
    });
  }

  return (
    <UserContext.Provider value={{ user, setUser, logout, searchTerm, handleSearchTerm, attemptLogin, cartPrice, setCartPrice }}>
      <header className = "header">
        <NavBar user={user} onSearchTerm={handleSearchTerm} /> {/* pass handleSearchTerm to NavBar */}
        {user ? 
          <div>
            <h1>Hello {user.name}</h1>
            <Outlet context={{ cartPrice, setCartPrice, logout, attemptLogin, searchTerm, handleSearchTerm }}/> {/* pass searchTerm and handleSearchTerm to Outlet */}
          </div>:
          <div>
            {/* <h1>Hello {user.name}</h1> */}
            <Outlet context={{ cartPrice, setCartPrice, logout, attemptLogin, searchTerm, handleSearchTerm }}/> {/* pass searchTerm and handleSearchTerm to Outlet */}
          </div>
        }
        {/* <Outlet context={{ cartPrice, setCartPrice, logout }}/> */}
      </header>
    </UserContext.Provider>
  )
}

export default App