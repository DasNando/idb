from unittest import main, TestCase
from main import db, app
from models import Book, Publisher, Author, Review


class TestModels(TestCase):
    def test_book_model_1(self):
         #def __init__(self, title, genre, year, edition, isbn, prices):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data = Book("title", "genre", "year", 1, "ISBN", 1.0)

            db.session.add(data)
            db.session.commit()

            book = db.session.query(Book).filter_by(title="title").first()
            self.assertEqual(book.title, "title")
            self.assertEqual(book.year, "year")

            db.session.delete(data)
            db.session.commit()

    def test_book_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data1 = Book("title1", "publisher1", "genre1", "author1",
                         1900, 3, 1.1, 2.00)
            data2 = Book("title2", "publisher2", "genre2", "author2",
                         2017, 3, 1.1, 2.00)

            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()

            book = db.session.query(Book).filter_by(year=2017).first()
            self.assertEqual(book.author, "author2")
            self.assertEqual(book.publisher, "publisher2")

            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()

    def test_book_model_3(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data1 = Book("title1", "publisher1", "genre1", "author1",
                         1900, 3, 1.1, 2.00)
            data2 = Book("title2", "publisher2", "genre2", "author2",
                         2017, 3, 1.1, 2.00)

            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()

            book = db.session.query(Book).filter_by(title="title1").first()
            self.assertEqual(book.year, 1900)
            self.assertEqual(book.genre, "genre1")

            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()

    def test_author_model_1(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data = Author(True, "name", "birth_date", "death_date", "works",
                          "genre", "publisher")

            db.session.add(data)
            db.session.commit()

            author = db.session.query(Author).filter_by(birth_date="birth_date").first()
            self.assertEqual(author.name, "name")
            self.assertEqual(author.death_date, "death_date")

            db.session.delete(data)
            db.session.commit()

    def test_author_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data1 = Author(True, "name1", "birth_date1", "death_date1", "works1",
                           "genre1")
            data2 = Author(False, "name2", "birth_date2", "death_date2", "works2",
                           "genre2")

            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()

            author = db.session.query(Author).filter_by(alive=False).first()
            self.assertEqual(author.death_date, "death_date2")
            self.assertEqual(author.genre, "genre2")

            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()

    def test_author_model_3(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data1 = Author(True, "name1", "birth_date1", "death_date1", "works1",
                           "genre1")
            data2 = Author(False, "Ernest Hemingway", "1899", "1961", "For Whom The Bell Tolls",
                           "fiction")

            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()

            author = db.session.query(Author).filter_by(name="Ernest Hemingway").first()
            self.assertEqual(author.birth_date, "1899")
            self.assertEqual(author.genre, "fiction")

    def test_publisher_model_1(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data = Publisher("name", "founding_date", "headquarters", "country",
                             "founders", "books", "authors")

            db.session.add(data)
            db.session.commit()

            publisher = db.session.query(Publisher).filter_by(country="country").first()
            self.assertEqual(publisher.name, "name")
            self.assertEqual(publisher.founders, "founders")

            db.session.delete(data)
            db.session.commit()

    def test_publisher_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data1 = Publisher("name1", "founding_date1", "headquarters1", "country1",
                              "founders1", "books1", "authors1")
            data2 = Publisher("name2", "founding_date2", "headquarters2", "country2",
                              "founders2", "books2", "authors2")

            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()

            publisher = db.session.query(Publisher).filter_by(headquarters="headquarters2").first()
            self.assertEqual(publisher.books, "books2")
            self.assertEqual(publisher.founders, "founders2")

            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()

    def test_review_model_1(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data = Review("book", "author", "reviewer", 5.5,
                          "content", "source")

            db.session.add(data)
            db.session.commit()

            review = db.session.query(Review).filter_by(book="book").first()
            self.assertEqual(review.book, "book")
            self.assertEqual(review.rating, 5.5)

            db.session.delete(data)
            db.session.commit()

    def test_review_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data = Review("book", "author", "reviewer", 5.5,
                          "content", "source")
            data2 = Review("book2", "author2", "reviewer2", 6.6,
                           "content2", "source2")

            db.session.add(data)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()

            review = db.session.query(Review).filter_by(book="book").first()
            self.assertEqual(review.book, "book")
            self.assertEqual(review.content, "content")

            db.session.delete(data)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()

    # here for no reason yet, really
    '''def test_financial_org_dictionary_1(self):
    """Test dictionary method of financial org class"""

    example1 = Book("id", "name", "summary", "city", "companies", "twitter",
                            "website", "logo")
    dict_rep = example1.dictionary()

    self.assertEqual(dict_rep['financial_org_id'], "id")
    self.assertEqual(dict_rep['name'], "name")
    self.assertEqual(dict_rep['summary'], "summary")
    self.assertEqual(dict_rep['city'], "city")'''


if __name__ == "__main__":  # pragma: no cover
    main()
