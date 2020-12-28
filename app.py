from flask import Flask, request
import json, vk, VKsettings, random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/helperBot/api/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    elif data['type'] == 'confirmation':
        return VKsettings.confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=VKsettings.api_ver)
        user_id = data['object']['message']['from_id']
        api.messages.send(access_token=VKsettings.token, user_id=str(user_id), message='Hi, I\'m new bot!',
                          random_id=random.getrandbits(64))
        return 'ok'




if __name__ == '__main__':
    app.run()
