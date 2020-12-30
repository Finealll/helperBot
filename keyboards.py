import keyboard_generator as kg
import payloads, roles

# Основная клавиатура
def get_main_keyboard():
    buttons = []
    buttons.append(kg.Button.text(label='Доступные задания', payload=payloads.payloads['get_tasks_list']))
    buttons.append(kg.Button.text(label='Мои задания', payload=payloads.payloads['get_now_tasks_list']))
    buttons.append(kg.Button.text(label='Роли', payload=payloads.payloads['get_roles_list']))
    generator = kg.KeyBoard(False, False, False)
    generator.load(buttons)
    kb = generator.get()
    return kb

#Inline клава для сообщения с ролями
def get_roles_keyboard(roles_now):
    buttons = []
    if roles.roles[4] in roles_now:
        payload = dict(payloads.payloads['change_role'])
        payload['role'] = roles.roles[4]
        payload['do'] = 'delete'
        buttons.append(kg.Button.text(label='Удалить роль \"'+roles.roles[4]+'\"', payload=payload, color='negative'))
    else:
        for role in roles.roles:
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
        roles.roles[0]: kg.Button.text(label='Системка', payload=payloads.payloads['get_progers_types']),
        roles.roles[1]: kg.Button.text(label='Элтех', payload=payloads.payloads['get_eltech_types']),
        roles.roles[2]: kg.Button.text(label='Дискретка', payload=payloads.payloads['get_math_types']),
        roles.roles[3]: kg.Button.text(label='Физика', payload=payloads.payloads['get_physics_types']),
    }
    buttons = []
    if roles.roles[4] in roles_now:
        for role in roles.roles[:-1]:
            buttons.append(pre_buttons[role])
    else:
        for role in roles_now:
            buttons.append(pre_buttons[role])
    buttons.append(kg.Button.text(label='На главную', payload=payloads.payloads['get_main_keyboard']))
    generator = kg.KeyBoard()
    generator.load(buttons)
    kb = generator.get()
    return kb
