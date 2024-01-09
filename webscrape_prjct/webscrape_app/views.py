from django.http import HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup as bs
from .models import Links
import requests
# Create your views here.
def home(request):
    if request.method=='POST':
        new_link=request.POST.get('page','')
        url=requests.get(new_link)
        bts=bs(url.text,'html.parser')
        for link in bts.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,name=li_name)
        return HttpResponseRedirect('/')
    else:
        datavalues=Links.objects.all()
    return render(request,'home.html',{'values':datavalues})
