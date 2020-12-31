import keyboard_generator as kg
import payloads, names, json

# Основная клавиатура
def get_main_keyboard():
    buttons = []
    buttons.append(kg.Button.text(label='Доступные задания', payload=payloads.payloads['get_tasks_list']))
    buttons.append(kg.Button.text(label='Мои задания', payload=payloads.payloads['get_now_tasks_list']))
    buttons.append(kg.Button.text(label='Роли', payload=payloads.payloads['get_roles_list']))
    buttons.append(kg.Button.text(label='FAQ', payload=payloads.payloads['get_faq']))
    generator = kg.KeyBoard(False, False, False)
    generator.load(buttons)
    kb = generator.get()
    return kb

#Inline клава для сообщения с ролями
def get_roles_keyboard(roles_now):
    buttons = []
    if names.roles[4] in roles_now:
        payload = dict(payloads.payloads['change_role'])
        payload['role'] = names.roles[4]
        payload['do'] = 'delete'
        buttons.append(kg.Button.text(label='Удалить роль \"' + names.roles[4] + '\"', payload=payload, color='negative'))
    else:
        for role in names.roles:
            payload = dict(payloads.payloads['change_role'])
            payload['role'] = role
            if role in roles_now:
                payload['do'] = 'delete'
                buttons.append(kg.Button.text(label='Удалить роль \"'+role+'\"', payload=payload, color='negative'))
            else:
                payload['do'] = 'add'
                buttons.append(kg.Button.text(label='Добавить роль \"'+role+'\"', payload=payload, color='positive'))
    buttons.append(kg.Button.text(label='На главную', payload=payloads.payloads['get_main_keyboard']))
    generator = kg.KeyBoard()
    generator.load(buttons)
    kb = generator.get()
    return kb


def get_subjects_keyboard(roles_now):
    pre_buttons = {
        names.roles[0]: kg.Button.text(label='Системка', payload=payloads.payloads['get_progers_types']),
        names.roles[1]: kg.Button.text(label='Элтех', payload=payloads.payloads['get_eltech_types']),
        names.roles[2]: kg.Button.text(label='Дискретка', payload=payloads.payloads['get_math_types']),
        names.roles[3]: kg.Button.text(label='Физика', payload=payloads.payloads['get_physics_types']),
    }
    buttons = []
    if names.roles[4] in roles_now:
        for role in names.roles[:-1]:
            buttons.append(pre_buttons[role])
    else:
        for role in roles_now:
            buttons.append(pre_buttons[role])
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
        payload['number'] = free_numbers[i]
        payload['type_task'] = type
        buttons[j].append(kg.Button.text(str(free_numbers[i]), payload=payload))
    buttons.append([])
    buttons[j+1].append(kg.Button.text(label='На главную', payload=payloads.payloads['get_main_keyboard']))
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
    generator = kg.KeyBoard(inline=True, one_line=True)
    generator.load(buttons)
    kb = generator.get()
    return kb








