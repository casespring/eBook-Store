// import { useState } from 'react'
// import { Outlet, useOutletContext } from "react-router-dom";

// function Login() {

//   // STATE //
//   const {attemptLogin} = useOutletContext()

//   const [name, setName] = useState('')
//   const [password, setPassword] = useState('')

//   // EVENTS //

//   const handleChangeUsername = e => setName(e.target.value)
//   const handleChangePassword = e => setPassword(e.target.value)

//   function handleSubmit(e) {
//     e.preventDefault()
//     attemptLogin({"name": name, "password":password})
//     console.log('log')
//   }

//   // RENDER //

//   return (
//     <form className='user-form' onSubmit={handleSubmit}>

//       <h2>Login</h2>

//       <input type="text"
//       onChange={handleChangeUsername}
//       value={name}
//       placeholder='name'
//       />

//       <input type="text"
//       onChange={handleChangePassword}
//       value={password}
//       placeholder='password'
//       />

//       <input type="submit"
//       value='Login'
//       />

//     </form>
//   )

// }

// export default Login

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';  
import { useOutletContext } from "react-router-dom";

function Login() {
  // STATE //
  const { attemptLogin } = useOutletContext();
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');

  // HOOKS //
  const navigate = useNavigate();  
  // EVENTS //
  const handleChangeUsername = e => setName(e.target.value);
  const handleChangePassword = e => setPassword(e.target.value);

  function handleSubmit(e) {
    e.preventDefault();
    attemptLogin({ "name": name, "password": password });

    // Assuming attemptLogin handles the login logic and returns a boolean indicating success
    const loginSuccessful = true;

    if (loginSuccessful) {
      navigate('/');
    }

    console.log('log');
  }

  // RENDER //
  return (
    <form className='user-form' onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input
        type="text"
        onChange={handleChangeUsername}
        value={name}
        placeholder='name'
      />
      <input
        type="text"
        onChange={handleChangePassword}
        value={password}
        placeholder='password'
      />
      <input
        type="submit"
        value='Login'
      />
    </form>
  );
}

export default Login;

   
