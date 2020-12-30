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
    for role in roles.roles:
        payload = payloads.payloads['change_role']
        payload['role'] = role[0]
        if role[0] in roles_now:
            payload['do'] = 'delete'
            buttons.append(kg.Button.text(label='-'+role[0], payload=payload))
        else:
            payload['do'] = 'add'
            buttons.append(kg.Button.text(label='+'+role[0], payload=payload))
    generator = kg.KeyBoard(inline=True)
    generator.load(buttons)
    kb = generator.get()
    return kb

