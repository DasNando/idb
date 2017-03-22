from main import db


"""
Models:

Book

Author:

Publisher:

Genre?
"""


# For more examples, refer to http://flask-sqlalchemy.pocoo.org/2.1/models/
# This is an example Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(160), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


# Two more, related models.
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person',
                                lazy='dynamic')


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


#########################################################
############### Our Models Start Here ###################
#########################################################
class Book(db.Model):
    """Links to Author, Review, Publisher"""
    title = db.Column(db.String(120))
    publisher = db.Column(db.String(120))
    genre = db.Column(db.String(120))  # This is multiple, so let's figure that out
    author = db.Column(db.String(80))
    year = db.Column(db.Integer)
    edition = db.Column(db.Integer)
    ISBN = db.Column(db.Float)
    prices = db.Column(db.Float)
    # cover_art = db.Column() ???

class Author(db.Model):
    """Links to Book, Publisher"""
    alive = db.Column(db.Boolean)  # ???
    name = db.Column(db.String(80))
    birth_date = db.Column(db.String(80)) # subject to change
    death_date = db.Column(db.String(80)) # ^^^
    works = db.Column(db.String(80)) # placeholder, NOT FINAL
    genre = db.Column(db.String(80))

class Publisher():
    """Links to Author, Book"""
    name = db.Column(db.String(80))
    founding_date = db.Column(db.String(80))  # subject to change
    headquarters = db.Column(db.String(160))
    country = db.Column(db.String(120))
    founders = db.Column(db.Column(db.String(160)))  # placeholder, NOT FINAL
    books = db.Column(db.String(80))   # ^^^
    authors = db.Column(db.String(80))  # ^^^
