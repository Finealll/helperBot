import vkAPI, keyboards, admin_db, db_work, names
import json


# admin methods
def admin_get_users(user_id, token):
    users = admin_db.GetUsers()
    for user in users:
        vkAPI.send_message(user_id, token, message=user[0]+" "+user[1]+" "+user[2])


def admin_delete_users(user_id, token):
    admin_db.ClearUsers()
    vkAPI.send_message(user_id, token, "Пользователи удалены")


# user methods
# Main
def go_home(user_id, token):
    vkAPI.send_message(user_id, token, "Главная:", keyboard=keyboards.get_main_keyboard())


# Work with tasks
def get_task_list(user_id, token):
    roles = db_work.get_roles_in_roles(user_id)
    if len(roles) == 0:
        vkAPI.send_message(user_id, token, 'У вас нет ролей!\nДобавьте себе роль, станьте человеком!',
                           keyboard=keyboards.get_roles_keyboard(roles))
    else:
        vkAPI.send_message(user_id, token, 'Выберите предмет:',
                           keyboard=keyboards.get_subjects_keyboard(roles))


def get_subject_types(user_id, token, payload):
    type1 = None
    type2 = None
    type3 = None
    if db_work.check_free_numbers_by_status_and_type(payload['table_name'], 1):
        type1 = payload['subtype1']
    if db_work.check_free_numbers_by_status_and_type(payload['table_name'], 2):
        type1 = payload['subtype2']
    if db_work.check_free_numbers_by_status_and_type(payload['table_name'], 3):
        type1 = payload['subtype3']
    keyboard = keyboards.get_subjects_types_keyboard(type1, type2, type3)
    vkAPI.send_message(user_id, token, "Выберите тип заданий", keyboard=keyboard)


def get_free_progers_numbers(user_id, token, table_name, type):
    free_numbers = db_work.get_free_numbers(table_name, type)
    keyboard = keyboards.get_free_numbers_keyboard(names.name_of_subject[0], free_numbers, 1)
    vkAPI.send_message(user_id, token, "Выберите задания", keyboard=keyboard)


# Work with roles
def get_roles_list(user_id, token):
    roles = db_work.get_roles_in_roles(user_id)
    vkAPI.send_message(user_id, token, 'Роли:', keyboard=keyboards.get_roles_keyboard(roles))


def change_role(user_id, token, payload):
    availability = db_work.check_roles_in_roles(user_id, payload['role'])
    if payload['do'] == 'add':
        if availability:
            message = "У вас уже есть эта роль!"
        elif not availability:
            db_work.add_role(user_id, payload['role'])
            message = "Роль " + payload['role'] + " добавлена"
    elif payload['do'] == 'delete':
        if not availability:
            message = "У вас нет этой роли!"
        elif availability:
            db_work.del_role(user_id, payload['role'])
            message = "Роль " + payload['role'] + " удалена"
    roles = db_work.get_roles_in_roles(user_id)
    vkAPI.send_message(user_id, token, message, keyboard=keyboards.get_roles_keyboard(roles))

