from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def assignment1(request):
    return render(request, "assignment1.html")
def assignment2(request):
    return render(request, "assignment2.html")
def assignment3(request):
    return render(request, "assignment3.html")
def assignment4(request):
    return render(request, "assignment4.html")
def assignment5(request):
    return render(request, "assignment5.html")
def assignment6(request):
    return render(request, "assignment6.html")
def assignment7(request):
    return render(request, "assignment7.html")
def assignment8(request):
    return render(request, "assignment8.html")
def assignment9(request):
    return render(request, "assignment9.html")
def assignment10(request):
    return render(request, "assignment10.html")
def assignment11(request):
    return render(request, "assignment11.html")
def assignment12(request):
    return render(request, "assignment12.html")
def assignment13(request):
    return render(request, "assignment13.html")
def assignment14(request):
    return render(request, "assignment14.html")
def assignment15(request):
    return render(request, "assignment15.html")
def assignment16(request):
    return render(request, "assignment16.html")
def bootstrap1(request):
    return render(request, "bootstrap1.html")
def bootstrap2(request):
    return render(request, "bootstrap2.html")
def fbhome(request):
    return render(request, "fbhome.html")
def fblogin(request):
    return render(request, "fblogin.html")
def home(request):
    return render(request, "home.html")
def contact(request):
    return render(request, "contact.html")
def sum(request):
    return render(request, "sum.html")
def fsum(request):
    fnum = request.GET["firstnumber"]
    snum = request.GET["secondnumber"]
    sum= int(fnum) + int(snum)
    return render(request, "sum.html",{'sum': sum})
    # return HttpResponse(sum)
def calcu(request):
    if (request.method == 'POST'):
        fnum = request.POST["firstnumber"]
        snum = request.POST["secondnumber"]
        sum= int(fnum) + int(snum)
        return render(request, "calcu.html",{'sum': sum})
    return render(request, "calcu.html")
def myform(request):
    if (request.method == 'POST'):
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        regval = registration(firstname=fname,lastname=lname,emailid=email,password=password)
        regval.save()
        return render(request, "validation.html",{'message': 'success'})
    return render(request, "validation.html")
def mytable(request):
    details = registration.objects.all()
    return render(request, "table.html",{'key':details})
   # add data
def mesg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        msg=Mesg(name=name, email=email, phone=phone, content=content)
        msg.save()
        return render(request, "datas.html",{'message': 'Your Message has been sent!'})
    return render(request, "datas.html")
def mymessages(request):
    messages = Mesg.objects.all()
    return render(request, "datastable.html",{'key':messages})
    # update data
def updatedata(request, id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        Mesg.objects.filter(id=id).update(name=name, email=email, phone=phone, content=content)
        return redirect('/mymesgs')
    details=Mesg.objects.get(id=id) 
    return render(request, 'updatedata.html',{'details':details})
    # delete data
def deletedata(request, id):
    # if (request.method == 'POST'):
    deldata = Mesg.objects.get(id=id)
    deldata.delete()
    return redirect('/mymesgs')
def addpost(request):
    if request.method=="POST":
        title=request.POST['title']
        author=request.POST['author']
        content =request.POST['content']
        slug =request.POST['slug']
        post=Post(title=title, author=author, slug=slug, content=content)
        post.save()
        return render(request, "addpost.html",{'message': 'Your Blog has been Added'})
    return render(request, "addpost.html")
def blogposts(request):
    posts = Post.objects.all()
    ordering=['-timeStamp']
    return render(request, "blogposts.html",{'key':posts})
def blogs(request):
    posts = Post.objects.all()
    return render(request, "blogs.html" ,{'key':posts})
def deletepost(request, id):
    # if (request.method == 'POST'):
        delpost = Post.objects.get(id=id)
        delpost.delete()
        return redirect('/blogposts')
def blogpage(request, slug):
    page = Post.objects.filter(slug=slug).first()
    context= {'page':page}
    return render(request, "blogpage.html", context)
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
    return render(request, 'editpost.html',{'postinfo':postinfo})
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        return render(request, "contact.html",{'message': 'Your Message has been sent!'})
    return render(request, "contact.html")
def messages(request):
    mesgs = Contact.objects.all()
    return render(request, "messages.html",{'key':mesgs})
def deletemsg(request, id):
        delmsg = Contact.objects.get(id=id)
        delmsg.delete()
        return redirect('/messages')





