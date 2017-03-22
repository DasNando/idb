from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    return 'hello'


@app.route('/profile/<username>')
def profile(username):
    return render_template('home.html', user=username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post id is: %d' % post_id

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    app.run()

