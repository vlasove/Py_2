import sqlite3 

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS vacancys (id INTEGER PRIMARY KEY, title TEXT, company TEXT, salary INT)"
cur.execute(query_create)

conn.close()