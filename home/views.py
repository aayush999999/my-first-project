from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Registration
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable1':"This is sent",
        'variable2':"Aayush"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page Mobile No. :- 6394983436")

def reg(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        name=request.POST.get('name')
        password=request.POST.get('password')
        contact=Registration(name=name,password=password,date=datetime.today())
        messages.success(request,"Successfully Registered")
        contact.save()
        context["name"] = name

    return render(request, 'reg.html', context=context)
    #return HttpResponse("this is services page")


def login(request):
    return render(request, 'login.html')