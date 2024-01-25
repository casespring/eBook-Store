import { useState } from 'react'

function Login({attemptLogin}) {

  // STATE //

  const [name, setName] = useState('')
  const [password, setPassword] = useState('')

  // EVENTS //

  const handleChangeUsername = e => setName(e.target.value)
  const handleChangePassword = e => setPassword(e.target.value)

function handleSubmit(e) {
  e.preventDefault();
  fetch('http://127.0.0.1:5555/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name, password }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      if (data.error) {
        // The login was not successful
        console.log('Login failed');
      } else {
        // The login was successful
        attemptLogin(data);
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

  // RENDER //

  return (
    <form className='user-form' onSubmit={handleSubmit}>

      <h2>Login</h2>

      <input type="text"
      onChange={handleChangeUsername}
      value={name}
      placeholder='name'
      />

      <input 
        type="password"
        onChange={handleChangePassword}
        value={password}
        placeholder='password'
      />

      <input type="submit"
      value='Login'
      />

    </form>
  )

}

export default Login