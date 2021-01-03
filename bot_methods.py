import vkAPI, keyboards, admin_db, db_work, names
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
        vkAPI.send_message(user_id, token, 'Ты добавлен')
    else:
        vkAPI.send_message(user_id, token, 'Ты уже есть в бд')


def go_home(user_id, token):
    vkAPI.send_message(user_id, token, "Главная:", keyboard=keyboards.get_main_keyboard())


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
        if db_work.check_is_exist_status(table, 'in process'):
            vkAPI.send_message(user_id, token, 'Нельзя взять больше одного задания за раз!\nВыполните текущее задание',
                               keyboard=keyboards.get_main_keyboard())
            return

    if db_work.check_is_added_task(table_name, payload['number'], payload['type_task']):
        free_numbers = db_work.get_free_numbers_and_text(table_name, payload['type_task'])
        vkAPI.send_message(user_id, token, 'Задание взял уже кто то другой( \nВозьмите другое',
                           keyboard=keyboards.get_free_numbers_keyboard(payload['subject'], free_numbers,
                                                                        payload['type_task']))
    else:
        db_work.update_field(table_name, payload['number'], payload['type_task'], 'in process', user_id)
        free_numbers = db_work.get_free_numbers_and_text(table_name, payload['type_task'])
        message = f'Добавлено:\n{payload["subject"]}. {get_type_question(payload["type_task"])}. №{payload["number"]}' \
                  f'\nЗадание: {payload["text"]}'
        vkAPI.send_message(user_id, token, message, keyboard=keyboards.get_free_numbers_keyboard(payload['subject'],
                                                                                                 free_numbers,
                                                                                                 payload['type_task']))


def delete_task(user_id, token, payload):
    table_name = names.subject_to_table[payload['subject']]
    if db_work.check_is_added_task_by_user(table_name, payload['number'], payload['type_task'], user_id):
        db_work.update_field(table_name, payload['number'], payload['type_task'])
        vkAPI.send_message(user_id, token, 'Задание успешно отвязано!')
        db_work.inc_refuse(user_id)
    else:
        vkAPI.send_message(user_id, token, 'Вы не являетесь (уже) исполнителем этого задания!')


def push_task(user_id, token, payload):
    table_name = names.subject_to_table[payload['subject']]
    if not db_work.check_is_added_task_by_user(table_name, payload['number'], payload['type_task'], user_id):
        vkAPI.send_message(user_id, token, 'Вы не являетесь (уже) исполнителем этого задания!')
        return
    db_work.update_status(table_name, payload['number'], payload['type_task'], 'loading')
    message = "Пришлите в диалог ответ на вопрос в формате .docx / .doc, затем нажмите кнопку отправить."
    keyboard = keyboards.get_push_file_keyboard(payload['subject'], payload['number'], payload['type_task'])
    vkAPI.send_message(user_id, token, message, keyboard=keyboard)



def get_type_question(type:int):
    if type == 1:
        return 'оценка знаний'
    if type == 2:
        return 'оценка умений'
    if type == 3:
        return 'задача'


def get_now_tasks(user_id, token):
    count = 0
    for i in range(len(names.table_name)):
        arr = db_work.get_now_tasks(names.table_name[i], user_id)
        for item in arr:
            message = f'{names.name_of_subject[i]}. {str(get_type_question(item[1])).capitalize()}. Номер {item[0]}'
            keyboard = keyboards.get_now_task_keyboard(names.name_of_subject[i], item[0], item[1])
            vkAPI.send_message(user_id, token, message, keyboard=keyboard)
            count += 1
    if count == 0:
        vkAPI.send_message(user_id, token, 'У вас нет заданий!')


def get_faq(user_id, token):
    vkAPI.send_message(user_id, token, names.faq)


def check_dialog(user_id, token):
    for table in names.table_name:
        if db_work.check_is_exist_status(table, 'loading'):
            vkAPI.send_message(user_id, token, 'Для совершения этого действия выйдите из диалога загрузки файлов!')
            return True
    return False


def write_attachment(user_id, token, attachment):
    answer = str(attachment['owner_id'])+'_'+str(attachment['id'])
    for table in names.table_name:
        if db_work.check_is_exist_status(table, 'loading'):
            info = db_work.get_info_by_status(table, 'loading')[0]
            db_work.update_answer(table, info[0], info[1], answer)


def send_file(user_id, token, payload):
    table_name = names.subject_to_table[payload['subject']]
    answer = db_work.get_answer(table_name, payload['num'], payload['type_task'])
    if answer == '-':
        vkAPI.send_message(user_id, token, "Отправьте документ в чат перед нажатием на кнопку!")
        return
    else:
        db_work.update_status(table_name, payload['num'], payload['type_task'], 'complete')
        db_work.inc_do(user_id)
        go_home(user_id, token)



def go_home_without_saving(user_id, token, payload):
    db_work.update_field(names.subject_to_table[payload['subject']], payload['num'], payload['type_task'], 'in process',
                         user_id, '-')
    go_home(user_id, token)


