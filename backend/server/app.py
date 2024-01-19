from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Mi

@app.route('/')
def index():
    return '<h1>Welcome to the eBook Store</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)