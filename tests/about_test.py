from flask_boilerplate import get_feature_flags


def _test_about_includes_current_time_when_flag_active(client, app):
    with app.app_context():
        flags = get_feature_flags()
    response = client.get('/about')
    assert b'Current time:' in response.data


def test_about_excludes_current_time_when_flag_inactive(client):
    response = client.get('/about')
    assert b'Current time:' not in response.data
