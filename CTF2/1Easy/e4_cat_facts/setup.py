# Note that the name and schema of the tables might be different on the server!
import sqlite3
from config import FLAG

conn = sqlite3.connect('instance/ctfchallenge.db')
cursor = conn.cursor()

# Drop the old table
cursor.execute('DROP TABLE IF EXISTS facts')
cursor.execute('DROP TABLE IF EXISTS secrets')

cursor.execute('''
CREATE TABLE facts (
    id INTEGER PRIMARY KEY,
    fact TEXT
)
''')

cursor.execute('''
CREATE TABLE secrets (
    id INTEGER PRIMARY KEY,
    secret TEXT
)
''')

f = open('cat_facts.txt', 'r')
for line in f.readlines():
    cursor.execute('''
    INSERT INTO facts (fact) VALUES (?)
    ''', (line.strip(), ))

cursor.execute('''
INSERT INTO secrets (secret) VALUES (?)
''', (FLAG,))

conn.commit()
conn.close()