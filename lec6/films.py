import sqlite3


class Film:
    def __init__(self, _id, title, duration):
        self._id = _id 
        self.title = title 
        self.duration = duration

    def save(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = 'INSERT INTO films VALUES(?, ?, ?)'
        cur.execute(query, (self._id, self.title, self.duration))

        conn.commit() 
        conn.close() 


    def update_title(self, new_title):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = 'UPDATE films SET title=? WHERE id=?'
        cur.execute(query, (new_title, self._id ))

        conn.commit()
        conn.close()

    def update_duration(self, new_duration):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = 'UPDATE films SET duration=? WHERE id=?'
        cur.execute(query, (new_duration, self._id ))

        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = 'DELETE FROM films WHERE id = ?'
        cur.execute(query, (self._id,)) 

        conn.commit()
        conn.close()
    
f = Film(1, 'asd', 200)
f.save()
f.delete()


query_save = "INSERT INTO films VALUES(?,?,?)"
cur.execute(query_save, (self._id, self.title, self.duration))

