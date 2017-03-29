from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
# postgresql://scott:tiger@localhost/mydatabase
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:swereaders@35.184.110.238:5432/postgres'
db = SQLAlchemy(app)


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


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    app.run(debug=True)

