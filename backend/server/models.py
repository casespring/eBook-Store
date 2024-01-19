from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string, datetime

#definitions of tables and associated schema constructs
metadata = MetaData()

# a Flask SQAlchemy extension
db = SQLAlchemy(metadata=metadata)



class Book(db.Model, SerializerMixin):
    __tablename__ = 'book_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
