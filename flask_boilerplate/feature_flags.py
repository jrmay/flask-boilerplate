from flask_boilerplate.db import get_db


# TODO: accept a specific user identifier
class FeatureFlags:
    def __init__(self, flags):
        self.mapping = {}
        for flag in flags:
            self.mapping[flag['key']] = (flag['active'] == 1)

    def get(self, key):
        if key in self.mapping:
            return self.mapping[key]
        else:
            return False


def get_feature_flags():
    db = get_db()
    result = db.execute(
        'SELECT key, active'
        ' FROM feature_flags'
    ).fetchall()
    return FeatureFlags(result)
