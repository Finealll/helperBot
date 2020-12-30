import vkAPI, keyboards, admin_db, db_work
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    names = vkAPI.get_user_info(user_id, token)

    # start
    #no payload:
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
        vkAPI.send_message(user_id, token, "Привет!", keyboard=keyboards.get_main_keyboard())



    #with payoad
    if 'payload' in data['object']['message']:
        payload = json.loads(data['object']['message']['payload'])

        # Обработка кнопок с кастомными payloadами
        if 'type' in payload.keys():
            # open keyboards
            if payload['type'] == 'open_keyboard':
                if payload['name'] == 'get_tasks_list':
                    vkAPI.send_message(user_id, token, "Переход к предметам")
                #Отправка сообщения с ролями
                elif payload['name'] == 'get_roles_list':
                    buff = db_work.get_roles_in_roles(user_id)
                    roles = []
                    for item in buff:
                        roles.append(item[0])
                    vkAPI.send_message(user_id, token, 'Роли:', keyboard=keyboards.get_roles_keyboard(roles))

            # send info message
            elif payload['type'] == 'send_info_message':
                #Отправка сообщения с текущими заданиями
                if payload['name'] == 'get_now_tasks_list':
                    vkAPI.send_message(user_id, token, "Переход к текущим заданиям")






def event_handler(data, token):
    return 1


