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