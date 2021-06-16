from django.db import models

# Create your models here.

class UserReg(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    emailid = models.CharField(max_length=100)
    dob = models.DateField()
class UserLogin(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    userid = models.ForeignKey(UserReg,on_delete=models.CASCADE)

# class User(models.Model):
#     firstname = models.CharField(max_length=80)
#     lastname = models.CharField(max_length=80)
#     emailid = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)
#     dob = models.DateField()

# class Fbuser(models.Model):
#     firstname = models.CharField(max_length=80)
#     lastname = models.CharField(max_length=80)
#     email = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     password = models.CharField(max_length=50)
#     dob=models.DateField()

# class Contactus(models.Model):
#     Name = models.CharField(max_length=80)
#     email = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     content = models.TextField()

