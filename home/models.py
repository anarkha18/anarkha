from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=100)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email



class blogcategory(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Post(models.Model):
    category=models.ForeignKey(blogcategory,on_delete=models.CASCADE, default="1" )
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    picture= models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title + " by " + self.author


class userinfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.BigIntegerFeild()
    about=models.TextField(max_length=200, blank=True)
    location=models.CharField(max_length=200, blank=True)

    
    def __str__(self):
        return str(self.user)
    


