from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Course
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'home.html')
def user(request):
    return render(request,'user.html')


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email_address']
        passw=request.POST['password']
        confirmpassw=request.POST['confirm_password']
        if passw==confirmpassw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('/registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already registered")
                return redirect('/registration')
            else:
                user=User.objects.create_user(username=username,email=email,password=passw)
                user.save();
                print("user created")
                return redirect('/login')

        else:
            messages.info(request,"password is not matching")
            print("password not match")
            return redirect('/registration')
        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/user')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')
    return render(request,"login.html")

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('form created')
            return redirect('/success')
    else:
        form = StudentForm()
    return render(request, 'form.html', {'form': form})


def success(request):
    return render(request,'confirmation_message.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)
