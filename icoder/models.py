from django.db import models

# Create your models here.
# (for validation.html)
class Reg(models.Model):              
    # uname = models.CharField(max_length=80)
    fname = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    pas = models.CharField(max_length=50)

# (for crud exmple)
class Mesg(models.Model):
    name= models.CharField(max_length=255)
    phone = models.IntegerField()
    email= models.CharField(max_length=100)
    content= models.TextField()

class UserReg(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    emailid = models.CharField(max_length=100)
    dob = models.DateField()
class UserLogin(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    userid = models.ForeignKey(UserReg,on_delete=models.CASCADE)

class User(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    emailid = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    dob = models.DateField()
