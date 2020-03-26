import sqlite3 

class Vacancy:
    def __init__(self, _id, title, company, salary):
        self._id = _id 
        self.title = title
        self.company = company
        self.salary = salary

    def add_to_database(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_insert = "INSERT INTO vacancys VALUES(?,?,?,?)"
        cur.execute(query_insert, (self._id, self.title, self.company, self.salary))

        conn.commit()
        conn.close()
