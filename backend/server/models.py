from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

#definitions of tables and associated schema constructs
metadata = MetaData()

# a Flask SQAlchemy extension
db = SQLAlchemy(metadata=metadata)