import sqlite3
from config import DATABASE_PATH

def initialize_catalog():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metadata (
        column_name TEXT,
        dtype TEXT,
        unique_values INTEGER,
        null_values INTEGER
    )
    """)

    conn.commit()
    conn.close()

def store_metadata(metadata):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    for col, values in metadata.items():

        cursor.execute("""
        INSERT INTO metadata VALUES (?, ?, ?, ?)
        """, (
            col,
            values['dtype'],
            values['unique_values'],
            values['null_values']
        ))

    conn.commit()
    conn.close()
