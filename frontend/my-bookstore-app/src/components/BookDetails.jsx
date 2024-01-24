import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import ReviewSection  from "./ReviewSection";
import { Outlet, useOutletContext } from "react-router-dom";

function BookDetails() {
    const [books, setBooks] = useState([]);
    const [reviews, setReviews] = useState([]);
    const [price, setPrice] = useState(0.00);

    const {cartPrice, setCartPrice} = useOutletContext()

    const { id } = useParams();
    useEffect(() => {
        fetch(`http://localhost:3000/books/${id}`)
            .then(r => r.json())
            .then(data => {
            setBooks(data)
        })
        },[]);

    useEffect(() => {
        fetch(`http://localhost:3000/books/${id}/book_review`)
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

        fetch("http://localhost:3000/cart", {
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
        fetch("http://localhost:3000/cart_total/1", {
            method: "PATCH",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                total: cartPrice
            })
        });
    }
    
    return (
        <>
        <div className="book-container">
            <img src={books.image}></img>
            <div className="book-info">
                <p>Title: {books.title}</p>
                <p>Author: {books.author}</p>
                <p>${books.price}</p>
                <button onClick={handleClick}>Add to Cart</button>
            </div>
        </div>

        <div className="overview">
            <h1>Overview</h1>
            <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.</p>
        </div>

        <h1>Reviews</h1>
        {renderReviews}
        </>
    )
}

export default BookDetails