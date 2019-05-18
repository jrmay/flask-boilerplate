from flask_boilerplate import get_feature_flags
from tests.conftest import in_app_context


@in_app_context
def test_nonexistent_flag_returns_false():
    flags = get_feature_flags()
    assert flags.get('nonexistent') is False


@in_app_context
def test_flag_can_be_false():
    flags = get_feature_flags()
    assert flags.get('always-false') is False


@in_app_context
def test_flag_can_be_true():
    flags = get_feature_flags()
    assert flags.get('always-true') is True


@in_app_context
def test_can_set_flag():
    flags = get_feature_flags()
    assert flags.get('new-flag') is False
    flags.set('new-flag', True)
    assert flags.get('new-flag') is True
