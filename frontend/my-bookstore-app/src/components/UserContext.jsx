import React, { createContext, useState, useEffect } from 'react';


const UserContext = createContext();

export const UserProvider = ({ children }) => {

  const [user, setUser] = useState(null);

  const attemptLogin = async (credentials) => {
    const response = await fetch('http://127.0.0.1:5555/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
      credentials: 'include', // Include cookies
    });
  
    if (response.ok) {
      const userData = await response.json();
      setUser(userData);
      return true;
    } else {
      return false;
    }
  };

  const logout = () => {
    setUser(null);
    // Add any additional logout logic here
  };

  return (
    <UserContext.Provider value={{ user, setUser, attemptLogin, logout }}>
      {children}
    </UserContext.Provider>
  );
};

export default UserContext;