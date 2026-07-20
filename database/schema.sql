CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    language TEXT DEFAULT 'en',
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);