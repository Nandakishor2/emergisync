from django.urls import path
from Hospital.views import *
urlpatterns = [
    path("home",hospital,name = "hospital"),
    path("hospital2",hospital2,name = "hospital2"),
    path("hospital3",hospital3,name = "hospital3"),
    path("hospital4",hospital4,name = "hospital4"),
    path("hospital5",hospital5,name = "hospital5")
]