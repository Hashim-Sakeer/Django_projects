from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['last name']
        email=request.POST['email address']
        passw=request.POST['password']
        confirmpassw=request.POST['confirm password']
        if passw==confirmpassw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already registered")
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=passw)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"password is not matching")
            print("password not match")
            return redirect('registration')
        return redirect('/')
    return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
