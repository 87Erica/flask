from flask import Flask

app = Flask(__name__)

@app.route('/about')
def about():
    return 'This is the about page.'
@app.route('/user/<username>')
#@app.route('/')
def show_user_profile(username):
    return f'User{username}'