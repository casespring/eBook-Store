// import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';
import "./BookCard.css";

function BookCard( {book} ) {

    return (
        <div className="book-card">
            <Link to={`/book/${book.id}`}>
                <img className="book-image" src={book.book_image} alt={book.title}></img>
            </Link>
            <p>Title: {book.title}</p>
            <p>Author: {book.author}</p>
            <p>${book.price}</p>
        </div>
    );
}

export default BookCard