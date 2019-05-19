INSERT INTO feature_flags (key, active)
VALUES
       ('always-true', 1),
       ('always-false', 0),
       ('blog-active', 1);

INSERT INTO users (username, password)
VALUES
    ('jordanmay', 'pbkdf2:sha256:150000$b7Qfnpmn$fcb9c6435fc2865d847abde7a1a60c008129264bcd2ca1259ca43c583fe9636f');
