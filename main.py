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
    # books = db1.query(models.Book).filter_by(genre="Fiction").all()
    # b_dict_list = []
    # i = 0
    # for b in books:
    #     print "loop"
    #     b_dict_list.append({"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic})
    #     print b_dict_list[i]
    #     print len(b_dict_list)
    #     i += 1
    #     if i >= 30:
    #         break
    # books = b_dict_list
    # print type(books)
    # print books
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

    #return "server response: " + res.text + "dict_from_server: " + str(dict_from_server)

    #return render_template('search.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


#################### API SECTION

book = {"book_test": "book_name"}


# get book with arbitrary filters
@app.route('/api/book')
@app.route('/api/book/<int:lim>')
def get_book1(lim=0):
    if not lim:
        lim = 10
    result = []
    for item in models.Book.query.all():
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

# get one book
def get_book2(self, book_name):
    b_dict_list = []

    book = db1.query(models.Book).filter_by(title=book_name).all()
    for b in book:
        b_dict_list.append(
            {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic})
    # print book.title
    return jsonify(b_dict_list)




# get book with arbitrary filters
def get_book3(self, params):
    commands = params.split('&')
    b_dict_list = []
    p = db1.query(models.Book)
    # print type(p)

    for item in commands:
        col, fil = item.split('=')
        if col in models.Book.__table__.columns.keys():
            p = p.filter(getattr(models.Book, col).like(fil))
    for b in p:
        b_dict_list.append(
            {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic})
    return jsonify(b_dict_list)



# get one Author
def get1(self, author_name):
    a_dict_list = []
    author_name = " " + author_name + " "

    author = db1.query(models.Author).filter_by(name=author_name).all()
    for b in author:
        a_dict_list.append({"name": b.name, "birth_date": b.birth_date, "death_date": b.death_date, "pic": b.pic,
                            "about": b.about, "num_works": b.num_works})
    return jsonify(a_dict_list)


# get book with arbitrary filters
def get2(self, params):
    commands = params.split('&')
    a_dict_list = []
    p = db1.query(models.Author)
    # print type(p)

    for item in commands:
        col, fil = item.split('=')
        if col in models.Author.__table__.columns.keys():
            p = p.filter(getattr(models.Author, col).like(fil))
    for b in p:
        a_dict_list.append({"name": b.name, "birth_date": b.birth_date, "death_date": b.death_date, "pic": b.pic,
                            "about": b.about, "num_works": b.num_works})
    return jsonify(a_dict_list)


# get one Publisher
def get3(self, publisher_name):
    p_dict_list = []

    publisher = db1.query(models.Publisher).filter_by(name=publisher_name).all()
    for b in publisher:
        p_dict_list.append(
            {"name": b.name, "founding_date": b.founding_date, "headquarters": b.headquarters, "country": b.country,
             "founders": b.founders})
    return jsonify(p_dict_list)


# get book with arbitrary filters
def get1(self, params):
    commands = params.split('&')
    p_dict_list = []
    p = db1.query(models.Publisher)
    # print type(p)

    for item in commands:
        col, fil = item.split('=')
        if col in models.Publisher.__table__.columns.keys():
            p = p.filter(getattr(models.Publisher, col).like(fil))
    for b in p:
        p_dict_list.append(
            {"name": b.name, "founding_date": b.founding_date, "headquarters": b.headquarters, "country": b.country,
             "founders": b.founders})
    return jsonify(p_dict_list)


if __name__ == '__main__':
    setup_db.init_db()
    app.run(host='127.0.0.1', port=8080, debug=True)
