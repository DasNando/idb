from flask import render_template, request
from flask_restful import Api, Resource
import logging
from app import db, models

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
    return render_template('books.html')


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
    import requests

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Travis-API-Version': '3',
        'Authorization': 'token wpV_1One91F2XNwmI6ukIg',
    }

    data = '{"request": {"branch": "master"}}'

    requests.post('https://api.travis-ci.org/repo/DasNando%2Fidb/requests', headers=headers, data=data)

    return render_template('search.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


#################### API SECTION


api = Api(app)
book = {"book_test": "book_name"}


class Q_Books(Resource):
    def get(self, book_id):
        return book

    def put(self, book_id):
        book = {book_id: book_id}
        return book

api.add_resource(Q_Books, '/<string:book_id>')


if __name__ == '__main__':
    app.run(debug=True)
