from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from random import random

# Create your views here.
def sd(request):
    return render(request, "home/sd.html")
def fbhome(request):
    return render(request, "home/fbhome.html")
def fblogin(request):
    return render(request, "home/fblogin.html")
def about(request):
    return render(request, "home/about.html")
def home(request):
    posts = Post.objects.order_by('-timeStamp')
    paginator= Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, "home/home.html",{'key':page_obj})
def addpost(request):
    if request.method=="POST":
        # print(category)
        title=request.POST['title']
        author=request.POST['author']
        content =request.POST['content']
        slug =request.POST['slug']
        pic=request.FILES['pic']
        filename = str(random())+pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename, pic)
        category_id=request.POST.get('category')
        category =blogcategory.objects.get(id=category_id)
        post=Post(category=category, title=title, author=author, picture=filename,slug=slug, content=content)
        post.save()
        # return render(request, "home/addpost.html")
        return render(request, "home/addpost.html",{'message': 'Your Blog has been Added'})
    bcat = blogcategory.objects.all()
    return render(request, "home/addpost.html",{'key':bcat})
def blogposts(request):
    posts = Post.objects.order_by('-timeStamp')
    # no_posts = Post.objects.all().count()
    paginator= Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, "home/blogposts.html",{'key':page_obj})
def blogs(request):
    posts = Post.objects.order_by('-timeStamp')
    # posts = Post.objects.all()
    paginator= Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    # print(page_obj)
    bcat = blogcategory.objects.all()
    return render(request, "home/blogs.html",{'key':page_obj, 'cat':bcat})
    # return render(request, "home/blogs.html" ,{'key':posts})
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
        pic=request.FILES['pic']
        filename = str(random())+pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename, pic)
        category_id=request.POST.get('category')
        category =blogcategory.objects.get(id=category_id)
        Post.objects.filter(id=id).update(category=category, title=title, author=author, slug=slug, content=content , picture=filename)
        return redirect('/blogposts')
    postinfo=Post.objects.get(id=id)
    bcat = blogcategory.objects.all() 
    return render(request, 'home/editpost.html',{'postinfo':postinfo,'key':bcat})
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content =request.POST['content']
        contact=Contact(name=name, email=email, content=content)
        contact.save()
        messages.success(request, "Your message has been successfully sent!")
        return render(request, "home/contact.html")
        # return render(request, "home/contact.html",{'message': 'Your Message has been sent!'})
    return render(request, "home/contact.html")
def inbox(request):
    mesgs = Contact.objects.order_by('-timeStamp')
    paginator= Paginator(mesgs, 5)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, "home/inbox.html",{'key':page_obj})
    # return render(request, "home/inbox.html",{'key':mesgs})
def deletemsg(request, id):
        delmsg = Contact.objects.get(id=id)
        delmsg.delete()
        return redirect('/inbox')
def handleSignup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username =request.POST['username']
        phone =request.POST['phone']
        email =request.POST['email']
        password =request.POST['password']
        cpassword =request.POST['c_password']

        # Create the user
        myuser = User.objects.create_user(username=username, email=email, password=password, first_name=fname)
        myuser.last_name=lname
        myuser.save()

        info=userinfo.objects.create(user=myuser,phone=phone)
        messages.success(request, "Your Account has been successfully created")
        return render(request, 'home/home.html')


    else:
        return HttpResponse('404 - Not Found')

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'home/profile.html')
    else:
        return HttpResponse("Login Required !!!")
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            posts = Post.objects.order_by('-timeStamp')
            return render(request, "home/dashboard.html",{'key':posts})
        else:
            return HttpResponse("Error 404 NOT Found!!!")
    return HttpResponse("Login Required !!!")
def editprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            email =request.POST['email']
            phone=request.POST['phone']
            location=request.POST['location']
            about=request.POST['about']
            if len(fname)<2 or len(lname)<1 or len(email)<5 or len(phone)<5:
                messages.error(request, "Please fill the form correctly")
            else:
                User.objects.filter(id=request.user.id).update(first_name=fname,last_name=lname,email=email)
                userinfo.objects.filter(user__id=request.user.id).update(about=about,location=location,phone=phone)
                messages.success(request, "Your Profile has been successfully updated!!")
            return render(request, 'home/editprofile.html')
        return render(request, 'home/editprofile.html')
    else:
        return HttpResponse("Login Required !!!")
def settings(request):
    return render(request, "home/settings.html")

# def postComment(request):
#     if request.method == "POST":
#         comment=request.POST.get('comment')
#         user=request.user
#         postSno =request.POST.get('postSno')
#         post= Post.objects.get(sno=postSno)
#         comment=BlogComment(comment= comment, user=user, post=post)
#         comment.save()
#         messages.success(request, "Your comment has been posted successfully")     
#     return redirect("/blog/{post.slug}")