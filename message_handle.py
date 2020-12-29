import vkAPI, keyboard_generator, db_work, admin_db
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    names = vkAPI.get_user_info(user_id, token)
    payload = json.loads(data['object']['message']['payload'])

    # start

    # admin
    if data['object']['message']['text'] == 'admin_delete_users!':
        admin_db.ClearUsers()
        vkAPI.send_message(user_id, token, "Пользователи удаоены")
    elif data['object']['message']['text'] == 'admin_get_users!':
        users = admin_db.GetUsers()
        for user in users:
            vkAPI.send_message(user_id, token, message=user[0]+" "+user[1]+" "+user[2])
    # Main
    if data['object']['message']['text'] == 'На главную':
        vkAPI.send_message(user_id, token, "Привет!", keyboard=keyboard_generator.get_main_keyboard())

    # open keyboards
    if 'type' in payload.keys():
        if payload['type'] == 'open_keyboard':
            if payload['name'] == 'get_tasks_list':
                vkAPI.send_message(user_id, token, "Переход к предметам")
            elif payload['name'] == 'get_roles_list':
                vkAPI.send_message(user_id, token, "Переход к ролям")
            elif payload['name'] == 'get_now_tasks_list':
                vkAPI.send_message(user_id, token, "Переход к текущим заданиям")






def event_handler(data, token):
    return 1


