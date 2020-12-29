import sqlite3

conn = sqlite3.connect('Databases/MainDB.sqlite3')
cur = conn.cursor()

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


def ClearUsers():
    cur.execute('''DELETE FROM users;''')
    conn.commit()


def GetUsers():
    cur.execute('''SELECT * FROM users;''')
    users = cur.fetchall()
    return users



