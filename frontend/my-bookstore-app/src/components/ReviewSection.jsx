import React, { useState, useEffect } from 'react';
import "./ReviewSection.css"

function ReviewSection({ review }) {
    const [bookInfo, setBookInfo] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/api/books/${review.book_id}`)
            .then((r) => r.json())
            .then((data) => {
                console.log(data);
                setBookInfo(data)
            });
    }, []);

    return (
        <div className="reviews">
            <div className="left-column">
                <img className="tiny-book-image" src={bookInfo.book_image} alt={bookInfo.title}></img>
                <p className="book-name">{bookInfo.title}</p>
                <p className="rating">Rating: {review.rating}</p>
                <p className="reviewer">User: {review.reviewer}</p>
            </div>
            <div className="right-column">
                <p className="comment">{review.comment}</p>
                <p className="created-at">{review.created_at}</p>
            </div>
        </div>
    );
}
export default ReviewSection