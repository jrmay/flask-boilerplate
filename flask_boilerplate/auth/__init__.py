from flask import Blueprint, session, g

from flask_boilerplate.auth.models import User
from flask_boilerplate.auth.routes import generate_routes

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.get_by_id(user_id)


generate_routes(auth_blueprint)
