from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('led',led,name= "led"),
    path("leddata",leddata ,name = "leddata"),
    path("ambulance",ambulance,name = "ambulance"),
    
]