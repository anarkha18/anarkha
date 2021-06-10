from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    emailid = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    dob = models.DateField()

class Fbuser(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    dob=models.DateField()

class Contactus(models.Model):
    Name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    content = models.TextField()

