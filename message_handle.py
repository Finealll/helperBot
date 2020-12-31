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


    if len(data['object']['message']['attachments']) > 0:
        if data['object']['message']['attachments'][0]['type'] == 'doc':
            bot_methods.write_attachment(user_id, token, data['object']['message']['attachments'][0]['doc'])


    #with payoad
    if 'payload' in data['object']['message']:
        payload = json.loads(data['object']['message']['payload'])

        if 'command' in payload.keys() and payload['command'] == 'start':
            bot_methods.add_new_user(user_id, token)

        # Обработка кнопок с кастомными payloadами
        if 'type' in payload.keys():

            if payload['type'] == 'file_pushing':
                if payload['name'] == 'get_main_keyboard_with_exit':
                    bot_methods.go_home_without_saving(user_id, token, payload)
                elif payload['name'] == 'send_file':
                    bot_methods.send_file(user_id, token, payload)
                return

            if bot_methods.check_dialog(user_id, token):
                return

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
                    bot_methods.get_now_tasks(user_id, token)
                    # Отправка faq
                elif payload['name'] == 'get_faq':
                    bot_methods.get_faq(user_id, token)

            # change user data
            elif payload['type'] == 'change_info':
                # Изменение ролей
                if payload['name'] == 'change_role':
                    bot_methods.change_role(user_id, token, payload)

            # Add task
            if payload['type'] == 'add_task':
                bot_methods.add_task(user_id, token, payload)

            # Delete task
            if payload['type'] == 'delete_task':
                bot_methods.delete_task(user_id, token, payload)

            # Push task
            if payload['type'] == 'push_task':
                bot_methods.push_task(user_id, token, payload)


def event_handler(data, token):
    return 1


