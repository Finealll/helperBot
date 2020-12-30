import vkAPI, keyboards, admin_db, db_work
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
def go_home(user_id, token):
    vkAPI.send_message(user_id, token, "Главная:", keyboard=keyboards.get_main_keyboard())


def get_task_list(user_id, token):
    roles = db_work.get_roles_in_roles(user_id)
    if len(roles) == 0:
        vkAPI.send_message(user_id, token, 'У вас нет ролей!\nДобавьте себе роль, станьте человеком!',
                           keyboard=keyboards.get_roles_keyboard(roles))
    else:
        vkAPI.send_message(user_id, token, 'Выберите предмет:',
                           keyboard=keyboards.get_subjects_keyboard(roles))


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

