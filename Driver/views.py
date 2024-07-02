from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token
import json
def handlelogin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token,created = Token.objects.get_or_create(user = user)
            print(token)
            return JsonResponse({"Token": str(token),"Allow":True})
        else:
            return JsonResponse({"Login": "Failed","Allow":False})
    else:
        return JsonResponse({"Message": "Only Post Allowed"})

def handlelogout(request):
    try:
        logout(request)
        return JsonResponse ({"Logout":"Successful"})
    except:
        return JsonResponse({"Login":" UnSuccessful"})
        
# def postdata(request):
#     if request.method == 'POST':
#         try:
#             # Parse JSON data from the request body
#             data = json.loads(request.body)
#             username = data.get('Username')
#             print(username)  # Output the username to console
#             return JsonResponse({"Message": "Received"})
#         except json.JSONDecodeError as e:
#             return JsonResponse({"Error": "Invalid JSON format"}, status=400)
#     else:
#         return JsonResponse({"Error": "Only POST requests are allowed"}, status=405)

    
