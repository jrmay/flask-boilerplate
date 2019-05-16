import os

from flask import Flask, render_template

import datetime

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

    return app


def generate_routes(app):
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/about')
    def about():
        flags = get_feature_flags()
        context = {
            'time': datetime.datetime.now(),
            'show_time': flags.get('show_time_on_about_page'),
        }
        return render_template('about.html', context=context)
