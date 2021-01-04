import vkAPI, keyboards, admin_db, db_work, names, random, os, requests, VKsettings
import json


# admin methods
def admin_get_users(user_id, token):
    users = admin_db.GetUsers()
    for user in users:
        vkAPI.send_message(user_id, token, message=user[0] + " " + user[1] + " " + user[2])


def admin_delete_users(user_id, token):
    admin_db.ClearUsers()
    vkAPI.send_message(user_id, token, "Пользователи удалены")





# user methods
# Main

def add_new_user(user_id, token):
    info = vkAPI.get_user_info(user_id, token)
    if not db_work.check_user_in_users(user_id):
        db_work.add_user(user_id, info[0], info[1])


def go_home(user_id, token):
    vkAPI.send_message(user_id, token, "Главная:", keyboard=keyboards.get_main_keyboard(user_id))
    check_returned(user_id, token)


# Work with tasks
def get_task_list(user_id, token):
    vkAPI.send_message(user_id, token, 'Выберите предмет:',
                       keyboard=keyboards.get_subjects_keyboard())


def get_subject_types(user_id, token, payload):
    type1 = None
    type2 = None
    type3 = None
    if db_work.check_free_numbers_by_status_and_type(payload['table_name'], 1):
        type1 = payload['subtype_1']
    if db_work.check_free_numbers_by_status_and_type(payload['table_name'], 2):
        type2 = payload['subtype_2']
    if db_work.check_free_numbers_by_status_and_type(payload['table_name'], 3):
        type3 = payload['subtype_3']
    keyboard = keyboards.get_subjects_types_keyboard(type1, type2, type3)
    vkAPI.send_message(user_id, token, "Выберите тип заданий", keyboard=keyboard)


def get_free_progers_numbers(user_id, token, table_name, type):
    free_numbers = db_work.get_free_numbers_and_text(table_name, type)
    keyboard = keyboards.get_free_numbers_keyboard(names.table_to_subject[table_name], free_numbers, type)
    vkAPI.send_message(user_id, token, "Выберите задания", keyboard=keyboard)



# Work with tasks
def add_task(user_id, token, payload):
    table_name = names.subject_to_table[payload['subject']]
    for table in names.table_name:
        if db_work.check_is_exist_status(table, user_id, 'in process'):
            vkAPI.send_message(user_id, token, 'Нельзя взять больше одного задания за раз!\nВыполните текущее задание',
                               keyboard=keyboards.get_main_keyboard(user_id))
            return

    if db_work.check_is_added_task(table_name, payload['number'], payload['type_task']):
        free_numbers = db_work.get_free_numbers_and_text(table_name, payload['type_task'])
        vkAPI.send_message(user_id, token, 'Задание взял уже кто то другой( \nВозьмите другое',
                           keyboard=keyboards.get_free_numbers_keyboard(payload['subject'], free_numbers,
                                                                        payload['type_task']))
    else:
        db_work.update_status(table_name, payload['number'], payload['type_task'], user_id, 'in process')
        free_numbers = db_work.get_free_numbers_and_text(table_name, payload['type_task'])
        text = db_work.get_text(table_name, payload["number"], payload['type_task'])
        if payload["type_task"] == 3:
            message = f'Добавлено:\n{payload["subject"]}. {get_type_question(payload["type_task"]).capitalize()}. №{payload["number"]}' \
                      f'\nЗадание: во вложении'
            vkAPI.send_message(user_id, token, message, attachment=text, keyboard=keyboards.get_main_keyboard(user_id))
        else:
            message = f'Добавлено:\n{payload["subject"]}. {get_type_question(payload["type_task"]).capitalize()}. №{payload["number"]}' \
                      f'\nЗадание: {text}'
            vkAPI.send_message(user_id, token, message, keyboard=keyboards.get_main_keyboard(user_id))


def add_random_number(user_id, token, payload):
    table_name = names.subject_to_table[payload['subject']]
    for table in names.table_name:
        if db_work.check_is_exist_status(table, user_id, 'in process'):
            vkAPI.send_message(user_id, token, 'Нельзя взять больше одного задания за раз!\nВыполните текущее задание',
                               keyboard=keyboards.get_main_keyboard(user_id))
            return
    free_numbers1 = db_work.get_free_numbers_and_text(table_name, payload['type_task'])
    if len(free_numbers1) == 0:
        vkAPI.send_message(user_id, token, "Задания по этому предмету закончились!", keyboard=keyboards.get_main_keyboard(user_id))
    index = random.randint(1, len(free_numbers1))
    index -= 1

    if db_work.check_is_added_task(table_name, free_numbers1[index][0], payload['type_task']):
        add_random_number(user_id, token, payload)
    else:
        db_work.update_status(table_name, free_numbers1[index][0], payload['type_task'], user_id, 'in process')
        if payload["type_task"] == 3:
            message = f'Добавлено:\n{payload["subject"]}. {get_type_question(payload["type_task"]).capitalize()}. №{free_numbers1[index][0]}' \
                      f'\nЗадание: во вложении'
            vkAPI.send_message(user_id, token, message, attachment=free_numbers1[index][1], keyboard=keyboards.get_main_keyboard(user_id))
        else:
            message = f'Добавлено:\n{payload["subject"]}. {get_type_question(payload["type_task"]).capitalize()}. №{free_numbers1[index][0]}' \
                      f'\nЗадание: {free_numbers1[index][1]}'
            vkAPI.send_message(user_id, token, message, keyboard=keyboards.get_main_keyboard(user_id))



def delete_task(user_id, token, payload):
    table_name = names.subject_to_table[payload['subject']]
    if db_work.check_is_added_task_by_user(table_name, payload['number'], payload['type_task'], user_id):
        db_work.update_status(table_name, payload['number'], payload['type_task'], '-', 'not complete')
        vkAPI.send_message(user_id, token, 'Задание успешно отвязано!', keyboard=keyboards.get_main_keyboard(user_id))
        db_work.inc_refuse(user_id)
    else:
        vkAPI.send_message(user_id, token, 'Вы не являетесь (уже) исполнителем этого задания!')
    check_returned(user_id, token)


def push_task(user_id, token, payload):
    table_name = names.subject_to_table[payload['subject']]
    if not db_work.check_is_added_task_by_user(table_name, payload['number'], payload['type_task'], user_id):
        vkAPI.send_message(user_id, token, 'Вы не являетесь (уже) исполнителем этого задания!')
        return
    db_work.update_status(table_name, payload['number'], payload['type_task'], user_id, 'loading')
    message = "Пришлите в диалог ответ на вопрос в формате .docx, затем нажмите кнопку отправить."
    keyboard = keyboards.get_push_file_keyboard(payload['subject'], payload['number'], payload['type_task'])
    vkAPI.send_message(user_id, token, message, keyboard=keyboard)



def get_type_question(type:int):
    if type == 1:
        return 'оценка знаний'
    if type == 2:
        return 'оценка умений'
    if type == 3:
        return 'задача'


def get_now_task(user_id, token):
    buff = False
    for table in names.table_name:
        if db_work.check_is_exist_status(table, user_id, 'in process'):
            task = db_work.get_now_task(table, user_id)
            keyboard = keyboards.get_now_task_keyboard(names.table_to_subject[table], task[0], task[1])
            if task[1] == 3:
                message = f'Текущее задание:\n{names.table_to_subject[table]}. {get_type_question(task[1]).capitalize()}. №{task[0]}' \
                          f'\nЗадание: во вложении'
                vkAPI.send_message(user_id, token, message, attachment=task[2], keyboard=keyboard)
            else:
                message = f'Текущее задание:\n{names.table_to_subject[table]}. {get_type_question(task[1]).capitalize()}. №{task[0]}' \
                          f'\nЗадание: {task[2]}'
                vkAPI.send_message(user_id, token, message, keyboard=keyboard)
            buff = True
    if not buff:
        vkAPI.send_message(user_id, token, 'У вас нет заданий!', keyboard=keyboards.get_main_keyboard(user_id))


def get_faq(user_id, token):
    vkAPI.send_message(user_id, token, names.faq)


def check_dialog(user_id, token):
    for table in names.table_name:
        if db_work.check_is_exist_status(table, user_id, 'loading'):
            vkAPI.send_message(user_id, token, 'Для совершения этого действия выйдите из диалога загрузки файлов!')
            return True
    return False


def write_attachment(user_id, token, attachment):
    info = None
    _table = ""
    for table in names.table_name:
        if db_work.check_is_exist_status(table, user_id, 'loading'):
            info = db_work.get_info_by_status(table, user_id, 'loading')
            _table = table
            break
    if info is not None:
        url = attachment['url']
        response = requests.get(url)

        name = f'{names.table_to_subject[_table]} {get_type_question(info[1])} {info[0]}.docx'
        file = open(name, 'wb')
        file.write(response.content)
        file.close()

        upload_url = vkAPI.api.docs.getWallUploadServer(access_token=VKsettings.token, group_id=names.id_community)[
            'upload_url']
        filestr = requests.post(upload_url, files={'file': open(name, 'rb')}).json()['file']
        file.close()
        os.remove(name)

        response = vkAPI.api.docs.save(access_token=VKsettings.token, file=filestr)
        answer = 'doc'+str(response['doc']['owner_id']) + '_' + str(response['doc']['id'])
        db_work.update_answer(_table, info[0], info[1], answer)
        vkAPI.send_message(user_id, token, "Файл успешно загружен!")

        db_work.update_status(_table, info[0], info[1], user_id, 'complete')
        db_work.update_score(_table, info[0], info[1], 0)
        db_work.inc_do(user_id)
        vkAPI.send_message(user_id, token, "Задание успешно отправлено!")

        subj = db_work.get_controler_info(user_id)
        if subj is not None:
            if subj == names.table_to_subject[_table]:
                db_work.update_score(_table, info[0], info[1], 2)
                db_work.update_controler_from_task(_table, info[0], info[1], user_id)


        check_returned(user_id, token)
        go_home(user_id, token)

    else:
        vkAPI.send_message(user_id, token, 'Файл не распознан!', keyboard=keyboards.get_main_keyboard(user_id))

# def send_file(user_id, token, payload):
#     table_name = names.subject_to_table[payload['subject']]
#     answer = db_work.get_answer(table_name, payload['num'], payload['type_task'])
#     if answer == '-':
#         vkAPI.send_message(user_id, token, "Отправьте документ в чат перед нажатием на кнопку!")
#         return
#     else:
#         db_work.update_status(table_name, payload['num'], payload['type_task'], user_id, 'complete')
#         db_work.update_score(table_name, payload['num'], payload['type_task'], 0)
#         db_work.inc_do(user_id)
#         vkAPI.send_message(user_id, token, "Задание успешно отправлено!")
#
#
#         check_returned(user_id, token)
#         go_home(user_id, token)



def check_returned(user_id, token):
    for table in names.table_name:
        if db_work.check_is_exist_status(table, user_id, 'returned'):
            info = db_work.get_info_by_status(table, user_id, 'returned')
            db_work.update_status(table, info[0], info[1], user_id, 'in process')
            answer = db_work.get_answer(table, info[0], info[1])
            db_work.update_answer(table, info[0], info[1])
            controler = vkAPI.get_user_info(db_work.get_controler_from_task(table, info[0], info[1]), token)

            if info[1] == 3:
                message = f'Вам добавлено задание:\n{names.table_to_subject[table]}. {get_type_question(info[1])}. №{info[0]}\n' \
                          f'Причина: не прошло проверку качества!\nПроверяющий: {controler[1]} {controler[0]}\nЗадание: во вложении' \
                          f'\nВаш ответ: во вложении'
                vkAPI.send_message(user_id, token, message, attachment=str(answer+','+info[2]),
                                   keyboard=keyboards.get_main_keyboard(user_id))
            else:
                message = f'Вам добавлено задание:\n{names.table_to_subject[table]}. {get_type_question(info[1])}. №{info[0]}\n' \
                          f'Причина: не прошло проверку качества!\nПроверяющий: {controler[1]} {controler[0]}' \
                          f'\nЗадание: {info[2]}\nВаш ответ: во вложении'
                vkAPI.send_message(user_id, token, message, attachment=answer, keyboard=keyboards.get_main_keyboard(user_id))



def go_home_without_saving(user_id, token, payload):
    db_work.update_status(names.subject_to_table[payload['subject']], payload['num'], payload['type_task'], user_id, 'in process')
    db_work.update_answer(names.subject_to_table[payload['subject']], payload['num'], payload['type_task'])
    go_home(user_id, token)


def get_tasks(user_id, token, payload):
    for item in names.questions:
        if item['subject'] == payload['subject']:
            attachment = item['attachment']
            break
    vkAPI.send_message(user_id, token, 'Задания:', attachment=attachment)


def get_profile(user_id, token):
    add_new_user(user_id, token)
    user_info = db_work.get_user_info(user_id)
    subject_controler = db_work.get_controler_info(user_id)
    message = f'{user_info[1]} {user_info[2]}\nВсего выполнено заданий: {user_info[3]}'
    if subject_controler is not None:
        message += f"\nЭксперт в предмете {subject_controler}\nВсего проверил заданий: {user_info[5]}"
    vkAPI.send_message(user_id, token, message)


def get_quality_num(user_id, token, payload):
    subject = payload['subject']
    tasks = db_work.get_tasks_for_control(names.subject_to_table[subject])
    if len(tasks) > 0:
        num = random.randint(0, len(tasks)-1)
        user = vkAPI.get_user_info(tasks[num][3], token)
        db_work.update_score(names.subject_to_table[subject], tasks[num][0], tasks[num][1], 3)
        keyboard = keyboards.get_quality_number_keyboard(subject, tasks[num][0], tasks[num][1])
        if tasks[num][1] == 3:
            message = f"Проверьте качество выполнения:\n{subject}. {get_type_question(tasks[num][1])} №{tasks[num][0]}\n" \
                      f"Исполнитель: {user[1]} {user[0]}\n" \
                      f"Задание: во вложении\n" \
                      f"Ответ: во вложении"
            vkAPI.send_message(user_id, token, message, attachment=str(tasks[num][4]+','+tasks[num][2]), keyboard=keyboard)
        else:
            message = f"Проверьте качество выполнения:\n{subject}. {get_type_question(tasks[num][1])} №{tasks[num][0]}\n" \
                      f"Исполнитель: {user[1]} {user[0]}\n" \
                      f"Задание: {tasks[num][2]}\n" \
                      f"Ответ: во вложении"
            vkAPI.send_message(user_id, token, message, attachment=tasks[num][4], keyboard=keyboard)
    else:
        vkAPI.send_message(user_id, token, 'Увы, все задания для проверки качества уже разобрали!',
                           keyboard=keyboards.get_main_keyboard(user_id))


def change_quality_score(user_id, token, payload):
    db_work.update_score(names.subject_to_table[payload['subject']], payload['num'], payload['type_task'], payload['score'])
    if payload['score'] == 1:
        buff = True
        table = names.subject_to_table[payload['subject']]
        user = db_work.get_user_id_in_task(table, payload['num'], payload['type_task'])
        db_work.update_status(table, payload['num'], payload['type_task'], user, 'returned')
        db_work.dec_do(user)
        db_work.update_controler_from_task(table, payload['num'], payload['type_task'], user_id)
        for _table in names.table_name:
            if db_work.check_is_exist_status(_table, user, 'in process') or db_work.check_is_exist_status(_table, user, 'loading'):
                info = vkAPI.get_user_info(user_id, token)
                message = f"Привет!\nТвое задание {payload['subject']}. {get_type_question(payload['type_task'])} №{payload['num']}\n" \
                          f"было отклонено экспертом и добавлено тебе в очередь!" \
                          f"Проверяющий: {info[1]} {info[0]}"
                vkAPI.send_message(user, token, message)
                buff = False
                break
        if buff:
            check_returned(user, token)
    vkAPI.send_message(user_id, token, 'Спасибо за вашу оценку!', keyboard=keyboards.get_main_keyboard(user_id))
    db_work.inc_control(user_id)






def on_main_from_quality(user_id, token, payload):
    db_work.update_score(names.subject_to_table[payload['subject']], payload['num'], payload['type_task'], 0)
    go_home(user_id, token)