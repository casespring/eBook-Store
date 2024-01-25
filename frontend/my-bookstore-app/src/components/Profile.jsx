import { Outlet, useOutletContext } from "react-router-dom";

function Profile() {
    
    const {logout} = useOutletContext()

    return(
        <>
            <h1>Profile</h1>
            <button onClick={logout}>Logout</button>
        </>
    )
}

export default Profile