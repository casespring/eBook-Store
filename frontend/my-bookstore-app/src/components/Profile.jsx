import React, { useContext, useEffect } from 'react';
import { Outlet, useOutletContext, useNavigate } from "react-router-dom";
import UserContext from './UserContext.jsx';
import defaultProfileImage from '../assets/default-User-Profile.jpg';
import './Profile.css';

function Profile() {
    const { user, setUser, logout } = useContext(UserContext);
    const navigate = useNavigate();

    useEffect(() => {
        if (!user) {
            navigate('/login');
        } else {navigate('/profile')}
    }, [user, navigate]);

    if (!user) {
        return "Loading..."; // or a loading spinner, or some other placeholder
    }

    const imageUrl = user.user_image || defaultProfileImage; 

    return(
        <div className="profile-container">
            <h1>{user.name}</h1>
            <img className="profile-picture" src={imageUrl} ></img>
            <p>Email: {user.email}</p>
            <p>Member since: {user.created_at}</p>
            <a href="/" >
                <button onClick={logout}>Logout</button>
            </a>
        </div>
    )
}

export default Profile;