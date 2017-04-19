import json
import logging
import os
import codecs

from .db import db, app
from .models import Book, Author, Review, Publisher

reader = codecs.getreader("utf-8")

def path(f):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, '/scraper', f)
    return json_url


def init_db():
    logging.warning("We're in init_db")

    db.drop_all()
    db.create_all()

    # with open(path("test3.json")) as test_json:
    #	test_data = json.load(test_json)

    with app.open_resource('data/books.json') as books_json:
        books_data = json.load(reader(books_json))

    with app.open_resource("data/book_test3.json") as books3_json:
        books3_data = json.load(reader(books3_json))

    with app.open_resource("data/reviews.json") as reviews_json:
        review_data = json.load(reader(reviews_json))

    with app.open_resource("data/authors.json") as authors_json:
        author_data = json.load(reader(authors_json))

    with app.open_resource('data/authors3.json') as authors3_json:
        author3_data = json.load(reader(authors3_json), strict=False)

    with app.open_resource('data/publishers2.json') as publishers_json:
        publisher_data = json.load(reader(publishers_json), strict=False)

    authors = 0
    for item in author3_data['authors']:
        try:
            name = item["name"].strip()
            print('found author: ', name)
        except:
            # name = 'Something has gone horribly wrong and we were, sadly, unable to fetch the name for this author.'
            print('failed to find author')
            continue
        try:
            image = item["image_url"]
        except:
            image = "about:blank"
        try:
            about = item["about"]
        except:
            about = ''
        try:
            num_works = str(item["works_count"])
        except:
            num_works = '0'
        try:
            birthday = item["birthdate"]
        except:
            birthday = ''
        try:
            deathday = item['deathdate']
        except:
            deathday = ''

        author = Author(name, birthday, deathday, image, about, num_works)
        q = db.session.query(Author).filter_by(name=name)
        if not db.session.query(q.exists()).scalar():
            db.session.add(author)
            authors = authors + 1
            print('added author with name: ', name)
        else:
            print("couldn't add author with name: ", name)

    publishers = 0
    # publisher info
    for item in publisher_data['publishers']:
        try:
            name = str(item['name']).strip()
            if len(name) == 0:
                continue
        except:
            continue
        try:
            about = item['about']
            if len(about) == 0:
                about = 'unknown'
        except:
            about = ' '
        try:
            founded = item['founding_date'].strip()
            if len(founded) == 0:
                founded = 'unknown'
        except:
            founded = 'unknown'
        try:
            country = item['country'].strip()
            if len(country) == 0:
                country = 'unknown'
        except:
            country = 'unknown'
        try:
            hq = item['hq'].strip()
            if len(hq) == 0:
                hq = 'unknown'
        except:
            hq = 'unknown'

        print('creating publisher with hq: "', hq, '"')
        publisher = Publisher(name, about, founded, country, hq)
        q = db.session.query(Publisher).filter_by(name=name)
        if not db.session.query(q.exists()).scalar():
            db.session.add(publisher)
            publishers += 1
        else:
            print('Unable to add publisher with name: ', name)

    books = 0
    # pubs = set()
    for search in (books_data["books"] + books3_data['books']):
        for item in search['items']:
            # finding book info
            try:
                title = item["volumeInfo"]['title']
            except:
                print('error fetching title for book# ', books)
                continue
            # title = 'error fetching title'
            try:
                genre = item["volumeInfo"]['categories'][0]
            except:
                genre = 'error fetching genre'
            try:
                year = item["volumeInfo"]['publishedDate']
            except:
                year = 'error fetching year'
            try:
                isbn = item["volumeInfo"]['industryIdentifiers'][1]["identifier"]
            except:
                isbn = 'error fetching isbn'
            try:
                price = str(item["saleInfo"]["retailPrice"]['amount'])
            except:
                price = 'This title is not for sale.'
            try:
                pic = item["volumeInfo"]["imageLinks"]["thumbnail"]
            except:
                print('Error fetching image url')
                pic = 'about:blank'
            try:
                rating = str(item['volumeInfo']['averageRating'])
            except:
                rating = 'No ratings for this title.'
            try:
                author = item['volumeInfo']['authors'][0]
            except:
                print("shit i couldnt find the author for the book:", title)
                author = 'unknown'
            try:
                pub = item['volumeInfo']['publisher']
            except:
                pub = 'unknown'

            book = Book(title, genre, year, isbn, price, pic, rating, author, pub)
            q = db.session.query(Book).filter_by(title=title)
            if not db.session.query(q.exists()).scalar():
                db.session.add(book)
                books = books + 1
            else:
                print('Unable to add book with name: ', title)

            # open('../scraper/pub_names.txt', 'w').write(str(list(pubs)))

    # review initialization
    reviews = 0
    for item in review_data['reviews']:
        try:
            name = item['reviewer']
        except:
            name = 'unknown reviewer'
        try:
            rating = item['rating']
        except:
            rating = 'unknown rating'
        try:
            content = item['review']
        except:
            content = 'no content'
        try:
            source = item['source']
        except:
            source = 'unknown source'
        try:
        	book = item['title']
        except:
        	book = 'unknown'

        reviews = reviews + 1
        review = Review(name, rating, content, source, book)
        db.session.add(review)

    db.session.commit()
    logging.warning("added ", books, ' books')
    logging.warning('added ', authors, ' authors')
    logging.warning('added ', reviews, ' reviews')
    logging.warning('added ', publishers, ' publishers')


"""
import json

from .db import db
from .models import Book, Author, Review, Publisher


def path(f):
    return "../scraper/" + f


def init_db():
    db.drop_all()
    db.create_all()

    # with open(path("test3.json")) as test_json:
    #	test_data = json.load(test_json)

    with open(path("books.json")) as books_json:
        books_data = json.load(books_json)

    with open(path("book_test3.json")) as books3_json:
        books3_data = json.load(books3_json)

    with open(path("reviews.json")) as reviews_json:
        review_data = json.load(reviews_json)

    with open(path("authors.json")) as authors_json:
        author_data = json.load(authors_json)

    with open(path('authors3.json')) as authors3_json:
        author3_data = json.load(authors3_json, strict=False)

    with open(path('publishers2.json')) as publishers_json:
        publisher_data = json.load(publishers_json, strict=False)

    authors = 0
    for item in author3_data['authors']:
        try:
            name = item["name"].strip()
            print('found author: ', name)
        except:
            # name = 'Something has gone horribly wrong and we were, sadly, unable to fetch the name for this author.'
            print('failed to find author')
            continue
        try:
            image = item["image_url"]
        except:
            image = "about:blank"
        try:
            about = item["about"]
        except:
            about = ''
        try:
            num_works = str(item["works_count"])
        except:
            num_works = '0'
        try:
            birthday = item["birthdate"]
        except:
            birthday = ''
        try:
            deathday = item['deathdate']
        except:
            deathday = ''

        author = Author(name, birthday, deathday, image, about, num_works)
        q = db.session.query(Author).filter_by(name=name)
        if not db.session.query(q.exists()).scalar():
            db.session.add(author)
            authors = authors + 1
            print('added author with name: ', name)
        else:
            print("couldn't add author with name: ", name)

    publishers = 0
    # publisher info
    for item in publisher_data['publishers']:
        try:
            name = str(item['name']).strip()
            if len(name) == 0:
                continue
        except:
            continue
        try:
            about = item['about']
            if len(about) == 0:
                about = 'unknown'
        except:
            about = ' '
        try:
            founded = item['founding_date'].strip()
            if len(founded) == 0:
                founded = 'unknown'
        except:
            founded = 'unknown'
        try:
            country = item['country'].strip()
            if len(country) == 0:
                country = 'unknown'
        except:
            country = 'unknown'
        try:
            hq = item['hq'].strip()
            if len(hq) == 0:
                hq = 'unknown'
        except:
            hq = 'unknown'

        print('creating publisher with hq: "', hq, '"')
        publisher = Publisher(name, about, founded, country, hq)
        q = db.session.query(Publisher).filter_by(name=name)
        if not db.session.query(q.exists()).scalar():
            db.session.add(publisher)
            publishers += 1
        else:
            print('Unable to add publisher with name: ', name)

    books = 0
    for search in (books_data["books"] + books3_data['books']):
        for item in search['items']:
            # finding book info
            try:
                title = item["volumeInfo"]['title']
            except:
                print('error fetching title for book# ', books)
                continue
            try:
                genre = item["volumeInfo"]['categories'][0].strip().title()
            except:
                genre = 'error fetching genre'
            try:
                year = item["volumeInfo"]['publishedDate']
            except:
                year = 'error fetching year'
            try:
                isbn = item["volumeInfo"]['industryIdentifiers'][1]["identifier"]
            except:
                isbn = 'error fetching isbn'
            try:
                price = str(item["saleInfo"]["retailPrice"]['amount'])
            except:
                price = 'This title is not for sale.'
            try:
                pic = item["volumeInfo"]["imageLinks"]["thumbnail"]
            except:
                print('Error fetching image url')
                pic = 'No image availible.'
            try:
                rating = str(item['volumeInfo']['averageRating'])
            except:
                rating = 'No ratings for this title.'
            try:
                author = item['volumeInfo']['authors'][0]
            except:
                print("shit i couldnt find the author for the book:", title)
                author = 'unknown'
            try:
                pub = item['volumeInfo']['publisher']
            except:
                pub = 'unknown'

            book = Book(title, genre, year, isbn, price, pic, rating, author, pub)
            q = db.session.query(Book).filter_by(title=title)
            if not db.session.query(q.exists()).scalar():
                db.session.add(book)
                books = books + 1
            else:
                print('Unable to add book with name: ', title)

    # review initialization
    reviews = 0
    for item in review_data['reviews']:
        try:
            name = item['reviewer'].strip().title()
        except:
            name = 'unknown reviewer'
        try:
            rating = str(item['rating']).strip()
        except:
            rating = 'no rating'
        try:
            content = item['review'].strip()
        except:
            content = 'no content'
        try:
            source = item['source']
        except:
            source = 'unknown source'

        reviews = reviews + 1
        review = Review(name, rating, content, source)
        db.session.add(review)

    db.session.commit()
    print("added ", books, ' books')
    print('added ', authors, ' authors')
    print('added ', reviews, ' reviews')
    print('added ', publishers, ' publishers')
"""