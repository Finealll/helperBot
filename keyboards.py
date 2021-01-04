import keyboard_generator as kg
import payloads, names, json, db_work

# Основная клавиатура
def get_main_keyboard(user_id):
    buttons = []
    buff = False
    for table in names.table_name:
        if db_work.check_is_exist_status(table, user_id, 'in process'):
            buff = True
    if buff:
        buttons.append(kg.Button.text(label='Текущее задание', payload=payloads.payloads['get_now_task']))
    else:
        buttons.append(kg.Button.text(label='Доступные задания', payload=payloads.payloads['get_tasks_list']))

        subject_controler = db_work.get_controler_info(user_id)
        if subject_controler is not None:
            tasks = db_work.get_tasks_for_control(names.subject_to_table[subject_controler])
            if len(tasks) > 0:
                payload = dict(payloads.payloads['get_quality_numbers'])
                payload['subject'] = subject_controler
                buttons.append(kg.Button.text(label='Проверка качества', payload=payload))


    buttons.append(kg.Button.text(label='Мой профиль', payload=payloads.payloads['get_profile']))
    buttons.append(kg.Button.text(label='FAQ', payload=payloads.payloads['get_faq']))
    generator = kg.KeyBoard(False, False, False)
    generator.load(buttons)
    kb = generator.get()
    return kb

def get_subjects_keyboard():
    buttons = []
    if db_work.check_free_numbers(names.table_name[0]):
        buttons.append(kg.Button.text(label=names.name_of_subject[0], payload=payloads.payloads['get_progers_types']))
    if db_work.check_free_numbers(names.table_name[1]):
        buttons.append(kg.Button.text(label=names.name_of_subject[1], payload=payloads.payloads['get_eltech_types']))
    if db_work.check_free_numbers(names.table_name[2]):
        buttons.append(kg.Button.text(label=names.name_of_subject[2], payload=payloads.payloads['get_math_types']))
    if db_work.check_free_numbers(names.table_name[3]):
        buttons.append(kg.Button.text(label=names.name_of_subject[3], payload=payloads.payloads['get_physics_types']))
    buttons.append(kg.Button.text(label='На главную', payload=payloads.payloads['get_main_keyboard']))
    generator = kg.KeyBoard()
    generator.load(buttons)
    kb = generator.get()
    return kb



def get_subjects_types_keyboard(type1, type2, type3):
    buttons = []
    if type1 is not None:
        buttons.append(kg.Button.text(label='Оценка знаний', payload=payloads.payloads[type1]))
    if type2 is not None:
        buttons.append(kg.Button.text(label='Оценка умений', payload=payloads.payloads[type2]))
    if type3 is not None:
        buttons.append(kg.Button.text(label='Задачи', payload=payloads.payloads[type3]))
    buttons.append(kg.Button.text(label='На главную', payload=payloads.payloads['get_main_keyboard']))
    generator = kg.KeyBoard()
    generator.load(buttons)
    kb = generator.get()
    return kb


def get_free_numbers_keyboard(subject, free_numbers, type):
    buttons = []
    payload = payloads.payloads['get_tasks']
    payload["subject"] = subject
    buttons.append([])
    buttons[0].append(kg.Button.text(label='Показать задания', payload=payload))
    j = 0
    for i in range(0, len(free_numbers)):
        if int(i / 5) == j:
            buttons.append([])
            j += 1
        payload = dict(payloads.payloads['add_task'])
        payload['subject'] = subject
        payload['number'] = free_numbers[i][0]
        payload['type_task'] = type
        buttons[j].append(kg.Button.text(str(free_numbers[i][0]), payload=payload))
    buttons.append([])
    buttons.append([])
    payload = payloads.payloads['get_random_number']
    payload['type_task'] = type
    payload['subject'] = subject
    buttons[j+1].append(kg.Button.text(label='Взять случайное задание', payload=payload))
    buttons[j+2].append(kg.Button.text(label='На главную', payload=payloads.payloads['get_main_keyboard']))
    generator = kg.KeyBoard()
    generator.extra_load(buttons)
    kb = generator.get()
    return kb


def get_now_task_keyboard(subject, num, type):
    buttons = []
    payload = payloads.payloads['push_task']
    payload['subject'] = subject
    payload['number'] = num
    payload['type_task'] = type
    buttons.append(kg.Button.text(label='Отправить', payload=payload, color='positive'))
    payload = payloads.payloads['delete_task']
    payload['subject'] = subject
    payload['number'] = num
    payload['type_task'] = type
    buttons.append(kg.Button.text(label='Отказаться', payload=payload, color='negative'))
    buttons.append(kg.Button.text(label='На главную', payload=payloads.payloads['get_main_keyboard']))
    generator = kg.KeyBoard(one_line=True)
    generator.load(buttons)
    kb = generator.get()
    return kb


def get_push_file_keyboard(subject, num, type):
    buttons = []
    payload2 = payloads.payloads['get_main_keyboard_with_exit']
    payload2['subject'] = subject
    payload2['num'] = num
    payload2['type_task'] = type
    # buttons.append(kg.Button.text(label='Отправить', payload=payload1, color='positive'))
    buttons.append(kg.Button.text(label='На главную', payload=payload2))
    generator = kg.KeyBoard()
    generator.load(buttons)
    kb = generator.get()
    return kb

def get_quality_number_keyboard(subject, num, type):
    buttons = []
    payload1 = dict(payloads.payloads['change_quality_score'])
    payload2 = dict(payloads.payloads['change_quality_score'])
    payload3 = dict(payloads.payloads['on_main_from_quality'])
    payload3['subject'] = payload2['subject'] = payload1['subject'] = subject
    payload3['num'] = payload2['num'] = payload1['num'] = num
    payload3['type_task'] = payload2['type_task'] = payload1['type_task'] = type
    payload2['score'] = 1
    payload1['score'] = 2

    buttons.append(kg.Button.text(label="Норм", color='positive', payload=payload1))
    buttons.append(kg.Button.text(label="Не норм", color='negative', payload=payload2))
    buttons.append(kg.Button.text(label="На главную", payload=payload3))
    generator = kg.KeyBoard(one_line=True)
    generator.load(buttons)
    kb = generator.get()
    return kb






