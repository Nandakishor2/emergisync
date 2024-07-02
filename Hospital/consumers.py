from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync,sync_to_async

class HospitalLocation(WebsocketConsumer):
    #This Sokt Is created to send coordinates of the driver to hospital
    def connect(self):
        self.roomname =  self.scope['url_route']['kwargs']['hospid']
        self.groupname = self.roomname
        print(self.groupname)
        async_to_sync(self.channel_layer.group_add)(
            self.groupname,self.channel_name
        )
        self.accept()
        print("Connection Esablished")
    def receive(self, text_data):
        print("AT Hospital",text_data.get("value"))
        self.send(json.dumps({"Data":text_data.get("value")}))
