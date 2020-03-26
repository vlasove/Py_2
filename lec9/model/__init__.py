import sqlite3 

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS autos (id INT, mark TEXT, amount INT)"
cur.execute(query_create)

conn.close()