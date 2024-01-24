import { useParams } from "react-router-dom";

function CartCard( {item} ) {
    const { id } = useParams();

    function handleClick() {
        fetch(`http://localhost:3000/cart/${id}`, {
        method: 'DELETE',
        headers: {'Content-type': 'application/json'},
    }) 
    console.log('deleted')
    }

    return(
        <div>
            <img src={item.image}></img>
            <p>{item.title}</p>
            <p>By: {item.author}</p>
            <p>${item.price}</p>
            <button onClick={handleClick}>x</button>
        </div>
    )
}

export default CartCard