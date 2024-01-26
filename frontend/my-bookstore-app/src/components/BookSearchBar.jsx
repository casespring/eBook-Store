import { useState } from "react";
import "./BookSearchBar.css"

function BookSearch({ onSearchTerm }) {
    const [term, setTerm] = useState('');
  
    const handleInputChange = (event) => {
      setTerm(event.target.value);
      onSearchTerm(event.target.value);
    }
  
    return (
        <div className="search" >
            <input
            className="searchbar"
            type="text"
            id="search"
            placeholder="Search by Title, Author, Genre... 📖"
            value={term}
            onChange={handleInputChange}
            />
        </div>
    );
}

export default BookSearch;