import sqlite3

conn = sqlite3.connect('database_bot.db')
cursor = conn.cursor()



cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE NOT NULL,
    name TEXT NOT NULL
)
''')

conn.commit()
cursor.close()
conn.close()