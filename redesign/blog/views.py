"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from blog import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Flaskを使用したblogサイト',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='連絡先',
        year=datetime.now().year,
        message='問い合わせはこちら.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='概要',
        year=datetime.now().year,
        message='ここはブログサイトです。1日1コミット'
    )
