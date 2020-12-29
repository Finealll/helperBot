from flask import Flask, request
import json, vk, random
import VKsettings, vkAPI, keyboard_generator, message_handle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/helperBot/api/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    print(json.dumps(data))
    if 'type' not in data.keys():
        return 'not vk'
    elif data['type'] == 'confirmation':
        return VKsettings.confirmation_token
    elif data['type'] == 'message_new':
        message_handle.message_handler(data, VKsettings.token)
        return 'ok'
    elif data['type'] == 'message_event':
        message_handle.event_handler(data, VKsettings.token)
        return 'ok'
    return 'ok'


if __name__ == '__main__':
    app.run()
