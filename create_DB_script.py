import sqlite3

# Init DBs

conn = sqlite3.connect('Databases/MainDB.sqlite3')
cur = conn.cursor()

# Create Tables

# Users, who will do tasks
cur.execute('''CREATE TABLE IF NOT EXISTS users( 
    user_id TEXT PRIMARY KEY, 
    first_name TEXT, 
    last_name TEXT, 
    count_all INTEGER, 
    refuse_all INTEGER
);''')

# tasks
cur.execute('''CREATE TABLE IF NOT EXISTS mathematics(
    num_of_task INTEGER PRIMARY KEY,
    user_id TEXT,
    status TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS physics(
    num_of_task INTEGER PRIMARY KEY,
    user_id TEXT,
    status TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS progers(
    num_of_task INTEGER PRIMARY KEY,
    user_id TEXT,
    status TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS roles(
    role TEXT,
    user_id TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

conn.commit()

