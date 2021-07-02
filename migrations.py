import sqlite3
import os, json

config = json.load(open('src/config.json'))
database = config['database']

if os.path.exists(database):
    confirm = input('Database already exists. Do you want to delete it and create a new one? (y/[N]): ')
    if confirm == 'y':
        os.remove(database)
        print('[-] Database already exists. Deleting it.')
    else:
        print('[-] Exiting.')
        exit()

conn = sqlite3.connect(database)
print('[+] Database opened successfully.')

conn.execute('''CREATE TABLE users
         (UserId       INTEGER PRIMARY KEY,
         date          STRING  NOT NULL
         );''')

print('[+] Table users created successfully.')

conn.execute('''CREATE TABLE settings
         (ownerId       INTEGER PRIMARY KEY,
         language       TEXT DEFAULT "english",
         defaultAcId    INTEGER
         );''')
         
print('[+] Table settings created successfully.')

conn.execute('''CREATE TABLE accounts
         (accountId INTEGER PRIMARY KEY,
         ownerId    INTEGER NOT NULL,
         userName   TEXT    NOT NULL,
         email      TEXT    NOT NULL,
         password   TEXT    NOT NULL,
         cookie     TEXT    NOT NULL
         );''')
         
print('[+] Table accounts created successfully.')