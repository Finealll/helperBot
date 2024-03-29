import vkAPI, bot_methods, names, admin_db
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    user_info = vkAPI.get_user_info(user_id, token)

    # vkAPI.send_message(user_id, token, 'Обновляю бота до 2:00')
    # return

    #no payload:
    # admin
    # if data['object']['message']['text'] == 'admin_delete_users!':
    #     bot_methods.admin_delete_users(user_id, token)
    #     return
    if data['object']['message']['text'] == 'admin_get_users!':
        bot_methods.admin_get_users(user_id, token)
        return
    # elif data['object']['message']['text'] == 'admin_addme!':
    #     bot_methods.add_new_user(user_id, token)
    #     return
    # elif data['object']['message']['text'] == 'admin_cldbs!':
    #     admin_db.get_clear_tables()
    #     vkAPI.send_message(user_id, token, 'Все бд очищены!')
    #     return
    # elif data['object']['message']['text'] == 'admin_cl!':
    #     admin_db.get_clear()
    #     vkAPI.send_message(user_id, token, 'Бд с заданиями очищены!')
    #     return
    elif data['object']['message']['text'] == 'admin_get_keyboard!':
        bot_methods.go_home(user_id, token)
        return
    elif data['object']['message']['text'].upper() == 'НАЧАТЬ':
        if bot_methods.check_dialog(user_id, token):
            return
        bot_methods.add_new_user(user_id, token)
        bot_methods.go_home(user_id, token)
        return
    elif data['object']['message']['text'].upper() == 'ПОШЕЛ НАХУЙ':
        bot_methods.send_go_to_hell(user_id, token, user_info[0] )
        return



    elif len(data['object']['message']['attachments']) > 0:
        if data['object']['message']['attachments'][0]['type'] == 'doc':
            if data['object']['message']['attachments'][0]['doc']['ext'] == 'docx':
                bot_methods.write_attachment(user_id, token, data['object']['message']['attachments'][0]['doc'])
            else:
                vkAPI.send_message(user_id, token, 'Отправьте файл в формате .docx')


    #with payoad
    elif 'payload' in data['object']['message']:
        payload = json.loads(data['object']['message']['payload'])

        if 'command' in payload.keys() and payload['command'] == 'start':
            bot_methods.add_new_user(user_id, token)
            bot_methods.go_home(user_id, token)

        # Обработка кнопок с кастомными payloadами
        elif 'type' in payload.keys():

            if payload['type'] == 'file_pushing':
                if payload['name'] == 'get_main_keyboard_with_exit':
                    bot_methods.go_home_without_saving(user_id, token, payload)
                # elif payload['name'] == 'send_file':
                #     bot_methods.send_file(user_id, token, payload)
                return

            elif bot_methods.check_dialog(user_id, token):
                return

            # open keyboards
            elif payload['type'] == 'open_keyboard':
                # Переход на главную
                if payload['name'] == 'get_main_keyboard':
                    bot_methods.go_home(user_id, token)
                    # Домой из проверки качества
                elif payload['name'] == 'on_main_from_quality':
                    bot_methods.on_main_from_quality(user_id, token, payload)
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

            # send docs
            elif payload['type'] == 'get_doc':
                # Отправка документов с заданием
                if payload['name'] == 'get_tasks':
                    bot_methods.get_tasks(user_id, token, payload)


            # send info message
            elif payload['type'] == 'send_info_message':
                # Отправка сообщения с текущими заданиями
                if payload['name'] == 'get_now_task':
                    bot_methods.get_now_task(user_id, token)
                    # Отправка faq
                elif payload['name'] == 'get_faq':
                    bot_methods.get_faq(user_id, token)
                    #Отправка инфы о профиле
                elif payload['name'] == 'get_profile':
                    bot_methods.get_profile(user_id, token)


            # Add task
            elif payload['type'] == 'add_task':
                bot_methods.add_task(user_id, token, payload)

            # Delete task
            elif payload['type'] == 'delete_task':
                bot_methods.delete_task(user_id, token, payload)

            # Push task
            elif payload['type'] == 'push_task':
                bot_methods.push_task(user_id, token, payload)

            # Random nunmer
            elif payload['type'] == 'get_random_number':
                bot_methods.add_random_number(user_id, token, payload)

            # check quality
            elif payload['type'] == 'check_quality':
                # Получение рандомного номера с заданием
                if payload['name'] == 'get_quality_num':
                    bot_methods.get_quality_num(user_id, token, payload)
                # Отправка отзыва на задание
                if payload['name'] == 'change_quality_score':
                    bot_methods.change_quality_score(user_id, token, payload)

            #Change info
            elif payload['type'] == 'change_info':
                # Свитчер уведомлений
                if payload['name'] == 'change_notify':
                    bot_methods.change_notify(user_id, token, payload)





def event_handler(data, token):
    return 1


