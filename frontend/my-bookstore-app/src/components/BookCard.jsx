// import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';

function BookCard( {book} ) {

    return (
        <div>
            <Link to={`/book/${book.id}`}>
                <img src={book.image}></img>
            </Link>
            <p>Title: {book.title}</p>
            <p>Author: {book.author}</p>
            <p>${book.price}</p>
        </div>
    )
}

export default BookCard