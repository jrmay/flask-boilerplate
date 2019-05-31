from flask import request, redirect, url_for, flash, render_template, \
    session, g

from flask_boilerplate.auth import User
from flask_boilerplate.auth.util import do_login


def generate_routes(blueprint):
    @blueprint.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            result = do_login(username, password)

            if result.success:
                return redirect(url_for('index'))
            else:
                flash(result.error)

        return render_template('auth/login.html', user=g.user)

    @blueprint.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('index'))

    @blueprint.route('/register', methods=('GET', 'POST'))
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

        return render_template('auth/register.html', user=g.user)
