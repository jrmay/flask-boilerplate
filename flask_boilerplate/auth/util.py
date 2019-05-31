from flask import session
from werkzeug.security import check_password_hash

from flask_boilerplate.auth import User


class LoginResult:
    error = None

    def __init__(self, success):
        self.success = success


def do_login(username, password) -> LoginResult:
    error = None

    user = User.get_by_username(username)
    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
        return LoginResult(True)
    else:
        result = LoginResult(False)
        result.error = error
        return result
