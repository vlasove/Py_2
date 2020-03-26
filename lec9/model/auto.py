import sqlite3 

class Auto:
    def __init__(self, _id, mark, amount):
        self._id = _id 
        self.mark = mark
        self.amount = amount 

    def add_to_database(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_insert = "INSERT INTO autos VALUES(?,?,?)"
        cur.execute(query_insert, (self._id, self.mark, self.amount))

        conn.commit()
        conn.close()
