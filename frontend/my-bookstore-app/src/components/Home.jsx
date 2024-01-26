import React, { useState, useEffect, useContext } from 'react';
import BookCard from './BookCard';
import NavBar from './NavBar'; // import NavBar
import ReviewSection from './ReviewSection';
import UserContext from './UserContext.jsx';
import './Home.css';

function Home() {
    const [bestSellers, setBestSellers] = useState([]);
    const [newArrivals, setNewArrivals] = useState([]);
    const [reviews, setReviews] = useState([]);
    const { searchTerm, handleSearchTerm } = useContext(UserContext);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/api/books')
            .then((r) => r.json())
            .then((data) => {
                console.log(data[0].category)
                console.log(data)
                let filteredData = data;
                if (searchTerm) {
                    filteredData = data.filter(book => 
                        (book.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                        book.author?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                        book.category?.name.toLowerCase().includes(searchTerm.toLowerCase()))
                    );
                }
                const bestSellersData = [...filteredData].sort((a, b) => (b.likes ? b.likes.length : 0) - (a.likes ? a.likes.length : 0));
                const newArrivalsData = filteredData.slice().sort((a, b) => b.id - a.id); // Sort by ID in descending order
                setBestSellers(bestSellersData);
                setNewArrivals(newArrivalsData);
            });
    }, [searchTerm]);

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