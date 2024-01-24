import React, { useState, useEffect } from 'react'
import CartCard from './CartCard'
import { useParams } from "react-router-dom";

function Cart() {

    const [cartItems, setCartItems] = useState([])
    const [isItemInCart, setIsItemInCart] = useState(false)

    useEffect(() => {
        fetch("http://localhost:3000/cart")
            .then(r => r.json())
            .then(data => {
            setCartItems(data)
            console.log(data)
            console.log(data.state)
            setIsItemInCart(data.state)
        })
    },[]);
    console.log(isItemInCart)
    const renderCart = cartItems.map((item) => <CartCard item={item}/>);
    return(
        <>
            {/* {isItemInCart ? {renderCart} : <p>Your cart is empty</p>} */}
            <div className="cart-container">
                <div>
                    {renderCart}
                </div>
                <h1>Order Summary</h1>
            </div>
        </>
    )
}

export default Cart