import os
import tempfile

import pytest

from flask_boilerplate import create_app
from flask_boilerplate.db import init_db, get_db


def test_data_sql():
    file_dir = os.path.dirname(__file__)
    path = os.path.join(file_dir, 'data.sql')
    with open(path, 'rb') as file:
        test_data = file.read().decode('utf8')
    return test_data


@pytest.fixture
def app():
    db_fd, database = tempfile.mkstemp()
    app = create_app({
        'DATABASE': database,
        'TESTING': True,
    })

    with app.app_context():
        init_db()
        get_db().executescript(test_data_sql())

    yield app

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


def in_app_context(f):
    def decorator(app, *args):
        with app.app_context():
            f(*args)

    return decorator
