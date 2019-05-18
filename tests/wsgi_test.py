from flask import Flask

from flask_boilerplate import wsgi


def test_wsgi_app_is_flask_app():
    app = wsgi.app
    assert app.__class__ is Flask
