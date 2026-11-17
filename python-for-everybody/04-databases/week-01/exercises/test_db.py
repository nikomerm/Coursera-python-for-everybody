import sqlite3

conn = sqlite3.connect("test.sqlite")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Users (name TEXT, age INTEGER)")
cur.execute("INSERT INTO Users (name, age) VALUES ('Nikos', 30)")

conn.commit()
conn.close()
print("Done")