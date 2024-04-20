import sqlite3

con = sqlite3.connect("MovieRentalDB.db")
cursor = con.cursor()

cursor.close()
con.close()