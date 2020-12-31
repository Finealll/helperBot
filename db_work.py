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


# update table
def update_field(table: str, num: int, type: int, status: str = "not complete", user_id: str = "-", answer: str = "-"):
    cur.execute(f'''UPDATE {table} SET status = ?, user_id = ?, answer = ? WHERE num_of_task IS ? AND type_of_task IS ?;''', (status, user_id, answer, num, type))
    conn.commit()


def update_status(table: str, num: int, type: int, status: str = "not complete"):
    cur.execute(f'''UPDATE {table} SET status = ? WHERE num_of_task IS ? AND type_of_task IS ?;''', (status, num, type))
    conn.commit()


def update_answer(table: str, num: int, type: int, answer: str = "-"):
    cur.execute(f'''UPDATE {table} SET answer = ? WHERE num_of_task IS ? AND type_of_task IS ?;''', (answer, num, type))
    conn.commit()


# Checkers
def check_user_in_users(user_id):
    cur.execute('''SELECT * FROM users WHERE user_id=?;''', (user_id,))
    return False if cur.fetchone() == None else True


def check_roles_in_roles(user_id: str, role: str):
    cur.execute('''SELECT * FROM roles WHERE user_id=? AND role=?;''', (user_id, role))
    return False if cur.fetchone() == None else True


def check_free_numbers(table: str):
    cur.execute(f'''SELECT num_of_task FROM {table} WHERE status IS ?;''', ('not complete',))
    return False if cur.fetchone() == None else True


def check_free_numbers_by_status_and_type(table: str, type: int):
    cur.execute(f'''SELECT num_of_task FROM {table} WHERE status IS ? AND type_of_task IS ?;''', ('not complete', type))
    return False if cur.fetchone() == None else True


def check_is_added_task(table: str, num:int, type: int):
    cur.execute(f'''SELECT status FROM {table} WHERE num_of_task IS ? AND type_of_task IS ?;''', (num, type))
    fetch = cur.fetchone()
    if fetch is None:
        return False
    return True if fetch[0] != 'not complete' else False


def check_is_added_task_by_user(table: str, num:int, type: int, user_id: str):
    cur.execute(f'''SELECT status FROM {table} WHERE num_of_task IS ? AND type_of_task IS ? AND user_id IS ?;''', (num, type, user_id))
    fetch = cur.fetchone()
    if fetch is None:
        return False
    return True if fetch[0] != 'not complete' else False


def check_is_exist_status(table: str, status: str):
    cur.execute(f'''SELECT status FROM {table} WHERE status IS ?;''', (status,))
    return False if cur.fetchone() is None else True


# Getters

def get_free_numbers(table: str, type: int):
    cur.execute(f'''SELECT num_of_task FROM {table} WHERE status IS ? AND type_of_task IS ?;''', ('not complete', type))
    buff = cur.fetchall()
    free_numbers = []
    for item in buff:
        free_numbers.append(item[0])
    return free_numbers


def get_roles_in_roles(user_id: str):
    cur.execute('''SELECT role FROM roles WHERE user_id=?;''', (user_id,))
    buff = cur.fetchall()
    roles = []
    for item in buff:
        roles.append(item[0])
    return roles

def get_now_tasks(table: str, user_id: str):
    cur.execute(f'''SELECT num_of_task, type_of_task FROM {table} WHERE user_id IS ? AND status IS ?;''', (user_id, 'in process',))
    return cur.fetchall()


def get_status(table: str, num: int, type: int):
    cur.execute(f'''SELECT status FROM {table} WHERE num_of_task IS ? AND type_of_task IS ?;''', (num, type,))
    status = cur.fetchone()[0]
    return status


def get_answer(table: str, num: int, type: int):
    cur.execute(f'''SELECT answer FROM {table} WHERE num_of_task IS ? AND type_of_task IS ?;''', (num, type,))
    status = cur.fetchone()[0]
    return status


def get_info_by_status(table: str, status: str):
    cur.execute(f'''SELECT num_of_task, type_of_task FROM {table} WHERE status IS ?;''', (status,))
    info = cur.fetchall()
    return info
