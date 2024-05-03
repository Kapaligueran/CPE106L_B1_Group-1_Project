import sqlite3


# class DatabaseManagement to perform CRUD operations on database
class DatabaseManagement:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def display(self, query):
        return self.cur.execute(query).fetchall()
