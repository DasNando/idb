from flask import render_template
import logging
from app import db

local_app = db.app

@local_app.route('/')
@local_app.route('/home')
def home():
    return render_template('home.html')


@local_app.route('/about')
def about():
    return render_template('about.html')


@local_app.route('/authors')
def authors():
    return render_template('authors.html')


@local_app.route('/books')
def books():
    return render_template('books.html')


@local_app.route('/publishers')
def publishers():
    return render_template('publishers.html')

@local_app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@local_app.route('/search')
def search():
    return render_template('search.html')


@local_app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    local_app.run(debug=True)

