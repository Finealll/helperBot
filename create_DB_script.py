import sqlite3, db_settings

# Init DBs


# Create Tables

# Users, who will do tasks
def create_users():
    conn = sqlite3.connect(db_settings.patch)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users( 
        user_id TEXT PRIMARY KEY, 
        first_name TEXT, 
        last_name TEXT, 
        count_all INTEGER, 
        refuse_all INTEGER,
        control_all INTEGER
    );''')
    conn.commit()

# tasks
def create_tasks(table_name: str):
    conn = sqlite3.connect(db_settings.patch)
    cur = conn.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(
        num_of_task INTEGER,
        type_of_task INTEGER,
        text TEXT,
        user_id TEXT,
        status TEXT,
        answer TEXT,
        datetime TEXT,
        score INTEGER,
        controler TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    );''')
    conn.commit()


def create_controls():
    conn = sqlite3.connect(db_settings.patch)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS controlers(
        subject TEXT,
        user_id TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    );''')
    conn.commit()


