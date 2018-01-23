from flask import Blueprint
import gevent
import redis
import json


ws = Blueprint('ws', __name__, url_prefix='/ws')

redis = redis.from_url('redis://127.0.0.1:6379')


class Chatroom(object):

    def __init__(self):
        self.clients = []
        self.notice = None
        self.pubsub = redis.pubsub()
        self.pubsub.subscribe('chat')

    def register(self, client):
        self.clients.append(client)
        self.notice = json.dumps({'username': 'New user come in,', 'text': 'people count: {}'.format(len(self.clients))})

    def send(self, client, data):
        try:
            client.send(data.decode('utf-8'))
        except:
            self.clients.remove(client)

    def run(self):
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                data = message.get('data')
                for client in self.clients:
                    gevent.spawn(self.send, client, data)

    def start(self):
        gevent.spawn(self.run)


chat = Chatroom()
chat.start()


@ws.route('/send')
def inbox(ws):
    while not ws.closed:
        if chat.notice:
            message = chat.notice
            redis.publish('chat', message)
            chat.notice = None
        message = ws.receive()
        if message:
            redis.publish('chat', message)


@ws.route('/recv')
def outbox(ws):
    chat.register(ws)
    while not ws.closed:
        gevent.sleep(0.1)
