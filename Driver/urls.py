from django.urls import path
from Driver.views import *

urlpatterns = [
    path('login', handlelogin,name = "handlelogin"),
    path('logout',handlelogout,name = "handlelogout"),
    # path('postdata',postdata,name = "postdata")
]