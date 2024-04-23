import sqlite3
from config import FLAG

conn = sqlite3.connect('instance/ctfchallenge.db')
cursor = conn.cursor()

# Drop the old table
cursor.execute('DROP TABLE IF EXISTS cat_breeds')
cursor.execute('DROP TABLE IF EXISTS secrets')

cursor.execute('''
CREATE TABLE cat_breeds (
    id INTEGER PRIMARY KEY,
    breed TEXT
)
''')

cursor.execute('''
CREATE TABLE secrets (
    id INTEGER PRIMARY KEY,
    secret TEXT
)
''')

f = open('cat_breeds.txt', 'r')
for line in f.readlines():
    cursor.execute('''
    INSERT INTO cat_breeds (breed) VALUES (?)
    ''', (line.strip(), ))

cursor.execute('''
INSERT INTO secrets (secret) VALUES (?)
''', (FLAG,))

conn.commit()
conn.close()