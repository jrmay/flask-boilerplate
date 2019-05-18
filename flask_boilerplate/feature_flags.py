from flask_boilerplate.db import get_db


# TODO: accept a specific user identifier
class FeatureFlags:
    def get(self, key: str) -> bool:
        mapping = self.mapping()
        if key in mapping:
            return mapping[key]
        else:
            return False

    def set(self, key: str, value: bool):
        db = get_db()
        value_num = int(value)
        db.execute(
            'INSERT INTO feature_flags (key, active)'
            'VALUES '
            f"('{key}', {value_num});"
        )

    def mapping(self):
        db = get_db()
        flags = db.execute(
            'SELECT key, active'
            ' FROM feature_flags'
        ).fetchall()
        mapping = dict()
        for flag in flags:
            mapping[flag['key']] = (flag['active'] == 1)
        return mapping


def get_feature_flags() -> FeatureFlags:
    return FeatureFlags()
