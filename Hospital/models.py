from django.db import models
from django.contrib.auth.models import User
class Hospitals(models.Model):
    Hospitalid = models.ForeignKey(User,on_delete=models.CASCADE)
    HospitalName = models.CharField(max_length=15)
    Address = models.CharField(max_length = 60)
    Lattitude = models.CharField(max_length=15)
    Longitude = models.CharField(max_length=15)
    logo = models.CharField(max_length= 300)
    def __str__(self):
        return self.HospitalName 
