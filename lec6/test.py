import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()


query = 'CREATE TABLE IF NOT EXISTS films (id INT, title TEXT, duration INT)'
cur.execute(query)

insert_query = "INSERT INTO films VALUES(?,?,?)"
cur.execute(insert_query, (2, 'HP', 178))
conn.commit()

select_query = "SELECT * FROM films"
for row in cur.execute(select_query):
    print(row)

update_query='UPDATE films SET duration=? WHERE title=?'
cur.execute(update_query,(920, 'HP'))
conn.commit()


delete_query = 'DELETE FROM films'
cur.execute(delete_query)
conn.commit()

select_query = "SELECT * FROM films"
for row in cur.execute(select_query):
    print(row)


conn.close()