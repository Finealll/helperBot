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

            # send info message
            elif payload['type'] == 'send_info_message':
                #Отправка сообщения с ролями
                if payload['name'] == 'get_roles_list':
                    roles = db_work.get_roles_in_roles(user_id)
                    print(roles)
                    if roles is None:
                        message = "У вас пока что нет ролей!\nДобавьте же их!"
                    else:
                        message = "Ваши текущие роли:"
                        for role in roles:
                            message += "\n"+str(role[0])
                    vkAPI.send_message(user_id, token, message, keyboards.get_roles_keyboard(roles))


                #Отправка сообщения с текущими заданиями
                elif payload['name'] == 'get_now_tasks_list':
                    vkAPI.send_message(user_id, token, "Переход к текущим заданиям")






def event_handler(data, token):
    return 1


