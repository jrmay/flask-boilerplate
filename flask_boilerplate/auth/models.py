from werkzeug.security import generate_password_hash

from flask_boilerplate.db import get_db


# Currently just a bag of methods
class User:
    @staticmethod
    def get_by_username(username):
        db = get_db()
        return db.execute(
            'SELECT id, username, password '
            'FROM users '
            'WHERE username = ?',
            (username,)
        ).fetchone()

    @staticmethod
    def create(username, password):
        db = get_db()
        db.execute(
            'INSERT INTO users (username, password) '
            'VALUES (?, ?)',
            (username, generate_password_hash(password))
        )
        db.commit()

    @staticmethod
    def count():
        db = get_db()
        return len(db.execute(
            'SELECT id FROM users'
        ).fetchall())

    @staticmethod
    def get_by_id(user_id):
        return get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()
