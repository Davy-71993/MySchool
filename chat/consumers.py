# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from .models import Massage

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        sm = Massage(text=message)
        sm.save()

        self.send(text_data=json.dumps({
            'message': message
        }))