ログイン/ログアウト/記事の登録/記事の一覧表示/記事の編集/記事の削除/コメントの追加/コメントの削除

- データベースを作成
  ```
  sqlite3 flaskr.db < schema.sql
  ```

- データベースの初期化
  ```
  $ python
  >>> from flaskr import init_db
  >>> init_db()
  ```
