from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from Hospital.models import *
from Base.models import *
import json
def hospital(request):
    return render(request,"hospital.html")
def hospital2(request):
    if request.method == "POST":
        hospitalid = request.POST.get("hospitalid")
        password = request.POST.get("password")
        user = authenticate(username = hospitalid ,password = password)
        if user is not None:
            login(request,user)
            return redirect("hospital3")
        else:
            return redirect("hospital")
        
    return render(request,"hospital2.html")
def hospital3(request):
    print(request.user)
    hospitalid = User.objects.get(username = request.user)
    my = Hospitals.objects.filter(Hospitalid = hospitalid)
    return render(request,"hospital3.html", {"data":my})
def hospital4(request):
    listdata = []
    data = Dataforlist.objects.filter(Completed = False)
    for row1 in data:
        listdata.append({
            "Username":row1.Username,
            "Ambulanceid":row1.Ambulanceid,
            "Hospital":row1.Hospital,
            "Lattitude":row1.Lattitude,
            "Longitude" :row1.Longitude,
            "HospLattitude":row1.HospLattitude,
            "HospLongitude":row1.HospLongitude,
            "Distance":row1.distance
        })
    return render(request,"hospital4.html",{"Listdata":listdata})
def hospital5(request):
    hospitalid = User.objects.get(username = request.user)
    my = Hospitals.objects.filter(Hospitalid = hospitalid)
    location = []
    for row in my:
        location.append({
            "longitude":row.Longitude,
            "lattitude":row.Lattitude
        })
    
  
 
    return render (request,"hospital4.html",{"Location":location})