import sqlite3, db_settings, create_DB_script, names, tasks, db_work

conn = sqlite3.connect(db_settings.patch)
cur = conn.cursor()


def add_tables():
    create_DB_script.create_controls()
    create_DB_script.create_users()
    for table_name in names.table_name:
        for subject in tasks.tasks:
            if subject['table_name'] == table_name:
                create_DB_script.create_tasks(table_name)
                for task in subject['tasks']:
                    db_work.add_field(table_name, task['num'], task['type'], task['text'])


def GetClearTables():
    pass


def ClearUsers():
    cur.execute('''DELETE FROM users;''')
    conn.commit()


def GetUsers():
    cur.execute('''SELECT * FROM users;''')
    users = cur.fetchall()
    return users


