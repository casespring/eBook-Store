import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import ReviewSection  from "./ReviewSection";
import { Outlet, useOutletContext } from "react-router-dom";
import "./BookDetails.css"

function BookDetails() {
    const [books, setBooks] = useState([]);
    const [reviews, setReviews] = useState([]);
    const [price, setPrice] = useState(0.00);

    const {cartPrice, setCartPrice} = useOutletContext()

    const { id } = useParams();
    useEffect(() => {
        fetch(`http://127.0.0.1:5555/api/books/${id}`)
            .then(r => r.json())
            .then(data => {
            setBooks(data)
        })
        },[]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/api/book_reviews/${id}`)
            .then(r => r.json())
            .then(data => {
            setReviews(data)
        })
    },[]);
    const renderReviews = reviews.map((review) => <ReviewSection review={review}/>);

    // Updates cart and price onclick
    function handleClick() {
        setCartPrice(prevCartPrice => prevCartPrice + books.price);
        console.log(cartPrice);

        fetch("http://127.0.0.1:5555/api/carts", {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify({
                image: books.image,
                title: books.title,
                author: books.author,
                price: books.price,
                state: true
            })
    })
        // fetch("http://localhost:3000/cart_total/1", {
        //     method: "PATCH",
        //     headers: {
        //         Accept: "application/json",
        //         "Content-Type": "application/json"
        //     },
        //     body: JSON.stringify({
        //         total: cartPrice
        //     })
        // });
    }
    
    return (
        <>
        <div className="book-container">
            <img src={books.book_image}></img>
            <div className="book-info">
                <p>Title: {books.title}</p>
                <p>Author: {books.author}</p>
                <p>${books.price}</p>
                <button onClick={handleClick}>Add to Cart</button>
            </div>
        </div>

        <div className="overview">
            <h1>Overview</h1>
            <p>{books.summary}</p>
        </div>

        <div className="review-container">
            <h1>Reviews</h1>
            {renderReviews}
        </div>
        </>
    )
}

export default BookDetails