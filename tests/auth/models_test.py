import sqlite3

from flask_boilerplate.auth import User
from tests.conftest import in_app_context


@in_app_context
def test_user_get_by_username_returns_existing_user():
    user = User.get_by_username('jordanmay')
    assert user.__class__ is sqlite3.Row
    assert user['username'] == 'jordanmay'


@in_app_context
def test_user_create():
    username = 'newname'
    password = 'password'
    initial_count = User.count()
    User.create(username, password)
    assert User.count() == initial_count + 1
