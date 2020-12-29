import vkAPI, keyboard_generator
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    vkAPI.send_message(user_id=user_id, token=token, message="Просто ответ!", keyboard=keyboard_generator.get_main_keyboard())


def event_handler(data, token):
    return 1
