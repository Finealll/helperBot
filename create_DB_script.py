import sqlite3, db_settings

# Init DBs

conn = sqlite3.connect(db_settings.patch)
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
cur.execute('''CREATE TABLE IF NOT EXISTS maths(
    num_of_task INTEGER,
    type_of_task INTEGER,
    user_id TEXT,
    status TEXT,
    answer BLOB,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS physics(
    num_of_task INTEGER,
    type_of_task INTEGER,
    user_id TEXT,
    status TEXT,
    answer BLOB,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS progers(
    num_of_task INTEGER,
    type_of_task INTEGER,
    user_id TEXT,
    status TEXT,
    answer BLOB,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS eltech(
    num_of_task INTEGER,
    type_of_task INTEGER,
    user_id TEXT,
    status TEXT,
    answer BLOB,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS roles(
    role TEXT,
    user_id TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);''')

conn.commit()

