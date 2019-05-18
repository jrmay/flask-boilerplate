from flask_boilerplate import create_app


def test_not_in_testing():
    app = create_app()
    assert app.testing is False
