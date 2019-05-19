from flask import Blueprint, request, redirect, url_for, flash, \
    render_template, session, g
from werkzeug.security import check_password_hash

from flask_boilerplate.auth.models import User

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.get_by_username(username) is not None:
            error = f'User {username} is already registered.'

        if error is None:
            User.create(username, password)
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None

        user = User.get_by_username(username)
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@auth_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@auth_blueprint.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.get_by_id(user_id)
