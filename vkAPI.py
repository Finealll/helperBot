import vk, random

session = vk.Session()
api = vk.API(session, v='5.120')


def send_message(user_id, token, message, attachment="", keyboard=""):
    api.messages.send(access_token=token, keyboard=keyboard, user_id=str(user_id), message=message, attachment=attachment,
                      random_id=random.getrandbits(64))


def get_user_info(user_id, token):
    response = api.users.get(access_token=token, user_ids=user_id)
    return response[0]["first_name"], response[0]["last_name"]


def test_uwed(token):
    api.messages.send(access_token=token, peer_id=2000000084, message='Hi',attachment='doc209640539_581822701',
                      random_id=random.getrandbits(64))