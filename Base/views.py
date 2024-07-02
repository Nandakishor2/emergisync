from django.http import JsonResponse
from django.shortcuts import render
from Base.models import *
def index(request):
    
    return render(request,'index.html')
def led(request):
    return render(request,"play.html")
def leddata(request):
    data = Leds.objects.filter(ipaddress = "192.168.43.246")
    for row in data:
        lights = [row.led1, row.led2, row.led3, row.led4, row.led5, row.led6, row.led7, row.led8, row.led9, row.led10, row.led11, row.led12, row.led13, row.led14, row.led15, row.led16, row.led17, row.led18, row.led19, row.led20, row.led21, row.led22, row.led23, row.led24, row.led25, row.led26, row.led27, row.led28, row.led29, row.led30, row.led31, row.led32,row.led33,row.led34,row.led35,row.led36,row.led37,row.led38,row.led39,row.led40,row.led41,row.led42,row.led43,row.led44,row.led45,row.led46,row.led47,row.led48]
    print(len(lights))
    return JsonResponse ({"Data":lights})
def ambulance(request):
    listdata = []
    data = Dataforlist.objects.filter(Completed = False)
    for row in data:
        listdata.append({
            "Username":row.Username,
            "Ambulanceid":row.Ambulanceid,
            "Hospital":row.Hospital,
            "Lattitude":row.Lattitude,
            "Longitude" :row.Longitude,
            "HospLattitude":row.HospLattitude,
            "HospLongitude":row.HospLongitude,
            "Distance":row.distance
        })
    return render(request,"ambulance.html",{"Data":listdata})



# while True:
#   response = urequests.post(url, headers={'Content-Type': 'application/json'})
#   if response.status_code == 200:
#     lights = ujson.loads(response.text)
#     leds = lights["Data"]
#     print(type(pattern1))
#     pattern1 = leds[0:8]
#     pattern2 = leds[9:16]
#     pattern3 = leds[17:24]
#     pattern4 = leds[25:32]
#     pattern5 = leds[33:40]
#     pattern6 = leds[41:48]
#     shift_out(data_pin7, clock_pin, latch_pin7, pattern1)
#     time.sleep(1)  # Delay for 1 second
#     pattern ^= 0b11111111

#     #shift_out(data_pin7, clock_pin, latch_pin7, pattern1)
#     #pattern1  ^= pattern1
#   else:
#     print("HTTP request failed with status code:", response.status_code)
#     response.close()
  