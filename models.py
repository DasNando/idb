from main import db


"""
Models:

Book

Author:

Publisher:

Reviews:
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
    title = db.Column(db.String(120), primary_key = True)
    publisher = db.relationship('Publisher', uselist = False, backref = 'book', lazy = 'dynamic')#db.Column(db.String(120))
    genre = db.Column(db.String(120))  # This is multiple, so let's figure that out
    author = db.relationship('Author', uselist = False, backref = 'book', lazy = 'dynamic')#db.Column(db.String(80))
    year = db.Column(db.Integer)
    edition = db.Column(db.Integer)
    ISBN = db.Column(db.String(80))
    prices = db.Column(db.Float)
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic')
    # cover_art = db.Column() ???

    def __init__(self, title, publisher, genre, author, year, edition, ISBN, prices, reviews):
        self.title = title
        assert(len(title) > 0)

        self.publisher = publisher

        self.genre = genre
        assert(len(genre) > 0)

        self.author = author

        self.year = year
        assert(year > 0 && year < 2018)

        self.edition = edition
        assert(edition > 0)

        self.ISBN = ISBN
        assert(len(ISBN) > 0)

        self.prices = prices
        assert(prices > 0)

        self.reviews = reviews

class Author(db.Model):
    """Links to Book, Publisher"""
    alive = db.Column(db.Boolean)  # ???
    name = db.Column(db.String(80), primary_key = True)
    birth_date = db.Column(db.String(80)) # subject to change
    death_date = db.Column(db.String(80)) # ^^^
    works = db.relationship('Book', backref = 'author', lazy = 'dynamic')#db.Column(db.String(80)) # placeholder, NOT FINAL
    genre = db.Column(db.String(80))
    publisher = db.relationship('Publisher', uselist = False, backref = 'author', lazy = 'dynamic')

    def __init__(self, alive, name, birth_date, death_date, works, genre, publisher):
        self.alive = alive
        assert(type(alive) == type(True))

        self.name = name
        assert(len(name) > 0)

        self.birth_date = birth_date
        assert(len(birth_date) > 0)

        self.death_date = death_date
        assert(len(death_date) > 0)

        self.works = works

        self.genre = genre
        assert(len(genre) > 0)

        self.publisher = publisher

class Publisher(db.Model):
    """Links to Author, Book"""
    name = db.Column(db.String(80), primary_key = True)
    founding_date = db.Column(db.String(80))  # subject to change
    headquarters = db.Column(db.String(160))
    country = db.Column(db.String(120))
    founders = db.Column(db.Column(db.String(160)))  # placeholder, NOT FINAL
    books = db.relationship('Book', backref = 'publisher', lazy = 'dynamic')#db.Column(db.String(80))   # ^^^
    authors = db.relationship('Author', backref = 'publisher', lazy = 'dynamic')#db.Column(db.String(80))  # ^^^

    def __init__(self, name, founding_date, headquarters, country, founders, books, authors):
        self.name = name
        assert(len(name) > 0)

        self.founding_date = founding_date
        assert(len(founding_date) > 0)

        self.headquarters = headquarters
        assert(len(headquarters) > 0)

        self.country = country
        assert(len(country) > 0)

        self.founders = founders
        assert(len(founders) > 0)

        self.books = books

        self.authors = authors

class Review(db.Model):
    """Links to Book, Author"""
    book = db.relationship('Book', uselist = False, backref = 'review', lazy = 'dynamic')
    author = db.relationship('Author', uselist = False, backref = 'review', lazy = 'dynamic')
    reviewer = db.Column(db.String(80))
    rating = db.Column(db.Float)
    content = db.Column(db.Text)
    source = db.Column(db.String(80))

    def __init__(self, book, author, reviewer, rating, content, source):
        self.book = book
        self.author = author

        self.reviewer = reviewer
        assert(len(reviewer) > 0)

        self.rating = rating
        assert(rating > 0)

        self.content = content
        assert(len(content) > 0)

        self.source = source
        assert(len(source) > 0)