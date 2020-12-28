from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/helperBot/api', methods=['POST'])
def processing():
    return '173a66e7'


if __name__ == '__main__':
    app.run()
