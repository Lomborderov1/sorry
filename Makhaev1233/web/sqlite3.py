import sqlite3 as sq 

conn = sq.connect('sqyuulite.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS menu(
    user_id INTEGER,
    name TEXT,
    age INTEGER NOT NULL DEFAULT 0
)""")

cur.execute("INSERT INTO menu VALUES (1, 'Yunus', 26)")

conn.close()