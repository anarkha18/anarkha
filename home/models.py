from django.db import models

# Create your models here.

class Mytable(models.Model):
    firstname = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    contact =models.IntegerField()


