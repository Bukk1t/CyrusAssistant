import sqlite3
from pathlib import Path

DB_PATH = Path("database/cyrus.db")
SCHEMA_PATH = Path("database/schema.sql")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as schema:
            connection.executescript(schema.read())


def add_user(user_id, username, first_name):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO users (id, username, first_name)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                username = excluded.username,
                first_name = excluded.first_name,
                last_seen = CURRENT_TIMESTAMP
            """,
            (user_id, username, first_name),
        )


def add_message(user_id):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE users
            SET
                messages = messages + 1,
                last_seen = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (user_id,),
        )


def get_user_count():
    with get_connection() as connection:
        cursor = connection.execute(
            "SELECT COUNT(*) FROM users"
        )
        return cursor.fetchone()[0]

def get_user(user_id):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id, username, first_name, joined_at, messages, last_seen
            FROM users
            WHERE id = ?
            """,
            (user_id,),
        )

        return cursor.fetchone()