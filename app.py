from flask import Flask, request
import json, vk, random
import VKsettings, vkAPI

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
        user_id = data['object']['message']['from_id']
        vkAPI.send_message(user_id=user_id, token=VKsettings.token, message="Hi!")
        return 'ok'




if __name__ == '__main__':
    app.run()
