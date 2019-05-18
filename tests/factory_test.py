from flask_boilerplate import create_app


def test_not_passing_test_config():
    app = create_app()
    assert app.testing is False
