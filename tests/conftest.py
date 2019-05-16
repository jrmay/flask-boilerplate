import os
import tempfile

import pytest

from flask_boilerplate import create_app


@pytest.fixture
def client():
    db_fd, database = tempfile.mkstemp()
    app = create_app({
        'DATABASE': database,
        'TESTING': True,
    })
    client = app.test_client()

    with app.app_context():
        pass  # TODO: init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
