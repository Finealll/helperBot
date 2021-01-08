import vk, random

session = vk.Session()
api = vk.API(session, v='5.120')


def send_message(user_id, token, message, attachment="", keyboard=""):
    api.messages.send(access_token=token, keyboard=keyboard, user_id=str(user_id), message=message, attachment=attachment,
                      random_id=random.getrandbits(64))


def delete_dock(token, owner_id, doc_id):
    api.docs.delete(access_token=token, owner_id=owner_id, doc_id=doc_id)


def get_user_info(user_id, token):
    response = api.users.get(access_token=token, user_ids=user_id)
    if len(response)>0:
        return response[0]["first_name"], response[0]["last_name"]
    else:
        return 'undefined', 'undefined'

