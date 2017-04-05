from flask import render_template
import logging
from app import db


@db.app.route('/')
@db.app.route('/home')
def home():
    return render_template('home.html')


@db.app.route('/about')
def about():
    return render_template('about.html')


@db.app.route('/authors')
def authors():
    return render_template('authors.html')


@db.app.route('/books')
def books():
    return render_template('books.html')


@db.app.route('/publishers')
def publishers():
    return render_template('publishers.html')

@db.app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@db.app.route('/search')
def search():
    return render_template('search.html')


@db.app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    db.app.run(debug=True)

