from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func

# Definitions of tables and associated schema constructs
metadata = MetaData()

# A Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)


class Book(db.Model, SerializerMixin):
    __tablename__ = 'book_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    author = db.Column(db.String(100))
    isbn = db.Column(db.String, unique=True)
    page_count = db.Column(db.Integer)
    summary = db.Column(db.Text)
    detail = db.Column(db.Text)
    table_of_contents = db.Column(db.Text)
    price = db.Column(db.Integer)
    published_date = db.Column(db.Date)
    book_image = db.Column(db.String)

    # book_image_id = db.Column(db.Integer, db.ForeignKey('book_image_table.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.id'))

    category = db.relationship("Category", back_populates="book")

    likes = db.relationship("Like", back_populates="book", cascade="all, delete-orphan")
    cart_list = db.relationship("Cart", back_populates="book", cascade="all, delete-orphan")
    book_review = db.relationship("BookReview", back_populates="book", cascade="all, delete-orphan")
    order_details = db.relationship("OrderDetail", back_populates="book")

    serialize_rules = ["-likes.book", "-cart_list.book"]

    def __repr__(self):
        return f"<Book {self.id}: {self.title}, {self.author}, {self.page_count}, {self.summary}, {self.detail}, {self.table_of_contents}, {self.price}, {self.published_date}, {self.book_image}, {self.category_id}>"

class User(db.Model, SerializerMixin):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    salt = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    
    likes = db.relationship("Like", back_populates="user", cascade="all, delete-orphan")
    cart_list = db.relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    orders = db.relationship("Order", back_populates="user", cascade="all, delete-orphan")

    serialize_rules = ["-likes.user", "-cart_list.user"]

    def __repr__(self):
        return f"<User {self.id}: {self.email}, {self.name}, {self.password}, {self.salt}, {self.created_at}>"
    
class Like(db.Model, SerializerMixin):
    __tablename__ = 'like_table'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'), primary_key=True)

    user = db.relationship("User", back_populates="likes")
    book = db.relationship("Book", back_populates="likes")

    serialize_rules = ["-user.likes", "-book.likes"]

    def __repr__(self):
        return f"<Like User {self.id}: {self.user_id}, Book:{self.book_id}>"

    
class Cart(db.Model, SerializerMixin):
    __tablename__ = 'cart_table'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'))

    user = db.relationship("User", back_populates="cart_list")
    book = db.relationship("Book", back_populates="cart_list")

    serialize_rules = ["-user.cart_table", "-book.cart_table"]

    def __repr__(self):
        return f"<Cart {self.id}: {self.quantity}, {self.user_id}, {self.book_id}>"
    
class BookReview(db.Model, SerializerMixin):
    __tablename__ = 'book_review_table'

    id = db.Column(db.Integer, primary_key=True)
    reviewer = db.Column(db.String)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'))

    book = db.relationship("Book", back_populates="book_review")

    def __repr__(self):
        return f"<Book Review {self.id}: {self.reviewer}, {self.comment}, {self.created_at}, {self.book_id}>"

# bookImage no need 
# class BookImage(db.Model, SerializerMixin):
#     __tablename__ = 'book_image_table'

#     id = db.Column(db.Integer, primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'))
#     file_path = db.Column(db.String)


class Category(db.Model, SerializerMixin):
    __tablename__ = 'category_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    book = db.relationship("Book", back_populates="category")

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"

class Order(db.Model, SerializerMixin):
    __tablename__ = 'order_table'

    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer)
    ordered_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery_table.id'))

    user = db.relationship("User", back_populates="orders")
    delivery = db.relationship("Delivery", back_populates="orders")
    order_details = db.relationship("OrderDetail", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}: {self.total_price}, {self.ordered_at}, {self.user_id}, {self.delivery_id}>"
    
class Delivery(db.Model, SerializerMixin):
    __tablename__ = 'delivery_table'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    recipient = db.Column(db.String)
    contact = db.Column(db.String)

    orders = db.relationship("Order", back_populates="delivery", cascade="all, delete-orphan")
    def __repr__(self):
        return f"<Delivery {self.id}: {self.address}, {self.recipient}, {self.contact}>"

class OrderDetail(db.Model, SerializerMixin):
    __tablename__ = 'order_detail_table'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order_table.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'), primary_key=True)
    quantity = db.Column(db.Integer)

    orders = db.relationship("Order", back_populates="order_details")
    book = db.relationship("Book", back_populates="order_details")

    

    def __repr__(self):
        return f"<Order Detail {self.id}: {self.order_id}, {self.book_id}, {self.quantity}>"

