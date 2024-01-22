from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import dotenv_values
from models import db

app = Flask(__name__)
# config = dotenv_values('.env')
# app.secret_key = config['FLASK_SECRET_KEY']
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)



@app.route('/')
def index():
    return '<h1>Welcome to the eBook Store</h1>'

@app.route('/books')
def get_book():
    pass

@app.route('/books/<init:id>')
def get_books_by_id(id):
    pass

@app.route('/user')
def get_user():
    pass



if __name__ == '__main__':
    app.run(port=5555, debug=True)