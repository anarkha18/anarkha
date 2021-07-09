from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def fbhome(request):
    return render(request, "home/fbhome.html")
def fblogin(request):
    return render(request, "home/fblogin.html")
def home(request):
    return render(request, "home/home.html")
# def contact(request):
#     return render(request, "home/contact.html")
def addpost(request):
    if request.method=="POST":
        title=request.POST['title']
        author=request.POST['author']
        content =request.POST['content']
        slug =request.POST['slug']
        post=Post(title=title, author=author, slug=slug, content=content)
        post.save()
        return render(request, "home/addpost.html",{'message': 'Your Blog has been Added'})
    return render(request, "home/addpost.html")
def blogposts(request):
    posts = Post.objects.all()
    return render(request, "home/blogposts.html",{'key':posts})
def blogs(request):
    posts = Post.objects.all()
    return render(request, "home/blogs.html" ,{'key':posts})
def deletepost(request, id):
    # if (request.method == 'POST'):
        delpost = Post.objects.get(id=id)
        delpost.delete()
        return redirect('/blogposts')
def blogpage(request, slug):
    page = Post.objects.filter(slug=slug).first()
    context= {'page':page}
    return render(request, "home/blogpage.html", context)
    # return render(request, "bloghome.html", {'key':page})
def updatepost(request, id):
    if request.method=="POST":
        title=request.POST['title']
        author=request.POST['author']
        content =request.POST['content']
        slug =request.POST['slug']
        Post.objects.filter(id=id).update(title=title, author=author, slug=slug, content=content)
        return redirect('/blogposts')
    postinfo=Post.objects.get(id=id) 
    return render(request, 'home/editpost.html',{'postinfo':postinfo})
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        return render(request, "home/contact.html",{'message': 'Your Message has been sent!'})
    return render(request, "home/contact.html")
def messages(request):
    mesgs = Contact.objects.all()
    return render(request, "home/messages.html",{'key':mesgs})
def deletemsg(request, id):
        delmsg = Contact.objects.get(id=id)
        delmsg.delete()
        return redirect('/messages')
