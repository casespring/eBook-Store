import React from 'react';

const UserContext = React.createContext({
  user: null, // initial user data
  setUser: () => {}, // function to update the user data
});

export default UserContext;