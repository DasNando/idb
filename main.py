from flask import render_template, jsonify, request
import logging
import requests
import json
import datetime
import socket
import sqlalchemy
from app import db, models, setup_db
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()

db1 = db.db
app = db.app


def is_ipv6(addr):
    """Checks if a given address is an IPv6 address."""
    try:
        socket.inet_pton(socket.AF_INET6, addr)
        return True
    except socket.error:
        return False


class Visit(db1.Model):
    id = db1.Column(db1.Integer, primary_key=True)
    timestamp = db1.Column(db1.DateTime())
    user_ip = db1.Column(db1.String(46))

    def __init__(self, timestamp, user_ip):
        self.timestamp = timestamp
        self.user_ip = user_ip


@app.route('/db_test')
def index():
    db1.create_all()
    # setup_db.init_db()
    user_ip = request.remote_addr

    # Keep only the first two octets of the IP address.
    if is_ipv6(user_ip):
        user_ip = ':'.join(user_ip.split(':')[:2])
    else:
        user_ip = '.'.join(user_ip.split('.')[:2])

    visit = Visit(
        user_ip=user_ip,
        timestamp=datetime.datetime.utcnow()
    )

    db1.session.add(visit)
    db1.session.commit()

    visits = Visit.query.order_by(sqlalchemy.desc(Visit.timestamp)).limit(10)

    results = [
        'Time: {} Addr: {}'.format(x.timestamp, x.user_ip)
        for x in visits]

    output = 'Last 10 visits:\n{}'.format('\n'.join(results))

    return output, 200, {'Content-Type': 'text/plain; charset=utf-8'}


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/authors')
def authors():
    return render_template('authors.html')


@app.route('/books')
def books():
    return render_template('books.html')  # , book_pics=iter(books), item=None)


@app.route('/publishers')
def publishers():
    return render_template('publishers.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/search')
def search():
    return render_template('search.html')


# my token: wpV_1One91F2XNwmI6ukIg
@app.route('/run_tests')
def run_tests():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Travis-API-Version': '3',
        'Authorization': 'token wpV_1One91F2XNwmI6ukIg',
    }

    data = '{"request": {"branch": "master"}}'
    requests.post('https://api.travis-ci.org/repo/DasNando%2Fidb/requests', headers=headers, data=data)

    return "<a href=\"https://travis-ci.org/DasNando/idb\">See Results</a>"
    # tests_output = subprocess.check_output(['make', 'test'])
    # print tests_output
    # # print res.text
    # # dict_from_server = res.json()
    # return 'testoutput: ' + tests_output

    # return "server response: " + res.text + "dict_from_server: " + str(dict_from_server)

    # return render_template('search.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


#################### API SECTION

book = {"book_test": "book_name"}


# get book with arbitrary filters
@app.route('/api/books_test/')
@app.route('/api/books_test/<int:lim>')
def get_book1(lim=0):
    if not lim:
        lim = 10
    result = []
    for item in models.Book.query.limit(lim).all():
        b_json = dict()
        b_json['title'] = item.title
        b_json['genre'] = item.genre
        result.append(b_json)
    return jsonify(result)

    # b_dict_list = []
    # p = db1.query(models.Book).limit(lim)
    # print type(p)
    #
    # for b in p:
    #      b_dict_list.append(
    #          {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic})
    #     #b_dict_list.append(
    #     #    {"title": "dummy_title", "genre": "dummy_genre", "year": "dummy_year", "isbn": "dummy_isbn", "prices": "dummy_prices", "pic": "dummy_pic"})
    # return jsonify(b_dict_list)


# get all books
@app.route('/api/books/all/')
def get_book0():
    b_dict_list = []

    book = models.Book.query.all()
    for b in book:
        b_dict_list.append(
            {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic,
             "author": b.author_name, "publisher": b.publisher_name, "rating": b.rating})
    # print book.title models.Book.query.limit(lim).all()
    return jsonify(b_dict_list)


# get one book
@app.route('/api/books/title=<string:book_name>')
def get_book2(book_name):
    b_dict_list = []

    book_name = "%" + book_name + "%"
    book = models.Book.query.filter(models.Book.title.ilike(book_name)).all()
    for b in book:
        b_dict_list.append(
            {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic,
             "author": b.author_name, "publisher": b.publisher_name, "rating": b.rating})
    # print book.title models.Book.query.limit(lim).all()
    return jsonify(b_dict_list)


# get book with arbitrary filters
@app.route('/api/books/params&<string:params>')
def get_book3(params):
    commands = params.split('&')
    b_dict_list = []
    p = models.Book.query
    # print type(p)

    for item in commands:
        col, fil = item.split('=')
        fil = "%" + fil + "%"
        if col in models.Book.__table__.columns.keys():
            p = p.filter(getattr(models.Book, col).ilike(fil))
    for b in p:
        b_dict_list.append(
            {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic,
             "author": b.author_name, "publisher": b.publisher_name, "rating": b.rating})
    return jsonify(b_dict_list)


@app.route('/book/title=<string:book_title>')
def book_info2(book_title):
    return render_template('book.html')


@app.route('/review/title=<string:book_title>')
def review_info2(book_title):
    return render_template('review.html')


@app.route('/author/name=<string:author_name>')
def author_info2(author_name):
    return render_template('author.html')


@app.route('/publisher/name=<string:pub_name>')
def publisher_info2(pub_name):
    return render_template('publisher.html')


# get all authors
@app.route('/api/authors/all/')
def get_auth0():
    a_dict_list = []

    author = models.Author.query.all()
    for b in author:
        a_dict_list.append({"name": b.name, "birth_date": b.birth_date, "death_date": b.death_date, "pic": b.pic,
                            "about": b.about, "num_works": b.num_works})
    return jsonify(a_dict_list)


# @app.route('/api/books/title=<string:book_name>')
# def get_book2(book_name):
#     b_dict_list = []
#
#     book_name = "%" + book_name + "%"
#     book = models.Book.query.filter(models.Book.title.ilike(book_name)).all()
#     for b in book:
#         b_dict_list.append(
#             {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic,
#              "author": b.author_name, "publisher": b.publisher_name, "rating": b.rating})
#     # print book.title models.Book.query.limit(lim).all()
#     return jsonify(b_dict_list)

# get one Author
@app.route('/api/authors/name=<string:auth>')
def get1(auth):
    # a_dict_list = []
    # auth = "&" + auth + "%"
    # print('Auth is ' + auth)
    # author = models.Author.query.filter(models.Author.name.ilike(auth)).all()
    # # book = models.Book.query.filter(models.Book.title.ilike(book_name)).all()
    # for b in author:
    #     a_dict_list.append({"name": b.name, "birth_date": b.birth_date, "death_date": b.death_date, "pic": b.pic,
    #                         "about": b.about, "num_works": b.num_works})
    # print('author length? %d', len(author))
    return get2("name=" + auth)


# get author with arbitrary filters
@app.route('/api/authors/params&<string:params>')
def get2(params):
    commands = params.split('&')
    a_dict_list = []
    p = models.Author.query
    # print type(p)

    for item in commands:
        col, fil = item.split('=')
        fil = "%" + fil + "%"
        if col in models.Author.__table__.columns.keys():
            p = p.filter(getattr(models.Author, col).ilike(fil))
    for b in p:
        a_dict_list.append({"name": b.name, "birth_date": b.birth_date, "death_date": b.death_date, "pic": b.pic,
                            "about": b.about, "num_works": b.num_works})
    return jsonify(a_dict_list)


# get all Publishers
@app.route('/api/publishers/all/')
def get_pub0():
    p_dict_list = []

    publisher = models.Publisher.query.all()
    for b in publisher:
        p_dict_list.append(
            {"name": b.name, "founding_date": b.founded, "headquarters": b.headquarters, "country": b.country,
             "about": b.about})
    return jsonify(p_dict_list)


# get one Publisher
@app.route('/api/publishers/name=<string:publisher_name>')
def get3(publisher_name):
    p_dict_list = []
    publisher_name = "%" + publisher_name + "%"

    publisher = models.Publisher.query.filter(models.Publisher.name.ilike(publisher_name)).all()
    # book = models.Book.query.filter_by(title=book_name).all()
    for b in publisher:
        p_dict_list.append(
            {"name": b.name, "founding_date": b.founded, "headquarters": b.headquarters, "country": b.country,
             "about": b.about})
    return jsonify(p_dict_list)


# get book with arbitrary filters
@app.route('/api/publishers/params&<string:params>')
def get5(params):
    commands = params.split('&')
    p_dict_list = []
    p = models.Publisher.query
    # print type(p)

    for item in commands:
        col, fil = item.split('=')
        fil = "%" + fil + "%"
        if col in models.Publisher.__table__.columns.keys():
            p = p.filter(getattr(models.Publisher, col).ilike(fil))
    for b in p:
        p_dict_list.append(
            {"name": b.name, "founding_date": b.founded, "headquarters": b.headquarters, "country": b.country,
             "about": b.about})
    return jsonify(p_dict_list)


# get all reviews
@app.route('/api/reviews/all/')
def get6():
    r_dict_list = []

    reviews = models.Review.query.all()
    for r in reviews:
        # book_name = r.book
        r_dict_list.append({"reviewer": r.reviewer, "rating": r.rating, "content": r.content, "source": r.source,
                            "book": r.book})
    return jsonify(r_dict_list)


# get one Review
@app.route('/api/reviews/book=<string:book_name>')
def get8review_name(book_name):
    r_dict_list = []
    book_name = "%" + book_name + "%"

    review = models.Review.query.filter(models.Review.book.ilike(book_name)).all()
    # book = models.Book.query.filter_by(title=book_name).all()
    for r in review:
        r_dict_list.append({"reviewer": r.reviewer, "rating": r.rating, "content": r.content, "source": r.source,
                            "book": r.book})
    return jsonify(r_dict_list)


# get nok with arbitrary filters
@app.route('/api/reviews/params&<string:params>')
def get9rev(params):
    commands = params.split('&')
    r_dict_list = []
    r = models.Review.query
    # print type(p)

    for item in commands:
        col, fil = item.split('=')
        fil = "%" + fil + "%"
        if col in models.Review.__table__.columns.keys():
            r = r.filter(getattr(models.Review, col).ilike(fil))
    for b in r:
        r_dict_list.append(
            {"reviewer": b.reviewer, "rating": b.rating, "content": b.content, "source": b.source,
              "book": b.book})
    return jsonify(r_dict_list)


if __name__ == '__main__':
    # models.build_all()
    app.run(host='127.0.0.1', port=8080, debug=True)