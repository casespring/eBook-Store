from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import dotenv_values
from models import db, Book, User, Like, Cart, BookReview, Category, Order, Delivery, OrderDetail

app = Flask(__name__)
# config = dotenv_values('.env')
# app.secret_key = config['FLASK_SECRET_KEY']
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)



@app.route('/')
def home():
    return '<h1>Welcome to the eBook Store Database</h1>'

@app.route('/books')
def get_books():
    books = Book.query.all()
    return [book.to_dict() for book in books]

@app.route('/books/<int:id>')
def get_books_by_id(id):
    book = Book.query.filter(Book.id == id).first()
    if not book:
        return {"error": "Scientist not found"}
    return book.to_dict()

if __name__ == '__main__':
    app.run(port=5555, debug=True)