from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def sd(request):
    return render(request, "home/sd.html")
def fbhome(request):
    return render(request, "home/fbhome.html")
def fblogin(request):
    return render(request, "home/fblogin.html")
def home(request):
    return render(request, "home/home.html")
def addpost(request):
    if request.method=="POST":
        # print(category)
        title=request.POST['title']
        author=request.POST['author']
        content =request.POST['content']
        slug =request.POST['slug']
        category_id=request.POST.get('category')
        category =blogcategory.objects.get(id=category_id)
        # print(category)
        post=Post(category=category, title=title, author=author, slug=slug, content=content)
        post.save()
        # return render(request, "home/addpost.html")
        return render(request, "home/addpost.html",{'message': 'Your Blog has been Added'})
    bcat = blogcategory.objects.all()
    return render(request, "home/addpost.html",{'key':bcat})
def blogposts(request):
    posts = Post.objects.order_by('-timeStamp')
    # posts = Post.objects.all()
    return render(request, "home/blogposts.html",{'key':posts})
def blogs(request):
    posts = Post.objects.order_by('-timeStamp')
    # posts = Post.objects.all()
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
        category_id=request.POST.get('category')
        category =blogcategory.objects.get(id=category_id)
        Post.objects.filter(id=id).update(category=category, title=title, author=author, slug=slug, content=content)
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
    return render(request, "home/inbox.html",{'key':mesgs})
def deletemsg(request, id):
        delmsg = Contact.objects.get(id=id)
        delmsg.delete()
        return redirect('/inbox')
def handleSignup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        cpassword =request.POST['c_password']

        # Create the user
        myuser = User.objects.create_user(username=username, email=email, password=password, first_name=fname)
        myuser.last_name=lname
        myuser.save()
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
    return render(request, 'home/profile.html')
def dashboard(request):
    return render(request, "home/dashboard.html")
def editprofile(request):
    return render(request, "home/editprofile.html")
def settings(request):
    return render(request, "home/settings.html")