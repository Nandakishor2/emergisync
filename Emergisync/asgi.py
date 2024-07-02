"""
ASGI config for Emergisync project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from Base.consumers import *
from Driver.consumers import *
from Hospital.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Emergisync.settings')


wspatterns  = [
    path("ws/ledcontrols/<ipaddress>",Ledcontroller.as_asgi()),
    path("ws/location/<locdetails>",Location.as_asgi()),
    path("ws/driver/<token>",Driver_data.as_asgi()),
    path("ws/base/pickedup",Datatransfer.as_asgi()),
    path("ws/directiondata",Testdata.as_asgi()),
    path("ws/hospital/<hospid>",HospitalLocation.as_asgi()),
    path("ws/base/leds",LEDS.as_asgi()),
]
application =ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket" : AuthMiddlewareStack(URLRouter(
        wspatterns
    ))
})
