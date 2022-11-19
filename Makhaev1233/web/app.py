import sqlite3 
conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()
cursor.execute("""SELET * FROM students""")
print(cursor.fetchall())
conn.commit()
conn.close()