from django.db import models

class driverdata(models.Model):
    Userip = models.CharField(max_length=20,default="")
    isactive = models.BooleanField(default=False)
    def __str__(self):
        return  self.Userip
