import vkAPI, bot_methods
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    names = vkAPI.get_user_info(user_id, token)


    #no payload:
    # admin
    if data['object']['message']['text'] == 'admin_delete_users!':
        bot_methods.admin_delete_users(user_id, token)
    elif data['object']['message']['text'] == 'admin_get_users!':
        bot_methods.admin_get_users(user_id, token)

    #with payoad
    if 'payload' in data['object']['message']:
        payload = json.loads(data['object']['message']['payload'])

        # Обработка кнопок с кастомными payloadами
        if 'type' in payload.keys():
            # open keyboards
            if payload['type'] == 'open_keyboard':
                # Переход на главную
                if payload['name'] == 'get_main_keyboard':
                    bot_methods.go_home(user_id, token)
                # Переход к предметам по ролям
                elif payload['name'] == 'get_tasks_list':
                    bot_methods.get_task_list(user_id, token)
                # Переход к типам предметов
                elif payload['name'] == 'get_progers_types':
                    bot_methods.get_subject_types(user_id, token, payload)
                elif payload['name'] == 'get_eltech_types':
                    bot_methods.get_subject_types(user_id, token, payload)
                elif payload['name'] == 'get_physics_types':
                    bot_methods.get_subject_types(user_id, token, payload)
                elif payload['name'] == 'get_math_types':
                    bot_methods.get_subject_types(user_id, token, payload)
                # Переход к номерам
                elif payload['name'] == 'get_progers_type1':
                    bot_methods.get_free_progers_numbers_1(user_id, token)
                # Переход к выбору ролей
                elif payload['name'] == 'get_roles_list':
                    bot_methods.get_roles_list(user_id, token)

            # send info message
            elif payload['type'] == 'send_info_message':
                # Отправка сообщения с текущими заданиями
                if payload['name'] == 'get_now_tasks_list':
                    vkAPI.send_message(user_id, token, "Переход к текущим заданиям")

            # change user data
            elif payload['type'] == 'change_info':
                # Изменение ролей
                if payload['name'] == 'change_role':
                    bot_methods.change_role(user_id, token, payload)


def event_handler(data, token):
    return 1


