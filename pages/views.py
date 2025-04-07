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
    # username=request.POST.get('username')
    # password=request.POST.get('password')
    # data=Login(username=username , password=password)
    # print(username)
    # print(password)
    # data.save()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # Potentially redirect or show a success message here
        else:
            # Handle the case where the form is not valid
            print(form.errors) # Print errors to the console for debugging
            return render(request, 'pages/about.html', {'lf': form}) # Re-render the form with errors
    else:
        form = LoginForm()


    return render(request,'pages/about.html',{'lf':LoginForm})

