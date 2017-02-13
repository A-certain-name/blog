# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, render_template, request, session, g, redirect, url_for,abort,flash
# import numpy as np
# from __future__ import with_statement
from contextlib import closing

DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'root'
PASSWORD = 'root'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# DB接続
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# DBの初期化
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# リクエスト前処理
@app.before_request
def before_request():
    g.db = connect_db()

# リクエスト後処理
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# ルーティング設定
# トップページ
@app.route('/')
def index():
    # 降順でテキストを取り出す
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    title = "blogサイト"
    message = "今の気分を一言"
    return render_template('index.html',
                           message=message, title=title, entries=entries)

# 記事投稿
@app.route('/post', methods=['POST'])
def post():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash(u'新しいつぶやきが追加されました')
    return redirect(url_for('index'))

#ログイン機能
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = u'ユーザ名が間違っています'
        elif request.form['password'] != app.config['PASSWORD']:
            error = u'パスワードが間違っています'
        else:
            session['logged_in'] = True
            flash(u'ログインしました')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash(u'ログアウトしました')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
