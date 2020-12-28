import vk, random

session = vk.Session()
api = vk.API(session, v='5.120')


def send_message(user_id, token, message, attachment="", keyboard=""):
    api.messages.send(access_token=token, keyboard=keyboard, user_id=str(user_id), message=message, attachment=attachment,
                      random_id=random.getrandbits(64))
