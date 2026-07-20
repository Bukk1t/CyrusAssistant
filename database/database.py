import sqlite3
from pathlib import Path

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
        INSERT OR IGNORE INTO users
        (user_id, username, first_name)
        VALUES (?, ?, ?)
        """,
        (user_id, username, first_name),
    )

    connection.commit()
    connection.close()


def get_user(user_id):
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.execute(
        "SELECT * FROM users WHERE user_id = ?",
        (user_id,),
    )

    user = cursor.fetchone()

    connection.close()

    return user