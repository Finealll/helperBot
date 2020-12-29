import vkAPI, keyboard_generator
import json

def message_handler(data, token):
    user_id = data['object']['message']['from_id']
    names = vkAPI.get_user_info(user_id, token)
    vkAPI.send_message(user_id=user_id, token=token, message=str(names[0]+" "+names[1]), keyboard=keyboard_generator.get_main_keyboard())


def event_handler(data, token):
    return 1


