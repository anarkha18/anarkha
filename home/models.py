from django.db import models

# Create your models here.

class registration(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    emailid = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

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

class Fbuser(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    dob=models.DateField()

class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    phone = models.IntegerField()
    email= models.CharField(max_length=100)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author