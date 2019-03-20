import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''DROP TABLE jobstats''')
c = conn.cursor()