import sqlite3

DATABASE = 'database.db'

def create_books_table():
    conn = sqlite3.connect(DATABASE)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price INTEGER NOT NULL,
            arrival_day TEXT NOT NULL
        )
    ''')
    conn.close()