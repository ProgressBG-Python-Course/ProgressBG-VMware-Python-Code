import sqlite3
conn = sqlite3.connect('example.db')


def createtable():
    c = conn.cursor()
    c.execute('''CREATE TABLE jobstats
                (date text, time text, totaljobs int, newjobs int)''')
    c = conn.cursor()

createtable()
