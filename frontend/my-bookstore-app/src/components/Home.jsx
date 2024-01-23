import React, { useState, useEffect } from 'react'
import BookCard from './BookCard'
import { useNavigate } from "react-router-dom";

function Home() {
    const [books, setBooks] = useState([]);
    // navigate = useNavigate();

    useEffect(() => {
        fetch("http://localhost:3000/books")
            .then(r => r.json())
            .then(data => {
            setBooks(data)
        })
        },[]);
    console.log(books)
    const renderBooks = books.map((book) => <BookCard book={book}/>);

    return(
        <>
        <div className="card-container">
            {renderBooks}
        </div>
        </>
    )
}

export default Home