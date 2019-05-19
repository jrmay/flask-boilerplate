import os

from flask import Flask

from flask_boilerplate.auth import auth_blueprint
from flask_boilerplate.feature_flags import get_feature_flags


def create_app(config: dict = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'development.sqlite'),
    )

    if config is None:
        # load the instance config when not in test
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the config
        app.config.from_mapping(config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    generate_routes(app)

    app.register_blueprint(auth_blueprint)

    return app


def generate_routes(app):
    @app.route('/')
    def index():
        return 'Hello World!'
