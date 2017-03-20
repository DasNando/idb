from flask import Flask, render_template

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()
