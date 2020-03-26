import sqlite3 

class Vacancy:
    def __init__(self, title, company, salary): 
        self.title = title
        self.company = company
        self.salary = salary

    def add_to_database(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_insert = "INSERT INTO vacancys VALUES(NULL,?,?,?)"
        cur.execute(query_insert, (self.title, self.company, self.salary))

        conn.commit()
        conn.close()
