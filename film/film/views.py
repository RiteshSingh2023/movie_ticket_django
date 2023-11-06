from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import adde,reserves,Solve
 

# Create your views here.

def index(request):
    
    return render(request,"index.html")

def adminregister(request):
    if request.method=='POST':
        name=request.POST.get("adminname")
        email=request.POST.get("adminemail")
        password=request.POST.get("adminpass1")
        confirmpassword=request.POST.get("adminpass2")

        if(password!=confirmpassword):
            messages.warning(request,"incorrect password")
            return redirect('/adminregister')
        try:
            if User.objects.get(adminname=name):
                messages.info(request,"username is taken")
                return redirect('/adminregister')
        except:
            pass
        
        try:
            if User.objects.get(adminemail=email):
                messages.info(request,"email is taken")
                return redirect('/adminregister')
        except:
            pass

        myuser=User.objects.create_user(name,email,password)   
        myuser.save()
        messages.success(request,"signup successful please login")
        return redirect('/adminlogin')
    return render(request,"adminregister.html")


def adminlogin(request):
    if request.method=='POST':
        name=request.POST.get('adminname1')
        pass1=request.POST.get('adminpass')
        myuser=authenticate(username=name,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"login Success")
            return redirect('/admi')
        else:
            messages.error(request,"wrong credential")
            return redirect('/adminlogin')
    return render(request,"adminlogin.html")

def admi(request):
    return render(request,"admi.html")

def addmovies(request):
    if request.method == "POST":
        mname = request.POST.get("moviename")
        mabout= request.POST.get("about1")
        mstory = request.POST.get("story")
        mcharge = request.POST.get("charge")
        mtime = request.POST.get("time1")
        query = adde.objects.create(mname=mname, mabout=mabout, mstory=mstory, mcharge=mcharge, mtime=mtime)
        query.save()
        messages.success(request," movie added")
        return redirect('/admi')
    return render(request,"addmovie.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"logout successful")    
    return redirect('/')

def userlogi(request):
    if request.method=='POST':
        name=request.POST.get('username1')
        pass1=request.POST.get('userpass')
        myuser=authenticate(username=name,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"login Success")
            return redirect('/customer')
        else:
            messages.error(request,"wrong credential")
            return redirect('/userlogi')
    return render(request,"userlogi.html")


def usersignup(request):
    if request.method=='POST':
        name1=request.POST.get("username")
        email1=request.POST.get("useremail")
        password1=request.POST.get("userpass1")
        confirmpassword1=request.POST.get("userpass2")

        if(password1!=confirmpassword1):
            messages.warning(request,"incorrect password")
            return redirect('/usersignup')
        try:
            if User.objects.get(username=name1):
                messages.info(request,"username is taken")
                return redirect('/usersignup')
        except:
            pass
        
        try:
            if User.objects.get(useremail=email1):
                messages.info(request,"email is taken")
                return redirect('/usersignup')
        except:
            pass

        myuser=User.objects.create_user(name1,email1,password1)   
        myuser.save()
        messages.success(request,"signup successful please login")
        return redirect('/userlogi')
    return render(request,"usersignup.html")

def customer(request):
    return render(request,"customer.html")

def ticket(request):
    data=adde.objects.all()
    context = {"data":data}
    return render(request,"ticket.html",context)

def book(request,id):
    if request.method=="POST":
        name=request.POST['movietitle']
        time1=request.POST['showtime']
        price=request.POST['price']
        name1 = request.POST.get("name1")
        email1 = request.POST.get("email1")
        theater = request.POST.get("theater")
        showdate = request.POST.get("showdate")
        quantity = request.POST.get("quantity")
        query = reserves.objects.create(name=name, name1=name1, email1=email1, time1=time1, price=price, theater=theater, showdate=showdate, quantity=quantity)
        query.save()
        messages.success(request," SHOW BOOKED")
        return redirect('/customer')
    book=adde.objects.get(id=id)
    return render(request,"book.html", {'d': book})


def total(request):
    cat=reserves.objects.all()
    context = {"cat":cat}
    return render(request,"total.html",context)

def about(request):
    
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        mess = request.POST.get("message")
        query = Solve.objects.create(name=name, email=email, subject=subject, mess=mess)
        query.save()
        messages.success(request," Thanks to contact us")
        return redirect('/customer')
    return render(request,"contact.html")
