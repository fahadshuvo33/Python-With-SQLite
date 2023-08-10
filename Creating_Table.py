import sqlite3

conn = sqlite3.connect('Sample_1.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE Book_List (
        ID INTEGER PRIMARY KEY,
        Subject VARCHAR(50),
        Book_Price INTEGER,
        Publisher VARCHAR(100),
        Book_Pages INTEGER)
        ''')

conn.close()