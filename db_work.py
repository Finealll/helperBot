import sqlite3, db_settings

conn = sqlite3.connect(db_settings.patch)
cur = conn.cursor()


# add users
def add_user(user_id: str, first_name: str, last_name: str):
    if not check_user_in_users(user_id):
        cur.execute('''INSERT INTO users VALUES(?,?,?,?,?);''', (user_id, first_name, last_name, 0, 0))
        conn.commit()
        return 1
    else:
        return 0

# add roles
def add_role(user_id: str, role: str):
    if not check_roles_in_roles(user_id, role):
        cur.execute('''INSERT INTO roles VALUES(?,?);''', (role, user_id))
        conn.commit()
        return 1
    else:
        return 0

# delete role
def del_role(user_id: str, role: str):
    if check_roles_in_roles(user_id, role):
        cur.execute('''DELETE FROM roles WHERE user_id=? AND role=?;''', (user_id, role))
        conn.commit()
        return 1
    else:
        return 0

# Checkers
def check_user_in_users(user_id):
    cur.execute('''SELECT * FROM users WHERE user_id=?;''', (user_id,))
    return False if cur.fetchone() == None else True


def check_roles_in_roles(user_id: str, role: str):
    cur.execute('''SELECT * FROM roles WHERE user_id=? AND role=?;''', (user_id, role))
    return False if cur.fetchone() == None else True

# Getters

def get_free_numbers(table: str):
    cur.execute(f'''SELECT num_of_task FROM {table} WHERE status IS ?;''', ('not complete',))
    return cur.fetchall()

def get_roles_in_roles(user_id: str):
    cur.execute('''SELECT role FROM roles WHERE user_id=?;''', (user_id,))
    return cur.fetchall()

