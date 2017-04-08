from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
# dialect+driver://username:password@host:port/database
# postgresql://scott:tiger@localhost/mydatabase
app.config.from_json(os.getcwd() + "/config.json")
db = SQLAlchemy(app)
