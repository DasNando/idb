from .db import db

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

db1 = db

class Book(db1.Model):
    """Links to Author, Review, Publisher
       Book-Author and Book-Publisher are one-to-one relationships,
       Book-Review is one-to-many"""

    title = db1.Column(db1.String(120), primary_key=True)
    genre = db1.Column(db1.String(120))
    year = db1.Column(db1.String(80))
    isbn = db1.Column(db1.String(80))
    prices = db1.Column(db1.String(80))
    pic = db1.Column(db1.String(120))

    author_name = db1.Column(db1.String(80), db1.ForeignKey("author.name"))
    author = db1.relationship('Author', uselist=False, backref='book')

    publisher_name = db1.Column(db1.String(80), db1.ForeignKey("publisher.name"))
    publisher = db1.relationship('Publisher', uselist=False, backref='book')

    reviewer_name = db1.Column(db1.String(80), db1.ForeignKey("review.source"))
    reviews = db1.relationship('Review', backref='book')

    def __init__(self, title, genre, year, isbn, prices, pic):
        """All string data members are asserted to be of len > 0, price is asserted to be > 0"""

        self.title = title
        assert len(title) > 0

        self.genre = genre
        assert len(genre) > 0

        self.year = year
        assert len(year) > 0

        self.isbn = isbn

        self.prices = prices
        assert len(prices) > 0

        self.pic = pic


class Author(db1.Model):
    """Links to Book, Publisher
       Author-Book is a one-to-many relationship,
       Author-Publisher is one-to-one"""
    name = db1.Column(db1.String(80), primary_key=True)
    birth_date = db1.Column(db1.String(80))
    death_date = db1.Column(db1.String(80))
    pic = db1.Column(db1.String(120))
    about = db1.Column(db1.Text)
    num_works = db1.Column(db1.String(80))
    # genre = db1.Column(db1.String(80))

    # books = db1.Column()
    # works = db1.relationship('Book', backref='author', lazy='dynamic')
    publisher_name = db1.Column(db1.String(80), db1.ForeignKey("publisher.name"))
    publisher = db1.relationship('Publisher', uselist=False, backref='author')  # , lazy='dynamic')

    def __init__(self, name, birth_date, death_date, pic, about, num_works):
        """All string members are asserted to be of len > 0"""

        self.name = name
        assert len(name) > 0

        self.birth_date = birth_date
        assert len(birth_date) > 0

        self.death_date = death_date
        assert len(death_date) > 0

        self.pic = pic
        assert len(pic) > 0

        self.about = about
        assert len(about) > 0

        self.num_works = num_works
        assert len(num_works) > 0


class Publisher(db1.Model):
    """Links to Author, Book
       Publisher-Book and Publisher-Author are one-to-many relationships"""
    name = db1.Column(db1.String(80), primary_key=True)
    about = db1.Column(db1.Text)
    headquarters = db1.Column(db1.String(80))
    country = db1.Column(db1.String(80))
    founded = db1.Column(db1.String(80))

    # books = db1.relationship('Book', backref='publisher', lazy='dynamic')
    # authors = db1.relationship('Author', backref='publisher', lazy='dynamic')

    def __init__(self, name, about, date, country, hq):
        """All string members are asserted to be len > 0"""

        self.name = name
        assert len(self.name) > 0

        self.about = about
        assert len(self.about) > 0

        self.headquarters = hq
        assert len(self.headquarters) > 0

        self.country = country
        assert len(self.country) > 0

        self.founded = date
        assert len(self.founded) > 0


class Review(db1.Model):
    """Links to Book, Author
       Review-Book and Review-Author are one-to-one relationships"""
    reviewer = db1.Column(db1.String(80))
    rating = db1.Column(db1.String(80))
    content = db1.Column(db1.Text)
    source = db1.Column(db1.String(80), primary_key=True)

    # book_name = db1.Column(db1.String(80), db1.ForeignKey("book.title"))
    # book = db1.relationship('Book', uselist=False, backref='review', lazy='dynamic')

    author_name = db1.Column(db1.String(80), db1.ForeignKey("author.name"))
    author = db1.relationship('Author', uselist=False, backref='review')  # , lazy='dynamic')

    def __init__(self, reviewer, rating, content, source):
        """All string members are asserted to be len > 0, rating is asserted to be >= 0"""

        self.reviewer = reviewer
        assert len(reviewer) > 0

        self.rating = rating
        assert len(rating) > 0

        self.content = content
        assert len(content) > 0

        self.source = source
        assert len(source) > 0

# db1.create_all()
# Session = sessionmaker(autoflush=False)
