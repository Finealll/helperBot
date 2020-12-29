import vkAPI, keyboard_generator
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    vkAPI.send_message(user_id=user_id, token=token, message="Просто ответ!", keyboard=keyboard_generator.get_main_keyboard())


def event_handler(data, token):
    if 'type' not in data['payload'].keys():
        return 0
    payload = json.loads(data['payload'])
    if payload['type'] == 'open_keyboard':
        if payload['name'] == 'main':
            keyboard = keyboard_generator.get_main_keyboard()
            vkAPI.send_message(user_id=data['user_id'], token=token, message='Выбери действие:', keyboard=keyboard)
        elif payload['name'] == 'my_roles':
            keyboard = keyboard_generator.get_roles_keyboard()
            vkAPI.send_message(user_id=data['user_id'],token=token, message='Выбери предмет', keyboard=keyboard)
    return 1
