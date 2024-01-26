from flask import Flask, make_response, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import dotenv_values
from models import db, Book, User, Like, Cart, BookReview, Category, Order, Delivery, OrderDetail
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from sqlalchemy.orm.exc import NoResultFound
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
# config = dotenv_values('.env')
app.secret_key = "asdfwer243523423asdrwr"
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)



@app.route('/api')
def home():
    return '<h1>Welcome to the eBook Store Database</h1>'

# CHECK SESSION
@app.get('/api/check_session')
def check_session():
    user = User.query.get(session.get('user_id'))
    print(f'check session {session.get("user_id")}')
    if user:
        return user.to_dict(rules=['-password']), 200
    else:
        return {"message": "No user logged in"}, 401

# LOGIN
@app.post('/api/login')
def login():
    data = request.json

    user = User.query.filter(User.name == data.get('name')).first()

    if user and bcrypt.check_password_hash(user.password, data.get('password')):
        session["user_id"] = user.id
        print("success")
        return user.to_dict(rules=['-password']), 200
    else:
        return { "error": "Invalid username or password" }, 401

#Books Crud
@app.route('/api/books')
def get_books():
    books = Book.query.all()
    return [book.to_dict() for book in books]

@app.route('/api/books/<int:id>')
def get_book_by_id(id):
    book = Book.query.get(id)
    if not book:
        return {"error": "Book not found"}
    return book.to_dict()

@app.delete('/api/logout')
def logout():
    session.pop('user_id')
    return { "message": "Logged out"}, 200

@app.patch('/api/books/<int:id>')
def patch_book(id):
    book = Book.query.get(id)
    if not book:
        return {"error": "Book not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(book, attribute, data[attribute])
        db.session.add(book)
        db.session.commit()
        return book.to_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.post('/api/books')
def post_book():
    try:
        data = request.json
        new_book = Book(
            title=data.get('title'),
            author=data.get('author'),
            isbn=data.get('isbn'),
            page_count=data.get('page_count'),
            summary=data.get('summary'),
            detail=data.get('detail'),
            table_of_contents=data.get('table_of_contents'),
            price=data.get('price'),
            published_date=data.get('published_date'), 
            category_id=data.get('category_id')
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/api/books/<int:id>')
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return {"error": "Book not found"}, 404
    db.session.delete(book)
    db.session.commit()
    return {}, 204

#Users Crud
@app.route('/api/users')
def get_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

@app.route('/api/users/<int:id>')
def get_users_by_id(id):
    user = User.query.get(id)
    if not user:
        return {"error": "User not found"}
    return user.to_dict()

@app.patch('/api/users/<int:id>')
def patch_user(id):
    user = User.query.get(id)
    if not user:
        return {"error": "User not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(user, attribute, data[attribute])
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

#when you need to check if a provided password matches the stored hash: 
    # check_password_hash(stored_hashed_password, provided_password)

@app.post('/api/users')
def post_user():
    try:
        data = request.json  
        hashed_password = generate_password_hash(data.get('password'))
        new_user = User(
            email=data.get('email'),
            name=data.get('name'),
            password=hashed_password,
            user_image=data.get('user_image'),
            created_at=data.get('created_at')
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/api/users/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return {"error": "User not found"}, 404
    db.session.delete(user)
    db.session.commit()
    return {}, 204

#Likes Crud
@app.route('/api/liked-books/<int:user_id>', methods=['GET'])
def get_liked_books(user_id):
    try:
        # Query the likes for the given user
        liked_books = db.session.query(Book).join(Like).filter(Like.user_id == user_id).all()

        # Serialize the liked books
        liked_books_data = [{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            # Add other book attributes as needed
        } for book in liked_books]

        return jsonify(liked_books_data)

    except NoResultFound:
        return jsonify({'error': 'No liked books found for this user'}), 404

@app.route('/api/likes', methods=['GET'])
def get_likes():
    likes = Like.query.all()
    return [like.to_dict() for like in likes]

@app.post('/api/likes')
def post_like():
    try:
        data = request.json
        new_like = Like(user_id=data.get('user_id'), book_id=data.get('book_id'))
        db.session.add(new_like)
        db.session.commit()
        return new_like.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/api/likes/<int:id>')
def delete_like(id):
    like = Like.query.get(id)
    if not like:
        return {"error": "Like not found"}, 404
    db.session.delete(like)
    db.session.commit()
    return {}, 204

#Carts Crud
@app.route('/api/carts/<int:user_id>')
def get_carts_by_user_id(user_id):
    try:
        carts = Cart.query.filter(Cart.user_id == user_id).all()
        if not carts:
            return {"error": "No cart found for this user"}, 404
        cart_info = [cart.to_dict() for cart in carts]
        return cart_info, 200
    except ValueError:
        return [], 200

@app.patch('/api/carts/<int:id>')
def patch_cart(id):
    cart = Cart.query.get(id)
    if not cart:
        return {"error": "Cart not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(cart, attribute, data[attribute])
        db.session.add(cart)
        db.session.commit()
        return cart.to_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.post('/api/carts')
def post_cart():
    try:
        data = request.json
        new_cart = Cart(
            quantity=data['quantity'],
            user_id=data['user_id'],
            book_id=data['book_id']
        )
        db.session.add(new_cart)
        db.session.commit()
        return new_cart.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/api/carts/<int:id>')
def delete_cart(id):
    cart = Cart.query.get(id)
    if not cart:
        return {"error": "Cart not found"}, 404
    db.session.delete(cart)
    db.session.commit()
    return {}, 204

#BookReview Crud
@app.route('/api/book_reviews')
def get_book_reviews():
    book_reviews = BookReview.query.all()
    return [book_review.to_dict() for book_review in book_reviews]

@app.route('/api/book_reviews/<int:book_id>')
def get_book_reviews_by_book_id(book_id):
    book = Book.query.get(book_id)
    if not book:
        return {"error": "Book not found"}, 404
    book_reviews = [review.to_dict() for review in book.book_review]
    return book_reviews, 200

@app.patch('/api/book_reviews/<int:id>')
def patch_book_review(id):
    book_review = BookReview.query.get(id)
    if not book_review:
        return {"error": "Book review not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(book_review, attribute, data[attribute])
        db.session.add(book_review)
        db.session.commit()
        return book_review.to_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.post('/api/book_reviews')
def post_book_review():
    try:
        data = request.json
        new_book_review = BookReview(reviewer=data.get('reviewer'), comment=data.get('comment'), created_at=data.get('created_at'), book_id=data.get('book_id'))
        db.session.add(new_book_review)
        db.session.commit()
        return new_book_review.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/api/book_reviews/<int:id>')
def delete_book_review(id):
    book_review = BookReview.query.get(id)
    if not book_review:
        return {"error": "Book review not found"}, 404
    db.session.delete(book_review)
    db.session.commit()
    return {}, 204

#Orders Crud
@app.route('/api/orders/<int:user_id>')
def get_orders_by_user_id(user_id):
    try:
        orders = Order.query.filter(Order.user_id == user_id).all()
        if not orders:
            return {"error": "No orders found for the user"}, 404
        orders_info = [order.to_dict() for order in orders]
        return orders_info, 200
    except ValueError:
        return {"error": "User not found"}, 404

@app.route('/api/orders/<int:id>')
def get_orders_by_id(id):
    order = Order.query.get(id)
    if not order:
        return {"error": "Order not found"}
    return order.to_dict()

@app.patch('/api/orders/<int:id>')
def patch_order(id):
    order = Order.query.get(id)
    if not order:
        return {"error": "Order not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(order, attribute, data[attribute])
        db.session.add(order)
        db.session.commit()
        return order.to_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.post('/api/orders')
def post_order():
    try:
        data = request.json
        new_order = Order(
            total_price=data.get('total_price'), 
            ordered_at=data.get('ordered_at'), 
            user_id=data.get('user_id'), 
            delivery_id=data.get('delivery_id'))
        db.session.add(new_order)
        db.session.commit()
        return new_order.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.delete('/api/orders/<int:id>')
def delete_order(id):
    order = Order.query.get(id)
    if not order:
        return {"error": "Order not found"}, 404
    db.session.delete(order)
    db.session.commit()
    return {}, 204    

#Delivery Crud
@app.route('/api/deliveries')
def get_deliveries():
    deliveries = Delivery.query.all()
    return [delivery.to_dict() for delivery in deliveries]

@app.route('/api/deliveries/<int:id>')
def get_delivery_by_id(id):
    delivery = Delivery.query.get(id)
    if not delivery:
        return {"error": "Delivery not found"}
    return delivery.to_dict()

@app.patch('/api/deliveries/<int:id>')
def patch_delivery(id):
    delivery = Delivery.query.get(id)
    if not delivery:
        return {"error": "Delivery not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(delivery, attribute, data[attribute])
        db.session.add(delivery)
        db.session.commit()
        return delivery.to_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.post('/api/deliveries')
def post_delivery():
    try:
        data = request.json
        new_delivery = Delivery(
            address=data.get('address'), 
            recipient=data.get('recipient'), 
            contact=data.get('contact'))
        db.session.add(new_delivery)
        db.session.commit()
        return new_delivery.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.delete('/api/deliveries/<int:id>')
def delete_delivery(id):
    delivery = Delivery.query.get(id)
    if not delivery:
        return {"error": "Delivery not found"}, 404
    db.session.delete(delivery)
    db.session.commit()
    return {}, 204    

#OrderDetail Crud
@app.route('/api/order_details/<int:order_id>')
def get_order_details_by_order_id(order_id):
    order = Order.query.get(order_id)
    if not order:
        return {"error": "Order not found"}, 404

    order_details = OrderDetail.query.filter(OrderDetail.order_id == order_id).all()
    if not order_details:
        return {"error": "Empty details found for the order"}, 404

    cart_info = [order_detail.to_dict() for order_detail in order_details]
    return cart_info, 200

@app.patch('/api/order_details/<int:id>')
def patch_order_detail(id):
    order_detail = OrderDetail.query.get(id)
    if not order_detail:
        return {"error": "Order detail not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(order_detail, attribute, data[attribute])
        db.session.add(order_detail)
        db.session.commit()
        return order_detail.to_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.post('/api/order_details')
def post_order_detail():
    try:
        data = request.json
        new_order_detail = OrderDetail(
            order_id=data.get('order_id'), 
            book_id=data.get('book_id'), 
            quantity=data.get('quantity'))
        db.session.add(new_order_detail)
        db.session.commit()
        return new_order_detail.to_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.delete('/api/order_details/<int:id>')
def delete_order_detail(id):
    order_detail = OrderDetail.query.get(id)
    if not order_detail:
        return {"error": "Order detail not found"}, 404
    db.session.delete(order_detail)
    db.session.commit()
    return {}, 204    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)