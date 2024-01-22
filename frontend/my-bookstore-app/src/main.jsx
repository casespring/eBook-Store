// import React from 'react'
// import ReactDOM from 'react-dom/client'
// import App from './App.jsx'
// import './index.css'
// import {createBrowserRouter, RouterProvider} from "react-router-dom";
// import routes from "./routes.jsx"

// const router = createBrowserRouter(routes)

// const root = ReactDOM.createRoot(document.getElementById("root"))
// root.render(<RouterProvider router={router} />);

// ReactDOM.createRoot(document.getElementById('root')).render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
// )
import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from './App.jsx'
import './index.css'
import routes from "./routes.jsx"


const router = createBrowserRouter(routes)
  
const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(<RouterProvider router={router} />);



