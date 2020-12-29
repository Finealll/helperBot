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

#admin_functions
def GetClearEltech(num1: int, num2: int, num3: int):
    cur.execute('''DELETE FROM eltech;''')
    conn.commit()
    for i in range(1, num1+1):
        cur.execute('''INSERT INTO eltech VALUES(?,?,?,?,?);''', (i, 1, '-', 'not complete', '-'))
    for i in range(1, num2+1):
        cur.execute('''INSERT INTO eltech VALUES(?,?,?,?,?);''', (i, 2, '-', 'not complete', '-'))
    for i in range(1, num3+1):
        cur.execute('''INSERT INTO eltech VALUES(?,?,?,?,?);''', (i, 3, '-', 'not complete', '-'))
    conn.commit()

def GetClearMath(num1: int, num2: int, num3: int):
    cur.execute('''DELETE FROM maths;''')
    conn.commit()
    for i in range(1, num1+1):
        cur.execute('''INSERT INTO maths VALUES(?,?,?,?,?);''', (i, 1, '-', 'not complete', '-'))
    for i in range(1, num2+1):
        cur.execute('''INSERT INTO maths VALUES(?,?,?,?,?);''', (i, 2, '-', 'not complete', '-'))
    for i in range(1, num3+1):
        cur.execute('''INSERT INTO maths VALUES(?,?,?,?,?);''', (i, 3, '-', 'not complete', '-'))
    conn.commit()

def GetClearProgers(num1: int, num2: int, num3: int):
    cur.execute('''DELETE FROM progers;''')
    conn.commit()
    for i in range(1, num1+1):
        cur.execute('''INSERT INTO progers VALUES(?,?,?,?,?);''', (i, 1, '-', 'not complete', '-'))
    for i in range(1, num2+1):
        cur.execute('''INSERT INTO progers VALUES(?,?,?,?,?);''', (i, 2, '-', 'not complete', '-'))
    for i in range(1, num3+1):
        cur.execute('''INSERT INTO progers VALUES(?,?,?,?,?);''', (i, 3, '-', 'not complete', '-'))
    conn.commit()

def GetClearPhysics(num1: int, num2: int, num3: int):
    cur.execute('''DELETE FROM physics;''')
    conn.commit()
    for i in range(1, num1+1):
        cur.execute('''INSERT INTO physics VALUES(?,?,?,?,?);''', (i, 1, '-', 'not complete', '-'))
    for i in range(1, num2+1):
        cur.execute('''INSERT INTO physics VALUES(?,?,?,?,?);''', (i, 2, '-', 'not complete', '-'))
    for i in range(1, num3+1):
        cur.execute('''INSERT INTO physics VALUES(?,?,?,?,?);''', (i, 3, '-', 'not complete', '-'))
    conn.commit()

def GetClearTables():
    GetClearEltech(20, 20, 3)
    GetClearProgers(30, 10, 0)
    GetClearPhysics(0, 0, 0)
    GetClearMath(0, 0, 0)




