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
    #buttons.append(kg.Button.text(label='Проверка качества', payload=payloads.payloads['get_roles_list']))
    buttons.append(kg.Button.text(label='FAQ', payload=payloads.payloads['get_faq']))
    generator = kg.KeyBoard(False, False, False)
    generator.load(buttons)
    kb = generator.get()
    return kb

def get_subjects_keyboard():
    buttons = []
    buttons.append(kg.Button.text(label=names.name_of_subject[0], payload=payloads.payloads['get_progers_types']))
    buttons.append(kg.Button.text(label=names.name_of_subject[1], payload=payloads.payloads['get_eltech_types']))
    buttons.append(kg.Button.text(label=names.name_of_subject[2], payload=payloads.payloads['get_math_types']))
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
        payload['text'] = free_numbers[i][1]
        payload['type_task'] = type
        buttons[j].append(kg.Button.text(str(free_numbers[i][0]), payload=payload))
    buttons.append([])
    buttons[j+1].append(kg.Button.text(label='Взять случайное задание', payload=payloads.payloads['get_random_number']))
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
    payload1 = payloads.payloads['send_file']
    payload2 = payloads.payloads['get_main_keyboard_with_exit']
    payload1['subject'] = payload2['subject'] = subject
    payload1['num'] = payload2['num'] = num
    payload1['type_task'] = payload2['type_task'] = type
    buttons.append(kg.Button.text(label='Отправить', payload=payload1, color='positive'))
    buttons.append(kg.Button.text(label='На главную', payload=payload2))
    generator = kg.KeyBoard()
    generator.load(buttons)
    kb = generator.get()
    return kb





