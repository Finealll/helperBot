import vkAPI, bot_methods, names
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    user_info = vkAPI.get_user_info(user_id, token)


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
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[0], 1)
                elif payload['name'] == 'get_progers_type2':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[0], 2)
                elif payload['name'] == 'get_progers_type3':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[0], 3)
                elif payload['name'] == 'get_eltech_type1':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[1], 1)
                elif payload['name'] == 'get_eltech_type2':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[1], 2)
                elif payload['name'] == 'get_eltech_type3':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[1], 3)
                elif payload['name'] == 'get_math_type1':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[2], 1)
                elif payload['name'] == 'get_math_type2':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[2], 2)
                elif payload['name'] == 'get_math_type3':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[2], 3)
                elif payload['name'] == 'get_physics_type1':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[3], 1)
                elif payload['name'] == 'get_physics_type2':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[3], 2)
                elif payload['name'] == 'get_physics_type3':
                    bot_methods.get_free_progers_numbers(user_id, token, names.table_name[3], 3)
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


