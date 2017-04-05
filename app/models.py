from db import db

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-arguments
# pylint: disable = too-many-instance-attributes
# pylint: disable = pointless-string-statement
# pylint: disable = missing-docstring

"""
Models:

Book
Author
Publisher
Reviews
"""


class Book(db.Model):
    """Links to Author, Review, Publisher
       Book-Author and Book-Publisher are one-to-one relationships,
       Book-Review is one-to-many"""
    title = db.Column(db.String(120), primary_key=True)    
    genre = db.Column(db.String(120))
    year = db.Column(db.Integer)
    edition = db.Column(db.Integer)
    isbn = db.Column(db.String(80))
    prices = db.Column(db.Float)

    author = db.relationship('Author', uselist=False, backref='book', lazy='dynamic')
    publisher = db.relationship('Publisher', uselist=False, backref='book', lazy='dynamic')
    reviews = db.relationship('Review', backref='book', lazy='dynamic')

    def __init__(self, title, genre, year, edition, isbn, prices):
        """All string data members are asserted to be of len > 0, price is asserted to be > 0"""

        self.title = title
        assert len(title) > 0

        self.genre = genre
        assert len(genre) > 0

        self.year = year
        assert 0 < year < 2018

        self.edition = edition
        assert edition > 0

        self.isbn = isbn
        assert len(isbn) > 0

        self.prices = prices
        assert prices > 0
        

class Author(db.Model):
    """Links to Book, Publisher
       Author-Book is a one-to-many relationship,
       Author-Publisher is one-to-one"""
    alive = db.Column(db.Boolean)
    name = db.Column(db.String(80), primary_key=True)
    birth_date = db.Column(db.String(80))  # subject to change
    death_date = db.Column(db.String(80))  # ^^^
    works = db.relationship('Book', backref='author',
                            lazy='dynamic')
    genre = db.Column(db.String(80))
    publisher = db.relationship('Publisher', uselist=False, backref='author', lazy='dynamic')

    def __init__(self, alive, name, birth_date, death_date, works, genre, publisher):
        """All string members are asserted to be of len > 0"""

        self.alive = alive

        self.name = name
        assert len(name) > 0

        self.birth_date = birth_date
        assert len(birth_date) > 0

        self.death_date = death_date
        assert len(death_date) > 0

        self.works = works

        self.genre = genre
        assert len(genre) > 0

        self.publisher = publisher


class Publisher(db.Model):
    """Links to Author, Book
       Publisher-Book and Publisher-Author are one-to-many relationships"""
    name = db.Column(db.String(80), primary_key=True)
    founding_date = db.Column(db.String(80))
    headquarters = db.Column(db.String(160))
    country = db.Column(db.String(120))
    founders = db.Column(db.String(160))
    books = db.relationship('Book', backref='publisher', lazy='dynamic')
    authors = db.relationship('Author', backref='publisher', lazy='dynamic')

    def __init__(self, name, founding_date, headquarters, country, founders, books, authors):
        """All string members are asserted to be len > 0"""

        self.name = name
        assert len(name) > 0

        self.founding_date = founding_date
        assert len(founding_date) > 0

        self.headquarters = headquarters
        assert len(headquarters) > 0

        self.country = country
        assert len(country) > 0

        self.founders = founders
        assert len(founders) > 0

        self.books = books

        self.authors = authors

class Review(db.Model):
    """Links to Book, Author
       Review-Book and Review-Author are one-to-one relationships"""
    reviewer = db.Column(db.String(80), primary_key=True)
    rating = db.Column(db.Float)
    content = db.Column(db.String(80))
    source = db.Column(db.String(80))
    book = db.relationship('Book', uselist=False, backref='review', lazy='dynamic')
    author = db.relationship('Author', uselist=False, backref='review', lazy='dynamic')

    def __init__(self, book, author, reviewer, rating, content, source):
        """All string members are asserted to be len > 0, rating is asserted to be > 0"""
        self.book = book
        self.author = author

        self.reviewer = reviewer
        assert len(reviewer) > 0

        self.rating = rating
        assert rating > 0

        self.content = content
        assert len(content) > 0

        self.source = source
        assert len(source) > 0

Session = sessionmaker(autoflush=False)
