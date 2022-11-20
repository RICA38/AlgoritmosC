from django.db import models

class Datosknn (models.Model):
    data1 = models.FloatField()
    car1 = models.CharField(max_length=3,blank=True, null=True)
    
# Create your models here.

    def __str__(self):
        return str(self.data1)+' , ' + str(self.car1)


        