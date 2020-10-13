from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO()
socketio.init_app(app)


@app.route('/')
def hello_word():
    return render_template('index.html')


@app.route('/chat')
def home():
    return render_template('chatroom.html')


@socketio.on('new user')
def new_user(nickname):
    print(nickname)
    emit('new user',
         {
             'nickname': nickname
         },
         broadcast=True)


@socketio.on('new message')
def new_message(message):
    print(message)
    emit('new message',
         {
             'message': message['message'],
             'nickname': message['nickname'],
         },
         broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
