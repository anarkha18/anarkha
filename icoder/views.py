from django.shortcuts import render, HttpResponse, redirect
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage

# Create your views here.
def assignment1(request):
    return render(request, "icoder/assignment1.html")
def assignment2(request):
    return render(request, "icoder/assignment2.html")
def assignment3(request):
    return render(request, "icoder/assignment3.html")
def assignment4(request):
    return render(request, "icoder/assignment4.html")
def assignment5(request):
    return render(request, "icoder/assignment5.html")
def assignment6(request):
    return render(request, "icoder/assignment6.html")
def assignment7(request):
    return render(request, "icoder/assignment7.html")
def assignment8(request):
    return render(request, "icoder/assignment8.html")
def assignment9(request):
    return render(request, "icoder/assignment9.html")
def assignment10(request):
    return render(request, "icoder/assignment10.html")
def assignment11(request):
    return render(request, "icoder/assignment11.html")
def assignment12(request):
    return render(request, "icoder/assignment12.html")
def assignment13(request):
    return render(request, "icoder/assignment13.html")
def assignment14(request):
    return render(request, "icoder/assignment14.html")
def assignment15(request):
    return render(request, "icoder/assignment15.html")
def assignment16(request):
    return render(request, "icoder/assignment16.html")
def bootstrap1(request):
    return render(request, "icoder/bootstrap1.html")
def bootstrap2(request):
    return render(request, "icoder/bootstrap2.html")
def sum(request):
    return render(request, "icoder/sum.html")
def fsum(request):
    fnum = request.GET["firstnumber"]
    snum = request.GET["secondnumber"]
    sum= int(fnum) + int(snum)
    return render(request, "icoder/sum.html",{'sum': sum})
def calcu(request):
    if (request.method == 'POST'):
        fnum = request.POST["firstnumber"]
        snum = request.POST["secondnumber"]
        sum= int(fnum) + int(snum)
        return render(request, "icoder/calcu.html",{'sum': sum})
    return render(request, "icoder/calcu.html")
def mesg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        msg=Mesg(name=name, email=email, phone=phone, content=content)
        msg.save()
        return render(request, "icoder/datas.html",{'message': 'Your Message has been sent!'})
    return render(request, "icoder/datas.html")
    # retrive data
def mymessages(request):
    messages = Mesg.objects.all()
    return render(request, "icoder/datastable.html",{'key':messages})
    # update data
def updatedata(request, id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        Mesg.objects.filter(id=id).update(name=name, email=email, phone=phone, content=content)
        return redirect('/icoder/mymesgs')
    details=Mesg.objects.get(id=id) 
    return render(request, 'icoder/updatedata.html',{'details':details})
    # delete data
def deletedata(request, id):
    # if (request.method == 'POST'):
    deldata = Mesg.objects.get(id=id)
    deldata.delete()
    return redirect('/icoder/mymesgs')
def reg(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pas =request.POST['pas'] 
        regis = Reg(fname=fname,lname=lname,email=email,pas=pas) 
        regis.save()
        return render(request, "icoder/reg.html",{'message': 'Your account is created'})
    return render(request, "icoder/reg.html")
def log(request):
    if request.method=="POST":
        lemail=request.POST['lemail']
        lpas =request.POST['lpas'] 
        try:
            svuser=Reg.objects.get(email=lemail)
            svpas=svuser.pas
            if(svuser.email==lemail and svpas==lpas):
                request.session['userlogged']=svuser.id
                # name=request.session['name']
                # return render(request,"datas.html", {'name':name})
                # return render(request,"datas.html")
                return redirect('/icoder/viewprofile')
                # return HttpResponse('vguy')
            else:
                return render(request,"icoder/log.html",{'message': 'login failed'})
        except User.DoesNotExist:
            return render(request,"icoder/log.html",{'message': 'login failed'})
    return render(request,'icoder/log.html')
def logout(request):
    del request.session['userlogged']
    return HttpResponse('You are logged out')

def viewprofile(request):
    try:
        current_session=request.session['userlogged']
        userlog=Reg.objects.get(id=current_session)
        return render(request, 'icoder/profile.html', {'current_session': userlog})
    except:
        return HttpResponse('login required')
def upload(request):
    if request.method=="POST":
        name=request.POST['name']
        place=request.POST['place']
        pic=request.FILES['pic']
        filename = str(random())+pic.name
        # print(filename)
        photo=FileSystemStorage()
        photo.save(filename, pic)
        details=Upload(name=name, place=place, pic=filename)
        details.save()
        return render(request, "icoder/new.html",{'message': 'Your pic has been uploaded'})
    return render(request, "icoder/new.html")
def img(request):
    tables = Upload.objects.all()
    return render(request, "icoder/img.html",{'key':tables})