from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('Index Page')
    x= {'name':'ali','age':30}
    return render(request,'pages/index.html',x)

def about(request):
    # return HttpResponse('About Page')
    return render(request,'pages/about.html')

