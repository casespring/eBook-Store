import React, { useState, useEffect } from 'react';
import BookCard from './BookCard';
import { useNavigate } from 'react-router-dom';
import ReviewSection from './ReviewSection';
import './Home.css';

function Home() {
    const [bestSellers, setBestSellers] = useState([]);
    const [newArrivals, setNewArrivals] = useState([]);
    const [reviews, setReviews] = useState([]);
    // navigate = useNavigate();

    useEffect(() => {
        fetch('http://127.0.0.1:5555/api/books')
            .then((r) => r.json())
            .then((data) => {
                console.log(data)
                const bestSellersData = [...data].sort((a, b) => (b.likes ? b.likes.length : 0) - (a.likes ? a.likes.length : 0));
                const newArrivalsData = data.slice().sort((a, b) => b.id - a.id); // Sort by ID in descending order
                setBestSellers(bestSellersData);
                setNewArrivals(newArrivalsData);
            });
    }, []);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/api/book_reviews')
            .then((r) => r.json())
            .then((data) => {
                setReviews(data);
            });
    }, []);

    const renderBooks = (bookList) => bookList.map((book) => <BookCard key={book.id} book={book} />);
    const renderReviews = reviews.map((review) => <ReviewSection key={review.id} review={review} />);

    return (
        <>
            <div>
                <h1 className="header-styles">Bestsellers </h1>
                <div className="card-container">{renderBooks(bestSellers)}</div>
            </div>
            <div>
                <h1 className="header-styles">New Arrivals </h1>
                <div className="card-container">{renderBooks(newArrivals)}</div>
            </div>
            <div>
                <h1 className="header-styles">User Reviews</h1>
                <div className="review-container">{renderReviews}</div>
            </div>
        </>
    );
}

export default Home;
