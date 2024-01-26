import React, { useEffect, useState } from "react";
import UserContext from './UserContext.jsx';
import "./Checkout.css"

function Checkout() {

    const [cartTotal, setCartTotal] = useState([])
    const [formData, setFormData] = useState({
        fname: "",
        lname: "",
        streetname: "",
        city: "",
        state: "",
        zipcode: "",
        phonenumber: "",
    });

    useEffect(() => {
        fetch(`http://localhost:3000/cart_total/1`)
            .then(r => r.json())
            .then(data => {
                setCartTotal(data.total);
            });
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevData => ({
            ...prevData,
            [name]: value,
        }));
    };
    
    const handleSubmit = (e) => {
        e.preventDefault();
        // Perform the POST request with formData and cartTotal
        fetch("http://localhost:3000/user_submitted_order", {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify({
                ...formData,
                cartTotal,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle success response if needed
            console.log("Order submitted successfully:", data);
            window.alert("Your order has been placed!");
        })
        .catch(error => {
            // Handle error if needed
            console.error("Error submitting order:", error);
        });
    };



    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="fname">First name:</label><br />
                <input type="text" id="fname" name="fname" value={formData.fname} onChange={handleChange}/><br />
                <label htmlFor="lname">Last name:</label><br />
                <input type="text" id="lname" name="lname" value={formData.lname} onChange={handleChange}/><br />
                <label htmlFor="streetname">Street Name:</label><br />
                <input type="text" id="streetname" name="streetname" value={formData.streetname} onChange={handleChange}/><br />
                <label htmlFor="city">City:</label><br />
                <input type="text" id="city" name="city" value={formData.city} onChange={handleChange}/><br />
                <label htmlFor="city">State:</label><br />
                <select value={formData.state} onChange={handleChange} name="state">
                    <option value="AL">Alabama</option>
                    <option value="AK">Alaska</option>
                    <option value="AZ">Arizona</option>
                    <option value="AR">Arkansas</option>
                    <option value="CA">California</option>
                    <option value="CO">Colorado</option>
                    <option value="CT">Connecticut</option>
                    <option value="DE">Delaware</option>
                    <option value="DC">District Of Columbia</option>
                    <option value="FL">Florida</option>
                    <option value="GA">Georgia</option>
                    <option value="HI">Hawaii</option>
                    <option value="ID">Idaho</option>
                    <option value="IL">Illinois</option>
                    <option value="IN">Indiana</option>
                    <option value="IA">Iowa</option>
                    <option value="KS">Kansas</option>
                    <option value="KY">Kentucky</option>
                    <option value="LA">Louisiana</option>
                    <option value="ME">Maine</option>
                    <option value="MD">Maryland</option>
                    <option value="MA">Massachusetts</option>
                    <option value="MI">Michigan</option>
                    <option value="MN">Minnesota</option>
                    <option value="MS">Mississippi</option>
                    <option value="MO">Missouri</option>
                    <option value="MT">Montana</option>
                    <option value="NE">Nebraska</option>
                    <option value="NV">Nevada</option>
                    <option value="NH">New Hampshire</option>
                    <option value="NJ">New Jersey</option>
                    <option value="NM">New Mexico</option>
                    <option value="NY">New York</option>
                    <option value="NC">North Carolina</option>
                    <option value="ND">North Dakota</option>
                    <option value="OH">Ohio</option>
                    <option value="OK">Oklahoma</option>
                    <option value="OR">Oregon</option>
                    <option value="PA">Pennsylvania</option>
                    <option value="RI">Rhode Island</option>
                    <option value="SC">South Carolina</option>
                    <option value="SD">South Dakota</option>
                    <option value="TN">Tennessee</option>
                    <option value="TX">Texas</option>
                    <option value="UT">Utah</option>
                    <option value="VT">Vermont</option>
                    <option value="VA">Virginia</option>
                    <option value="WA">Washington</option>
                    <option value="WV">West Virginia</option>
                    <option value="WI">Wisconsin</option>
                    <option value="WY">Wyoming</option>
                </select><br />
                <label htmlFor="zipcode">Zip Code:</label><br />
                <input type="text" id="zipcode" name="zipcode" value={formData.zipcode} onChange={handleChange}/><br />
                <label htmlFor="phonenumber">Phone Number:</label><br />
                <input type="text" id="phonenumber" name="phonenumber" value={formData.phonenumber} onChange={handleChange}/><br />
                <label htmlFor="cardName">Card Holder Name:</label><br />
                <input type="text" id="cardName" name="cardName" value={formData.cardName} onChange={handleChange}/><br />
                <label htmlFor="cardNumber">Card Number:</label><br />
                <input type="text" id="cardNumber" name="cardNumber" value={formData.cardNumber} onChange={handleChange}/><br />
                <label htmlFor="cardExpiry">Expiry Date:</label><br />
                <input type="text" id="cardExpiry" name="cardExpiry" value={formData.cardExpiry} onChange={handleChange}/><br />
                <label htmlFor="cardCVV">CVV:</label><br />
                <input type="text" id="cardCVV" name="cardCVV" value={formData.cardCVV} onChange={handleChange}/><br />
                <div>
                    <h1>Order Summary</h1>
                    <p>{cartTotal}</p>
                </div>
                <input type="submit" value="Submit" />
            </form>

        </div>
    );
}

export default Checkout;
