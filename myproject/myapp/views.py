from django.shortcuts import render
from django.http import HttpResponse
from .models import places
from .models import team
# Create your views here.
def demo(request):
    obj=places.objects.all()
    obj1=team.objects.all()
    return render(request,'index.html',{'key': obj,'key1':obj1})


# def about(request):
#     return render(request,"about.html")
# def help(request):
#     return HttpResponse('help desk')
