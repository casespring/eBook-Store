import { NavLink } from "react-router-dom";
import React from "react";
import { useNavigate } from "react-router-dom";
import "./NavBar.css";

function NavBar( {user} ) {
    const navigate = useNavigate();

    return (
        // Navbar
        <nav className="navbar">
            <a href="/" >
                <h1 className="logo">BookStore</h1>
            </a>
            {/* searchbar */}
            <div className="search">
                <form>
                    <input className="searchbar" type="text" placeholder="Search by Title, Author, Genre"></input>
                </form>
            </div>
            {/* profile and cart */}
            
            <ul className="profilecart">
                {/* <li>
                {user ? <a href="/profile"> : <a href="/login">}
                    {user ? <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile"></img> : <h1>Sign In</h1>}
                </a>
                </li>

                <li>
                <a href="/cart">
                    <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/263/263142.png" alt="cart"></img>
                </a>
                </li> */}
                <li>
                    {user ? (
                        <a href="/profile">
                            <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile" />
                        </a>
                    ) : (
                    <a href="/login">
                        <h1>Sign In</h1>
                    </a>
                    )}
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
