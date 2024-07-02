from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync,sync_to_async
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from channels.layers import get_channel_layer
from Base.consumers import *
class Driver_data(WebsocketConsumer):
    def connect(self):
        self.roomname = self.scope['url_route']['kwargs']['token']
        userdata = Token.objects.get(key = self.roomname)
        self.user = userdata.user
        self.groupname = "room" + str(self.user)
        async_to_sync(self.channel_layer.group_add)(
            self.groupname,
            self.channel_name
        )
        self.accept()



       
        self.send(json.dumps({"Message":"Connection Established","User":str(self.user)}))
    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            "Data_to_Base",{
                'type' : 'printdata',
                'value' : text_data
            }
        )
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.groupname,
            self.channel_name
        )
