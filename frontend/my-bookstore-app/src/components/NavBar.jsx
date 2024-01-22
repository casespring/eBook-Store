import { NavLink } from "react-router-dom";
import React from "react";
import { useNavigate } from "react-router-dom";

function NavBar() {
    const navigate = useNavigate();

    return (
        // Navbar
        <nav className="navbar">
            <NavLink to="/home" >
                <div className="logo">
                    <img src = "https://img.freepik.com/premium-vector/eagle-wing-logo-illustration-template_560456-25.jpg"></img>
                </div>
            </NavLink>

            {/* searchbar */}
            <div className="search">
                <form>
                    <input className="searchbar" type="text" placeholder="search"></input>
                </form>
            </div>

            {/* profile and cart */}

            <div className="profilecart">
                <NavLink to="/profile" >
                    <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile"></img>
                </NavLink>
            </div> 
                <NavLink to="/cart">
                    <img className="profilecart-image" src="https://cdn-icons-png.flaticon.com/512/263/263142.png" alt="cart"></img>
                </NavLink>
                
        </nav>
    );
}

export default NavBar;
