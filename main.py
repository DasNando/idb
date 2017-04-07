from flask import render_template, jsonify
from flask_restful import Api, Resource
import logging
import requests
from app import db, models
import requests_toolbelt.adapters.appengine
requests_toolbelt.adapters.appengine.monkeypatch()

db1 = db.db
app = db.app


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
    # books = db1.session.query(models.Book).filter_by(genre="Fiction").all()
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


api = Api(app)
book = {"book_test": "book_name"}


# get book with arbitrary filters
class F_Book(Resource):
    def get(self, lim=0):
        if not lim:
            lim = 10
        b_dict_list = []
        p = db1.session.query(models.Book).limit(lim)
        print type(p)
        for b in p:
            # b_dict_list.append(
            #     {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic})
            b_dict_list.append(
                {"title": "dummy_title", "genre": "dummy_genre", "year": "dummy_year", "isbn": "dummy_isbn", "prices": "dummy_prices", "pic": "dummy_pic"})
        return jsonify(b_dict_list)


api.add_resource(F_Book, '/api/books/', '/api/books/<int:lim>')

# get one book
class Q_Book(Resource):
    def get(self, book_name):
        b_dict_list = []

        book = db1.session.query(models.Book).filter_by(title=book_name).all()
        for b in book:
            b_dict_list.append(
                {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic})
        # print book.title
        return jsonify(b_dict_list)


api.add_resource(Q_Book, '/api/books/title=<string:book_name>')


# get book with arbitrary filters
class QA_Book(Resource):
    def get(self, params):
        commands = params.split('&')
        b_dict_list = []
        p = db1.session.query(models.Book)
        print type(p)

        for item in commands:
            col, fil = item.split('=')
            if col in models.Book.__table__.columns.keys():
                p = p.filter(getattr(models.Book, col).like(fil))
        for b in p:
            b_dict_list.append(
                {"title": b.title, "genre": b.genre, "year": b.year, "isbn": b.isbn, "prices": b.prices, "pic": b.pic})
        return jsonify(b_dict_list)


api.add_resource(QA_Book, '/api/books/params&<string:params>')


# get one Author
class Q_Author(Resource):
    def get(self, author_name):
        a_dict_list = []
        author_name = " " + author_name + " "

        author = db1.session.query(models.Author).filter_by(name=author_name).all()
        for b in author:
            a_dict_list.append({"name": b.name, "birth_date": b.birth_date, "death_date": b.death_date, "pic": b.pic,
                                "about": b.about, "num_works": b.num_works})
        return jsonify(a_dict_list)


api.add_resource(Q_Author, '/api/authors/name=<string:author_name>')


# get book with arbitrary filters
class QA_Author(Resource):
    def get(self, params):
        commands = params.split('&')
        a_dict_list = []
        p = db1.session.query(models.Author)
        print type(p)

        for item in commands:
            col, fil = item.split('=')
            if col in models.Author.__table__.columns.keys():
                p = p.filter(getattr(models.Author, col).like(fil))
        for b in p:
            a_dict_list.append({"name": b.name, "birth_date": b.birth_date, "death_date": b.death_date, "pic": b.pic,
                                "about": b.about, "num_works": b.num_works})
        return jsonify(a_dict_list)
api.add_resource(QA_Author, '/api/authors/params&<string:params>')


# get one Publisher
class Q_Publisher(Resource):
    def get(self, publisher_name):
        p_dict_list = []

        publisher = db1.session.query(models.Publisher).filter_by(name=publisher_name).all()
        for b in publisher:
            p_dict_list.append(
                {"name": b.name, "founding_date": b.founding_date, "headquarters": b.headquarters, "country": b.country,
                 "founders": b.founders})
        return jsonify(p_dict_list)


# get book with arbitrary filters
class QA_Publisher(Resource):
    def get(self, params):
        commands = params.split('&')
        p_dict_list = []
        p = db1.session.query(models.Publisher)
        print type(p)

        for item in commands:
            col, fil = item.split('=')
            if col in models.Publisher.__table__.columns.keys():
                p = p.filter(getattr(models.Publisher, col).like(fil))
        for b in p:
            p_dict_list.append(
                {"name": b.name, "founding_date": b.founding_date, "headquarters": b.headquarters, "country": b.country,
                 "founders": b.founders})
        return jsonify(p_dict_list)
api.add_resource(QA_Publisher, '/api/publishers/params&<string:params>')


api.add_resource(Q_Publisher, '/api/publishers/name=<string:publisher_name>')


if __name__ == '__main__':
    app.run(debug=True)
