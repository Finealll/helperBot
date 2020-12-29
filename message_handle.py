import vkAPI, keyboard_generator, db_work, admin_db
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    names = vkAPI.get_user_info(user_id, token)

    #start
    if 'command' in data['object']['payload'].keys():
        if data['object']['payload']['command'] == 'start':
            db_work.add_user(user_id, names[0], names[1])
            vkAPI.send_message(user_id, token, "Произошел старт, пользователь добавлен в бд")
    #admin
    elif data['object']['message']['text'] == 'admin_delete_users!':
        admin_db.ClearUsers()
        vkAPI.send_message(user_id, token, "Пользователи удаоены")
    elif data['object']['message']['text'] == 'admin_get_users!':
        users = admin_db.GetUsers()
        for user in users:
            vkAPI.send_message(user_id, token, message=user[1]+" "+user[2])


    #vkAPI.send_message(user_id=user_id, token=token, message=str(names[0]+" "+names[1]), keyboard=keyboard_generator.get_main_keyboard())


def event_handler(data, token):
    return 1


