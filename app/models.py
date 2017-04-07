import db

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

db1 = db.db

book_author = db1.Table('book_author',
                        db1.Column('book_id', db1.Integer, db1.ForeignKey('author_id')),
                        db1.Column('author_id', db1.Integer, db1.ForeignKey('book_id')), 
                        db1.PrimaryKeyConstraint('book_id', 'author_id'))

pub_author = db1.Table('pub_author',
                        db1.Column('pub_id', db1.Integer, db1.ForeignKey('author_id')),
                        db1.Column('author_id', db1.Integer, db1.ForeignKey('pub_id')), 
                        db1.PrimaryKeyConstraint('pub_id', 'author_id'))

class Book(db1.Model):
    """Links to Author, Review, Publisher
       Book-Publisher is a one-to-many relationship,
       Book-Review is one-to-many
       Book-Author is many-to-many"""

    __tablename__ = 'book'

    id = db1.Column('id', db1.Integer, primary_key=True, autoincrement=True)
    title = db1.Column('title', db1.String(120))
    genre = db1.Column('genre', db1.String(120))
    year = db1.Column('year', db1.String(80))
    isbn = db1.Column('isbn', db1.String(80))
    prices = db1.Column('prices', db1.String(80))
    pic = db1.Column('pic',db1.String(120))
    pub_id = db1.Column('pub_id', db1.Integer, db1.ForeignKey('publisher.id'), nullable=False)

    #Many to Many
    authors = db1.relationship('Author', secondary='book_author', backref='book')
    #one to Many
    reviews = db1.relationship('Review', backref ='book', lazy='dynamic')

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
       Author-Book is a many-to-many relationship,
       Author-Publisher is many-to-many"""

    __tablename__ = 'author'

    id = db1.Column('id', db1.Integer, primary_key=True, autoincrement=True)
    name = db1.Column('name', db1.String(80), primary_key=True)
    birth_date = db1.Column('birth_date', db1.String(80))
    death_date = db1.Column('death_date', db1.String(80))
    pic = db1.Column('pic', db1.String(120))
    about = db1.Column('about', db1.Text)
    num_works = db1.Column('num_works', db1.String(80))

    #Many to Many
    publishers = db1.relationship('Author', secondary='pub_author', backref='publisher')
    
    #One to many
    reviews = db1.relationship('Review', backref ='author', lazy='dynamic')

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
       Publisher-Book is a many-to-one relationship
       Publisher-Author is many-to-many"""

    __tablename__ = 'publisher'

    id = db1.Column('id', db1.Integer, primary_key=True, autoincrement=True)
    name = db1.Column('name', db1.String(80))
    founding_date = db1.Column('founding_date', db1.String(80))
    headquarters = db1.Column('headquarters', db1.String(160))
    country = db1.Column('country', db1.String(120))
    founders = db1.Column('founders', db1.String(160))


    #Many to one
    books = db1.relationship('Books', backref ='publisher', lazy='dynamic')

    def __init__(self, name, founding_date, headquarters, country, founders):
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


class Review(db1.Model):
    """Links to Book, Author
       Review-Book and Review-Author are one-to-many relationships"""

    __tablename__ = 'review'   
    
    id = db1.Column('id', db1.Integer, primary_key=True, autoincrement=True)
    reviewer = db1.Column('reviewer', db1.String(80))
    rating = db1.Column('rating', db1.String(80))
    content = db1.Column('content', db1.Text)
    source = db1.Column('source', db1.String(80))
    book_id = db1.Column('book_id', db1.Integer, db1.ForeignKey('book.id'), nullable=False)
    author_id = db1.Column('author_id', db1.Integer, db1.ForeignKey('author.id'), nullable=False)


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