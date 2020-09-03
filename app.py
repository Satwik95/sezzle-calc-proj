from flask import Flask, render_template, request, url_for, redirect
from flask_socketio import SocketIO, join_room
import requests
from collections import deque

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('send_exp')
def handle_send_exp(data):
    exp = data['exp']
    app.logger.info(exp)
    PARAMS = {'expr': exp}
    URL = "http://api.mathjs.org/v4/"
    r = requests.get(url=URL, params=PARAMS)
    res = {"exp": exp, "res": r.json()}
    socketio.emit("receive_res_exp", res)

if __name__ == '__main__':
    #socketio.run(app, debug=True)
    app.run()