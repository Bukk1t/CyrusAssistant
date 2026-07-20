import sqlite3
from pathlib import Path
from datetime import datetime


DB_PATH = Path("database/cyrus.db")
SCHEMA_PATH = Path("database/schema.sql")


def initialize_database():
    connection = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema:
        connection.executescript(schema.read())

    connection.commit()
    connection.close()


def add_user(user_id, username, first_name):
    connection = sqlite3.connect(DB_PATH)

    connection.execute(
        """
        INSERT INTO users (id, username, first_name)
        VALUES (?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
        username = excluded.username,
        first_name = excluded.first_name,
        last_seen = CURRENT_TIMESTAMP
        """,
        (user_id, username, first_name)
    )

    connection.commit()
    connection.close()


def add_message(user_id):
    connection = sqlite3.connect(DB_PATH)

    connection.execute(
        """
        UPDATE users
        SET messages = messages + 1,
        last_seen = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (user_id,)
    )

    connection.commit()
    connection.close()


def get_user_count():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.execute(
        "SELECT COUNT(*) FROM users"
    )

    count = cursor.fetchone()[0]

    connection.close()

    return count