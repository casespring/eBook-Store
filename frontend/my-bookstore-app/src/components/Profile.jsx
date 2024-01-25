import { Outlet, useOutletContext } from "react-router-dom";

function Profile() {
    
    const {logout} = useOutletContext()

    return(
        <>
            <h1>Profile</h1>
            <a href="/" >
                <button onClick={logout}>Logout</button>
            </a>
        </>
    )
}

export default Profile