import { useState, useContext } from 'react';
import UserContext from './UserContext.jsx';
import { useNavigate } from 'react-router-dom';  
import { useOutletContext } from "react-router-dom";
import "./Login.css";

function Login() {
  // STATE //
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const { attemptLogin } = useContext(UserContext);


  // HOOKS //
  const navigate = useNavigate();  
  // EVENTS //
  const handleChangeUsername = e => setName(e.target.value);
  const handleChangePassword = e => setPassword(e.target.value);

  async function handleSubmit(e) {
    e.preventDefault();
    const loginSuccessful = await attemptLogin({ "name": name, "password": password });
  
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
        type="password" // Changed from 'text' to 'password' to hide the input
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