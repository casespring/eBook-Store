import React, { useState, useEffect } from 'react'
import BookCard from './BookCard'
import { useNavigate } from "react-router-dom";
import ReviewSection from './ReviewSection';
import "./Home.css";

function Home() {
    const [books, setBooks] = useState([]);
    const [reviews, setReviews] = useState([]);
    // navigate = useNavigate();

    useEffect(() => {
        fetch("http://localhost:3000/books")
            .then(r => r.json())
            .then(data => {
            setBooks(data)
        })
        },[]);

        useEffect(() => {
            fetch("http://localhost:3000/book_review")
                .then(r => r.json())
                .then(data => {
                setReviews(data)
            })
            },[]);

    console.log(books)
    const renderBooksTopSellers = books.map((book) => <BookCard book={book}/>);
    // const renderBooksTopNewArrivals = books.map((book)) => <BookCard book={book}/>);
    const renderReviews = reviews.map((review) => <ReviewSection review={review}/>);

    return(
        <>
        <div>
            <h1 className='header-styles'>Bestsellers </h1>
            <div className="card-container">
                {renderBooksTopSellers}
            </div>   
        </div>
        <div>
            <h1 className='header-styles'>New Arrivals </h1>
            <div className="card-container">
                {renderBooksTopSellers}
            </div>   
        </div>
        <div>
            <h1 className='header-styles'>User Reviews</h1>
            <div className="review-container">
                {renderReviews}
            </div>   
        </div>

        </>
    )
}

export default Home