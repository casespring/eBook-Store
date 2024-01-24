from flask import Flask, make_response, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import dotenv_values
from models import db, Book, User, Like, Cart, BookReview, Category, Order, Delivery, OrderDetail
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from sqlalchemy.orm.exc import NoResultFound
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



@app.route('/')
def home():
    return '<h1>Welcome to the eBook Store Database</h1>'

#Books Crud
@app.route('/books')
def get_books():
    books = Book.query.all()
    return [book.as_dict() for book in books]

####################################   VALIDATION ##########################################



# CHECK SESSION
@app.get('/check_session')
def check_session():
    user = db.session.get(User, session.get('user_id'))
    print(f'check session {session.get("user_id")}')
    if user:
        return user.to_dict(rules=['-password']), 200
    else:
        return {"message": "No user logged in"}, 401

# LOGIN
@app.post('/login')
def login():
    data = request.json

    user = User.query.filter(User.name == data.get('name')).first()

    if user and bcrypt.check_password_hash(user.password, data.get('password')):
        session["user_id"] = user.id
        print("success")
        return user.to_dict(rules=['-password']), 200
    else:
        return { "error": "Invalid username or password" }, 401


####################################   VALIDATION ##########################################


@app.route('/books/<int:id>')
def get_book_by_id(id):
    book = Book.query.filter(Book.id == id).first()
    if not book:
        return {"error": "Book not found"}
    return book.as_dict()



@app.patch('/books/<int:id>')
def patch_book(id):
    book = db.session.get(Book, id)
    if not book:
        return {"error": "Book not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(book, attribute, data[attribute])
        db.session.add(book)
        db.session.commit()
        return book.as_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.post('/books')
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
        return new_book.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/books/<int:id>')
def delete_book(id):
    book = db.session.get(Book, id)
    if not book:
        return {"error": "Book not found"}, 404
    db.session.delete(book)
    db.session.commit()
    return {}, 204

#Users Crud
@app.route('/users')
def get_users():
    users = User.query.all()
    return [user.as_dict() for user in users]

@app.route('/users/<int:id>')
def get_users_by_id(id):
    user = User.query.filter(User.id == id).first()
    if not user:
        return {"error": "User not found"}
    return user.as_dict()

@app.patch('/users/<int:id>')
def patch_user(id):
    user = db.session.get(User, id)
    if not user:
        return {"error": "User not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(user, attribute, data[attribute])
        db.session.add(user)
        db.session.commit()
        return user.as_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

#when you need to check if a provided password matches the stored hash: 
    # check_password_hash(stored_hashed_password, provided_password)

@app.post('/users')
def post_user():
    try:
        data = request.json  
        hashed_password = generate_password_hash(data.get('password'), method='sha256')
        new_user = User(
            email=data.get('email'),
            name=data.get('name'),
            password=hashed_password,
            salt=data.get('salt'),
            created_at=data.get('created_at')
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/users/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)
    if not user:
        return {"error": "User not found"}, 404
    db.session.delete(user)
    db.session.commit()
    return {}, 204

#Likes Crud
@app.route('/likes', methods=['GET'])
def get_likes():
    likes = Like.query.all()
    return [like.as_dict() for like in likes]

@app.post('/likes')
def post_like():
    try:
        data = request.json
        new_like = Like(user_id=data.get('user_id'), book_id=data.get('book_id'))
        db.session.add(new_like)
        db.session.commit()
        return new_like.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/likes/<int:id>')
def delete_like(id):
    like = db.session.get(Like, id)
    if not like:
        return {"error": "Like not found"}, 404
    db.session.delete(like)
    db.session.commit()
    return {}, 204

#Carts Crud
@app.route('/carts/<int:user_id>')
def get_carts_by_user_id(user_id):
    try:
        carts = Cart.query.filter(Cart.user_id == user_id).all()
        if not carts:
            return {"error": "Empty cart found for the user"}, 404
        cart_info = [cart.as_dict() for cart in carts]
        return cart_info, 200
    except ValueError:
        return {"error": "User not found"}, 404

@app.patch('/carts/<int:id>')
def patch_cart(id):
    cart = db.session.get(Cart, id)
    if not cart:
        return {"error": "Cart not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(cart, attribute, data[attribute])
        db.session.add(cart)
        db.session.commit()
        return cart.as_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.post('/carts')
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
        return new_cart.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
# def post_cart():  checks for validations on routes
#     try:
#         data = request.json

#         # Check if required fields are present in the incoming JSON data
#         required_fields = ['quantity', 'user_id', 'book_id']
#         if not all(field in data for field in required_fields):
#             return make_response({"errors": ["Required fields are missing"]}, 400)

#         new_cart = Cart(
#             quantity=data['quantity'],
#             user_id=data['user_id'],
#             book_id=data['book_id']
#         )
#         db.session.add(new_cart)
#         db.session.commit()
#         return new_cart.as_dict(), 201
#     except ValueError:
#         return make_response({"errors": ["Validation errors"]}, 400)

@app.delete('/carts/<int:id>')
def delete_cart(id):
    cart = db.session.get(Cart, id)
    if not cart:
        return {"error": "Cart not found"}, 404
    db.session.delete(cart)
    db.session.commit()
    return {}, 204

#BookReview Crud
@app.route('/book_reviews/<int:book_id>')
def get_book_reviews_by_book_id(book_id):
    book = Book.query.get(book_id)
    if not book:
        return {"error": "Book not found"}, 404
    book_reviews = [review.as_dict() for review in book.book_review]
    return book_reviews, 200

@app.patch('/book_reviews/<int:id>')
def patch_book_review(id):
    book_review = db.session.get(BookReview, id)
    if not book_review:
        return {"error": "Book review not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(book_review, attribute, data[attribute])
        db.session.add(book_review)
        db.session.commit()
        return book_review.as_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.post('/book_reviews')
def post_book_review():
    try:
        data = request.json
        new_book_review = BookReview(reviewer=data.get('reviewer'), comment=data.get('comment'), created_at=data.get('created_at'), book_id=data.get('book_id'))
        db.session.add(new_book_review)
        db.session.commit()
        return new_book_review.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

@app.delete('/book_reviews/<int:id>')
def delete_book_review(id):
    book_review = db.session.get(BookReview, id)
    if not book_review:
        return {"error": "Book review not found"}, 404
    db.session.delete(book_review)
    db.session.commit()
    return {}, 204

#Orders Crud
@app.route('/orders/<int:user_id>')
def get_orders_by_user_id(user_id):
    try:
        orders = Order.query.filter(Order.user_id == user_id).all()
        if not orders:
            return {"error": "No orders found for the user"}, 404
        orders_info = [order.as_dict() for order in orders]
        return orders_info, 200
    except ValueError:
        return {"error": "User not found"}, 404

@app.route('/orders/<int:id>')
def get_orders_by_id(id):
    order = Order.query.filter(Order.id == id).first()
    if not order:
        return {"error": "Order not found"}
    return order.as_dict()

@app.patch('/orders/<int:id>')
def patch_order(id):
    order = db.session.get(Order, id)
    if not order:
        return {"error": "Order not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(order, attribute, data[attribute])
        db.session.add(order)
        db.session.commit()
        return order.as_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.post('/orders')
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
        return new_order.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.delete('/orders/<int:id>')
def delete_order(id):
    order = db.session.get(Order, id)
    if not order:
        return {"error": "Order not found"}, 404
    db.session.delete(order)
    db.session.commit()
    return {}, 204    

#Delivery Crud
@app.route('/deliveries')
def get_deliveries():
    deliveries = Delivery.query.all()
    return [delivery.as_dict() for delivery in deliveries]

@app.route('/deliveries/<int:id>')
def get_delivery_by_id(id):
    delivery = Delivery.query.filter(Delivery.id == id).first()
    if not delivery:
        return {"error": "Delivery not found"}
    return delivery.as_dict()

@app.patch('/deliveries/<int:id>')
def patch_delivery(id):
    delivery = db.session.get(Delivery, id)
    if not delivery:
        return {"error": "Delivery not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(delivery, attribute, data[attribute])
        db.session.add(delivery)
        db.session.commit()
        return delivery.as_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.post('/deliveries')
def post_delivery():
    try:
        data = request.json
        new_delivery = Delivery(
            address=data.get('address'), 
            recipient=data.get('recipient'), 
            contact=data.get('contact'))
        db.session.add(new_delivery)
        db.session.commit()
        return new_delivery.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.delete('/deliveries/<int:id>')
def delete_delivery(id):
    delivery = db.session.get(Delivery, id)
    if not delivery:
        return {"error": "Delivery not found"}, 404
    db.session.delete(delivery)
    db.session.commit()
    return {}, 204    

#OrderDetail Crud
@app.route('/order_details/<int:order_id>')
def get_order_details_by_order_id(order_id):
    try:
        order_details = OrderDetail.query.filter(OrderDetail.order_id == order_id).all()
        if not order_details:
            return {"error": "Empty details found for the order"}, 404
        cart_info = [order_detail.as_dict() for order_detail in order_details]
        return cart_info, 200
    except NoResultFound:
        return {"error": "Order not found"}, 404

@app.patch('/order_details/<int:id>')
def patch_order_detail(id):
    order_detail = db.session.get(OrderDetail, id)
    if not order_detail:
        return {"error": "Order detail not found"}, 404
    try:
        data = request.json
        for attribute in data:
            setattr(order_detail, attribute, data[attribute])
        db.session.add(order_detail)
        db.session.commit()
        return order_detail.as_dict(), 202
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.post('/order_details')
def post_order_detail():
    try:
        data = request.json
        new_order_detail = OrderDetail(
            order_id=data.get('order_id'), 
            book_id=data.get('book_id'), 
            quantity=data.get('quantity'))
        db.session.add(new_order_detail)
        db.session.commit()
        return new_order_detail.as_dict(), 201
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)
    
@app.delete('/order_details/<int:id>')
def delete_order_detail(id):
    order_detail = db.session.get(OrderDetail, id)
    if not order_detail:
        return {"error": "Order detail not found"}, 404
    db.session.delete(order_detail)
    db.session.commit()
    return {}, 204    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)