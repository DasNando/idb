from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
# postgresql://scott:tiger@localhost/mydatabase
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:swereaders@35.184.110.238:5432/postgres'
db = SQLAlchemy(app)