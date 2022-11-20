from django.db import models

class Datos (models.Model):
    dato1 = models.FloatField()
    c1 = models.CharField(max_length=3,blank=True, null=True)
    dato2 = models.FloatField()
    dato3 = models.FloatField()
# Create your models here.

    def __str__(self):
        return str(self.x1)+' , ' + str(self.c1) + ' , ' + str(self.x2) +' , ' + str(self.x3)