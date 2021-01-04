import sqlite3, db_settings, datetime

conn = sqlite3.connect(db_settings.patch)
cur = conn.cursor()


# add users
def add_user(user_id: str, first_name: str, last_name: str):
    if not check_user_in_users(user_id):
        cur.execute('''INSERT INTO users VALUES(?,?,?,?,?,?);''', (user_id, first_name, last_name, 0, 0, 0))
        conn.commit()
        return 1
    else:
        return 0

# add controlers
def add_controlers(user_id: str, subject: str):
    if not check_controler_in_controlers(user_id, subject):
        cur.execute('''INSERT INTO controlers VALUES(?,?);''', (subject, user_id))
        conn.commit()
        return 1
    else:
        return 0


def add_field(table: str, num: int, type: int, text: str = '', user_id: str = "-", status: str = "not complete", answer: str = "-", time: str = datetime.datetime.utcnow(),
                 score: int = 0, controler = ''):
    cur.execute(f'''INSERT INTO {table} VALUES(?,?,?,?,?,?,?,?,?);''', (num, type, text, user_id, status, answer, time, score, controler))
    conn.commit()

# delete role
def del_table(table: str):
    cur.execute(f'''DELETE FROM {table};''')
    conn.commit()


# update table

def update_status(table: str, num: int, type: int, user_id: str, status: str = "not complete"):
    cur.execute(f'''UPDATE {table} SET status = ?, datetime = ?, user_id = ? WHERE num_of_task IS ? AND type_of_task IS ?;''',
                (status, datetime.datetime.now(), user_id, num, type))
    conn.commit()


def update_answer(table: str, num: int, type: int, answer: str = "-"):
    cur.execute(f'''UPDATE {table} SET answer = ?, datetime = ? WHERE num_of_task IS ? AND type_of_task IS ?;''', (answer, datetime.datetime.utcnow(), num, type))
    conn.commit()


def update_date(table: str, num: int, type: int, time: str = datetime.datetime.now()):
    cur.execute(f'''UPDATE {table} SET datetime = ? WHERE num_of_task IS ? AND type_of_task IS ?;''',
                (time, num, type))
    conn.commit()

# Checkers
def check_user_in_users(user_id):
    cur.execute('''SELECT * FROM users WHERE user_id=?;''', (user_id,))
    return False if cur.fetchone() == None else True


def check_controler_in_controlers(user_id: str, subject: str):
    cur.execute('''SELECT * FROM controlers WHERE user_id=? AND subject=?;''', (user_id, subject))
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
    return True if (fetch[0] != 'not complete' and fetch[0] != 'complete') else False


def check_is_exist_status(table: str, user_id: str, status: str):
    cur.execute(f'''SELECT status FROM {table} WHERE status IS ? and user_id IS ?;''', (status, user_id,))
    return False if cur.fetchone() is None else True


# Getters

def get_user_info(user_id: str):
    cur.execute(f'''SELECT * FROM users WHERE user_id IS ?;''', (user_id,))
    buff = cur.fetchone()
    return buff


def get_controler_info(user_id: str):
    cur.execute(f'''SELECT subject FROM controlers WHERE user_id IS ?;''', (user_id,))
    buff = cur.fetchone()
    return None if buff == None else buff[0]



def get_free_numbers_and_text(table: str, type: int):
    cur.execute(f'''SELECT num_of_task, text FROM {table} WHERE status IS ? AND type_of_task IS ?;''', ('not complete', type))
    buff = cur.fetchall()
    return buff



def get_controlers_in_controlers(user_id: str):
    cur.execute('''SELECT subject FROM controlers WHERE user_id=?;''', (user_id,))
    buff = cur.fetchall()
    controlers = []
    for item in buff:
        controlers.append(item[0])
    return controlers

def get_now_task(table: str, user_id: str):
    cur.execute(f'''SELECT num_of_task, type_of_task, text FROM {table} WHERE user_id IS ? AND status IS ?;''', (user_id, 'in process',))
    return cur.fetchone()


def get_status(table: str, num: int, type: int):
    cur.execute(f'''SELECT status FROM {table} WHERE num_of_task IS ? AND type_of_task IS ?;''', (num, type,))
    status = cur.fetchone()[0]
    return status


def get_answer(table: str, num: int, type: int):
    cur.execute(f'''SELECT answer FROM {table} WHERE num_of_task IS ? AND type_of_task IS ?;''', (num, type,))
    status = cur.fetchone()[0]
    return status


def get_text(table: str, num: int, type: int):
    cur.execute(f'''SELECT text FROM {table} WHERE num_of_task IS ? AND type_of_task IS ?;''', (num, type,))
    text = cur.fetchone()[0]
    return text


def get_info_by_status(table: str, user_id: str, status: str):
    cur.execute(f'''SELECT num_of_task, type_of_task, text FROM {table} WHERE status IS ? and user_id IS ?;''', (status, user_id,))
    info = cur.fetchone()
    return info


# Statistics
def inc_do(user_id: str):
    cur.execute(f'''SELECT count_all FROM users WHERE users.user_id IS ?;''', (user_id,))
    count = cur.fetchone()[0]
    count += 1
    cur.execute('''UPDATE users SET count_all = ? WHERE user_id IS ?;''', (count, user_id,))
    conn.commit()


def inc_refuse(user_id: str):
    cur.execute(f'''SELECT refuse_all FROM users WHERE users.user_id IS ?;''', (user_id,))
    refuse = cur.fetchone()[0]
    refuse += 1
    cur.execute('''UPDATE users SET refuse_all = ? WHERE user_id IS ?;''', (refuse, user_id,))
    conn.commit()


def inc_control(user_id: str):
    cur.execute(f'''SELECT control_all FROM users WHERE users.user_id IS ?;''', (user_id,))
    refuse = cur.fetchone()[0]
    refuse += 1
    cur.execute('''UPDATE users SET control_all = ? WHERE user_id IS ?;''', (refuse, user_id,))
    conn.commit()


def dec_do(user_id: str):
    cur.execute(f'''SELECT count_all FROM users WHERE users.user_id IS ?;''', (user_id,))
    count = cur.fetchone()[0]
    count -= 1
    cur.execute('''UPDATE users SET count_all = ? WHERE user_id IS ?;''', (count, user_id,))
    conn.commit()


def dec_refuse(user_id: str):
    cur.execute(f'''SELECT refuse_all FROM users WHERE users.user_id IS ?;''', (user_id,))
    refuse = cur.fetchone()[0]
    refuse -= 1
    cur.execute('''UPDATE users SET refuse_all = ? WHERE user_id IS ?;''', (refuse, user_id,))
    conn.commit()


def dec_control(user_id: str):
    cur.execute(f'''SELECT control_all FROM users WHERE users.user_id IS ?;''', (user_id,))
    refuse = cur.fetchone()[0]
    refuse -= 1
    cur.execute('''UPDATE users SET control_all = ? WHERE user_id IS ?;''', (refuse, user_id,))
    conn.commit()
