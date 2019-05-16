DROP TABLE IF EXISTS feature_flags;

CREATE TABLE feature_flags (
    key TEXT UNIQUE NOT NULL,
    active INTEGER NOT NULL DEFAULT 0
);
