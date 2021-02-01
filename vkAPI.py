import vk, random
#group session
session = vk.Session()
api = vk.API(session, v='5.120')
#user session
session1 = vk.AuthSession(7721679, 'логин', "пароль", 'docs')
api1 = vk.API(session1, v='5.120')


def send_message(user_id, token, message, attachment="", keyboard=""):
    api.messages.send(access_token=token, keyboard=keyboard, user_id=str(user_id), message=message, attachment=attachment,
                      random_id=random.getrandbits(64))


def delete_dock(owner_id, doc_id):
    api1.docs.delete(owner_id=owner_id, doc_id=doc_id)


def add_tag_dock(owner_id, doc_id, title, tags):
    api1.docs.edit(owner_id=owner_id, doc_id=doc_id, title=title, tags=tags)


def get_user_info(user_id, token):
    response = api.users.get(access_token=token, user_ids=user_id)
    if len(response)>0:
        return response[0]["first_name"], response[0]["last_name"]
    else:
        return 'undefined', 'undefined'

