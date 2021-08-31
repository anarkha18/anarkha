from django.db import models

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
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    category=models.ForeignKey(blogcategory,on_delete=models.CASCADE, default="1" )

    def __str__(self):
        return self.title + " by " + self.author
