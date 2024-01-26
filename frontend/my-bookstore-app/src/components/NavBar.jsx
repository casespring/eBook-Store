import { NavLink } from "react-router-dom";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import BookSearch from './BookSearchBar.jsx'; // import BookSearch
import "./NavBar.css";

function NavBar( {user, onSearchTerm} ) { // add onSearchTerm prop
    const navigate = useNavigate();

    const handleSearchChange = (event) => {
        onSearchTerm(event.target.value);
      };

    return (
        // Navbar
        <nav className="navbar">
            <a href="/" >
                <h1 className="logo">Hugo's & Farms</h1>
            </a>
            {/* searchbar */}
            <BookSearch onSearchTerm={onSearchTerm} /> {/* use BookSearch component */}
            {/* profile and cart */}
            
            <ul className="profilecart">
                <li>
                {/* <NavLink to="/profile" > */}
                <a href="/profile">
                    {user ? <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile"></img> : <p>Sign In</p>}
                    {/* // <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile"></img> */}
                </a>
                {/* </NavLink> */}
                </li>
                <li>
                <a href="/cart">
                    <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/263/263142.png" alt="cart"></img>
                </a>
                </li>
            </ul> 
                
        </nav>
    );
}

export default NavBar;