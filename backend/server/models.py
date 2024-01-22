from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import validates
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
    # isbn = db.Column(db.String, unique=True)
    page_count = db.Column(db.Integer)
    summary = db.Column(db.Text)
    detail = db.Column(db.Text)
    table_of_contents = db.Column(db.Text)
    price = db.Column(db.Integer)
    published_date = db.Column(db.Date)
    book_image_file_path = db.Column(db.String)

    # book_image_id = db.Column(db.Integer, db.ForeignKey('book_image_table.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category_table.id'))


class User(db.Model, SerializerMixin):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    salt = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())


class Like(db.Model, SerializerMixin):
    __tablename__ = 'like_table'

    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'), primary_key=True)


class Cart(db.Model, SerializerMixin):
    __tablename__ = 'cart_table'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'))


class BookReview(db.Model, SerializerMixin):
    __tablename__ = 'book_review_table'

    id = db.Column(db.Integer, primary_key=True)
    reviewer = db.Column(db.String)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'))


# class BookImage(db.Model, SerializerMixin):
#     __tablename__ = 'book_image_table'

#     id = db.Column(db.Integer, primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'))
#     file_path = db.Column(db.String)


class Category(db.Model, SerializerMixin):
    __tablename__ = 'category_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)


class Order(db.Model, SerializerMixin):
    __tablename__ = 'order_table'

    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer)
    ordered_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery_table.id'))


class Delivery(db.Model, SerializerMixin):
    __tablename__ = 'delivery_table'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    recipient = db.Column(db.String)
    contact = db.Column(db.String)


class OrderDetail(db.Model, SerializerMixin):
    __tablename__ = 'order_detail_table'

    order_id = db.Column(db.Integer, db.ForeignKey('order_table.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_table.id'), primary_key=True)
    quantity = db.Column(db.Integer)

