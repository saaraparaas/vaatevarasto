CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INEEGER PRIMARY KEY,
    title TEXT,
    size INTEGER,
    color TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);

