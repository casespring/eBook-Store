from app import app
from models import db, Book, User, Like, Cart, BookReview, Category, Order, Delivery, OrderDetail
from random import choice, randint, choice as rc
import json
from datetime import datetime
import random
from faker import Faker
from sqlalchemy.sql import func 
from flask_bcrypt import Bcrypt
# regular seed.py
# if __name__ == "__main__":
#     with app.app_context():
#         with open("db.json") as f:
#             data = json.load(f)

#         OrderDetail.query.delete()
#         Order.query.delete()
#         Cart.query.delete()
#         Like.query.delete()
#         BookReview.query.delete()
#         User.query.delete()
#         Book.query.delete()
#         Category.query.delete()
#         Delivery.query.delete()

#         book_list = []
#         book_review_list = []
#         user_data = []
#         order_data = []

#         #categories first
#         category_list = []
#         for category_data in data.get("categories", []):
#             category = Category(name=category_data.get("name"))
#             category_list.append(category)
#         db.session.add_all(category_list)
#         db.session.commit()

#         for book in data["books"]:
#             b = Book(
#                 title = book.get('title'),
#                 author = book.get('author'),
#                 isbn = book.get('isbn'),
#                 # page_count = book.get('page_count'),
#                 # summary = book.get('summary'),
#                 # detail = book.get('detail'),
#                 # table_of_contents = book.get('table_of_contents'),
#                 # price = book.get('price'),
#                 # published_date = book.get('published_date')
#             )
#             book_list.append(b)
#         db.session.add_all(book_list)
#         db.session.commit()

#         for review in data["book_review"]:
#             date_string = review.get('created_at')
#             date_format = "%m/%d/%Y"
#             date_object = datetime.strptime(date_string, date_format)
#             r = BookReview(
#                 reviewer=review.get('reviewer'),
#                 comment=review.get('comment'),
#                 created_at= date_object,
#             )
#             book_review_list.append(r)
#         db.session.add_all(book_review_list)
#         db.session.commit()


#         for user in data["user"]:
#         # for user in user_data:
#             u = User(
#                 email = user.get('email'),
#                 name = user.get('name'),
#                 password = user.get('password'),
#             )
#             user_data.append(u)
#         db.session.add_all(user_data)
#         db.session.commit()

#         for order in data["order"]:
#             # for od in order_data:
#             o = Order(
#                 total_price = order.get('total_price')
#             )
#             order_data.append(o)
#         db.session.add_all(order_data)
#         db.session.commit()


# Using random and faker to libaries to generate info 
fake = Faker()

def seed_categories():
    category_names = ["Fiction", "Science Fiction", "Mystery", "Thriller", "Romance", "Fantasy"]
    for category_name in category_names:
        existing_category = Category.query.filter_by(name=category_name).first()
        if not existing_category:
            category = Category(name=category_name)
            db.session.add(category)
    db.session.commit()

def seed_books(num_books=5):
    categories = Category.query.all()
    book_list = []

    for _ in range(num_books):
        title = fake.word()
        used_titles = set()
        while title in used_titles:
            title = fake.word()

        # Check if a book with the same title already exists
        # existing_book = Book.query.filter_by(title=title).first()
        print(title)
        if title not in used_titles:
            # Insert the book if no duplicate title found
            book = Book(
                title=title,
                author=fake.name(),
                isbn=fake.isbn13(),
                page_count=fake.random_int(min=100, max=500),
                summary=fake.text(),
                detail=fake.text(),
                table_of_contents=fake.text(),
                price=fake.random_int(min=10, max=50),
                published_date=fake.date_between(start_date='-2y', end_date='today'),
                book_image=fake.image_url(),
                category=choice(categories)
            )
            book_list.append(book)
            used_titles.add(title)
    db.session.add_all(book_list)
    db.session.commit()

def seed_users(bcrypt, num_users=5):
    user_list = []

    for i in range(num_users):
        user = User(
            email=fake.email(),
            name=str(i),
            password=bcrypt.generate_password_hash(str(i)),
        )
        user_list.append(user)

    db.session.add_all(user_list)
    db.session.commit()

def seed_likes(num_likes=5):
    users = User.query.all()
    books = Book.query.all()

    like_list = set()

    while len(like_list) < num_likes:
        user = choice(users)
        book = choice(books)
        
        # Check if the like already exists
        existing_like = Like.query.filter_by(user_id=user.id, book_id=book.id).first()

        if existing_like is None:
            # Add a new like
            new_like = Like(user_id=user.id, book_id=book.id)
            like_list.add(new_like)

    db.session.bulk_save_objects(like_list)
    db.session.commit()


def seed_carts(num_carts=15):
    users = User.query.all()
    books = Book.query.all()
    cart_list = []

    for _ in range(num_carts):
        cart = Cart(
            quantity=fake.random_int(min=1, max=5),
            user=choice(users),
            book=choice(books),
        )
        cart_list.append(cart)

    db.session.add_all(cart_list)
    db.session.commit()

def seed_reviews(num_reviews=20):
    users = User.query.all()
    books = Book.query.all()
    reviews_list = []

    for _ in range(num_reviews):
        review = BookReview(
            rating=fake.random_int(min=1, max=5),
            comment=fake.text(),
            reviewer=random.choice(users).name,  
            created_at=fake.date_time_this_decade(),
            book=random.choice(books),
        )
        reviews_list.append(review)

    db.session.add_all(reviews_list)
    db.session.commit()

def seed_orders(num_orders=10):
    users = User.query.all()
    deliveries = Delivery.query.all()
    order_list = []

    for _ in range(num_orders):
        order = Order(
            total_price=fake.random_int(min=50, max=200),
            ordered_at=fake.date_time_this_decade(),
            user=choice(users),
            delivery=choice(deliveries),
        )
        order_list.append(order)

    db.session.add_all(order_list)
    db.session.commit()

def seed_deliveries(num_deliveries=5):
    delivery_list = []

    for _ in range(num_deliveries):
        delivery = Delivery(
            address=fake.address(),
            recipient=fake.name(),
            contact=fake.phone_number(),
        )
        delivery_list.append(delivery)

    db.session.add_all(delivery_list)
    db.session.commit()

def seed_order_details():
    # Your seeding logic here
    order_id = 2
    book_id = 4
    quantity = 3

    # Check if the record already exists
    existing_order_detail = OrderDetail.query.filter_by(order_id=order_id, book_id=book_id).first()

    if existing_order_detail is None:
        # Record doesn't exist, proceed with insertion
        new_order_detail = OrderDetail(order_id=order_id, book_id=book_id, quantity=quantity)
        db.session.add(new_order_detail)
        db.session.commit()
    else:
        # Record already exists, handle accordingly
        print(f"Record for order_id={order_id}, book_id={book_id} already exists.")

if __name__ == "__main__":
    with app.app_context():
        bcrypt = Bcrypt(app)
        Book.query.delete()
        Category.query.delete()
        User.query.delete()
        Like.query.delete()
        Cart.query.delete()
        BookReview.query.delete()
        Delivery.query.delete()
        Order.query.delete()
        OrderDetail.query.delete()

        seed_categories()
        seed_books()
        seed_users(bcrypt)
        seed_likes()
        seed_carts()
        seed_reviews()
        seed_deliveries()
        seed_orders()
        seed_order_details()