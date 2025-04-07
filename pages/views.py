from django.shortcuts import render
from pages.models import Login
from .forms import LoginForm
# from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse('Index Page')
    x= {'name':'ali','age':30}
    return render(request,'pages/index.html',x)

def about(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    data=Login(username=username , password=password)
    print(username)
    print(password)
    data.save()



    return render(request,'pages/about.html',{'lf':LoginForm})

