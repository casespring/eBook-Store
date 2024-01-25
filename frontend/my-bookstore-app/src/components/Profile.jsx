import React, { useContext } from 'react';
import { Outlet, useOutletContext } from "react-router-dom";
import UserContext from '../components/UserContext.jsx';

function Profile() {
    const { user, setUser, logout } = useContext(UserContext);


    return(
        <>
            <h1>Profile</h1>
            <p>Name: {user.name}</p>
            <p>Email: {user.email}</p>
            {/* display other user info as needed */}
            <a href="/" >
                <button onClick={logout}>Logout</button>
            </a>
        </>
    )
}

export default Profile