from unittest import main, TestCase
from .db import app, db
from .models import Book, Publisher, Author, Review


class TestModels(TestCase):
    def test_book_model_1(self):
         #def __init__(self, title, genre, year, isbn, prices, pic):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            data = Book("title", "genre", "year", "ISBN", "$1", "pic")

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
            data1 = Book("title1", "genre1", "year1", "isbn1",
                         "$1.00", "pic.jpg")
            data2 = Book("title2", "genre2", "year2", "isbn2",
                         "$2.00", "pic2.jpg")
    
            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()
    
            book = db.session.query(Book).filter_by(year="year2").first()
            self.assertEqual(book.author, "author2")
    
            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()
    
    def test_book_model_3(self):
        """Test querying the database by attribute using simple keywords"""
    
        with app.test_request_context():
            data1 = Book("title1", "genre1", "year1", "isbn1",
                         "$1.00", "pic.jpg")
            data2 = Book("title2", "genre2", "year2", "isbn2",
                         "$2.00", "pic2.jpg")
    
            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()
    
            book = db.session.query(Book).filter_by(title="title1").first()
            self.assertEqual(book.year, "year1")
            self.assertEqual(book.genre, "genre1")
    
            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()
    
    def test_author_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with app.test_request_context():
            data = Author("name", "birth_date", "death_date", "pic",
                          "about", "13")
    
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
            data1 = Author("name1", "birth_date1", "death_date1", "pic1",
                           "about1", "1")
            data2 = Author("name2", "birth_date2", "death_date2", "pic2",
                           "about2", "2")
    
            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()
    
            author = db.session.query(Author).filter_by(name="name2").first()
            self.assertEqual(author.death_date, "death_date2")
            self.assertEqual(author.about, "about2")
    
            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()
    
    def test_author_model_3(self):
        """Test querying the database by attribute using simple keywords"""
    
        with app.test_request_context():
            data1 = Author("name1", "birth_date1", "death_date1", "pic1",
                           "about1", "1")
            data2 = Author("name2", "birth_date2", "death_date2", "pic2",
                           "about1", "2")
    
            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()
    
            author = db.session.query(Author).filter_by(name="name2").first()
            self.assertEqual(author.birth_date, "birth_date2")
            self.assertEqual(author.pic, "pic2")
    
    def test_publisher_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with app.test_request_context():
            data = Publisher("name", "about", "date", "country",
                             "hq")
    
            db.session.add(data)
            db.session.commit()
    
            publisher = db.session.query(Publisher).filter_by(country="country").first()
            self.assertEqual(publisher.name, "name")
            self.assertEqual(publisher.about, "about")
    
            db.session.delete(data)
            db.session.commit()
    
    def test_publisher_model_2(self):
        """Test querying the database by attribute using simple keywords"""
    
        with app.test_request_context():
            data1 = Publisher("name1", "about1", "date1", "country1",
                              "hq1")
            data2 = Publisher("name2", "about2", "date2", "country2",
                              "hq2")
    
            db.session.add(data1)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()
    
            publisher = db.session.query(Publisher).filter_by(headquarters="hq1").first()
            self.assertEqual(publisher.name, "name1")
            self.assertEqual(publisher.about, "about1")
    
            db.session.delete(data1)
            db.session.commit()
            db.session.delete(data2)
            db.session.commit()
    
    def test_review_model_1(self):
        """Test querying the database by attribute using simple keywords"""
    
        with app.test_request_context():
            data = Review("reviewer", "rating", "content", "source")
    
            db.session.add(data)
            db.session.commit()
    
            review = db.session.query(Review).filter_by(rating="rating").first()
            self.assertEqual(review.reviewer, "reviewer")
            self.assertEqual(review.content, "content")
    
            db.session.delete(data)
            db.session.commit()
    
    def test_review_model_2(self):
        """Test querying the database by attribute using simple keywords"""
    
        with app.test_request_context():
            data = Review("reviewer1", "rating1", "content1", "source1")
            data2 = Review("reviewer2", "rating2", "content2", "source2")
    
            db.session.add(data)
            db.session.commit()
            db.session.add(data2)
            db.session.commit()
    
            review = db.session.query(Review).filter_by(content="content1").first()
            self.assertEqual(review.source, "source1")
            self.assertEqual(review.rating, "rating1")
    
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


if __name__=='__main__':
     main(exit=False)