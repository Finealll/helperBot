import sqlite3, db_settings

# Init DBs

conn = sqlite3.connect(db_settings.patch)
cur = conn.cursor()

# Create Tables

# Users, who will do tasks
def create_users():
    cur.execute('''CREATE TABLE IF NOT EXISTS users( 
        user_id TEXT PRIMARY KEY, 
        first_name TEXT, 
        last_name TEXT, 
        count_all INTEGER, 
        refuse_all INTEGER
    );''')
    conn.commit()

# tasks
def create_tasks(table_name: str):
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(
        num_of_task INTEGER,
        type_of_task INTEGER,
        user_id TEXT,
        status TEXT,
        answer TEXT,
        datetime TEXT,
        score INTEGER,
        count_of_scores INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    );''')
    conn.commit()


def create_controls():
    cur.execute('''CREATE TABLE IF NOT EXISTS controlers(
        subject TEXT,
        user_id TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    );''')
    conn.commit()

conn.commit()

