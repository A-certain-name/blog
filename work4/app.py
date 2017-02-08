# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

# Routing
@app.route('/')
def index():
    title = "blogサイト"
    message = "今の気分を一言"
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "投稿しました"
    if request.method == 'POST':
        tweet = request.form['tweet']
        return render_template('index.html',
                               tweet=tweet, title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
