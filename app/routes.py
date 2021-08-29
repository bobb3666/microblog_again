from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland maates!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movies can suck my cunt!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)