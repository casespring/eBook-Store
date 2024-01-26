import React from "react";
import App from "./App.jsx"
import Profile from "./components/Profile"
import Cart from "./components/Cart"
import Home from "./components/Home"
import BookDetails from "./components/BookDetails"
import Checkout from "./components/Checkout"
import Login from "./components/Login"

const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <h1>Something went wrong!</h1>,
        children: [
            {
                path: "/",
                element: <Home />,
                errorElement: <h1>Something went wrong!</h1>,
            },
            {
                path: "/profile",
                element: <Profile />,
                errorElement: <h1>Something went wrong!</h1>
            },
            {
                path: "/cart",
                element: <Cart />,
                errorElement: <h1>Something went wrong!</h1>
            },
            {
                path: "/book/:id",
                element: <BookDetails />
            },
            {
                path: "/checkout",
                element: <Checkout />
            },
            {
                path: "/login",
                element: <Login />
            }
        ]
}
]

export default routes