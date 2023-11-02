from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Registration
# from django.contrib.auth.models import Registration
from django.contrib import messages
from django.core.exceptions import ValidationError


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
    # context = {}
    if request.method == "POST":
        

        # print(request.POST)
        name = request.POST.get('name')
        password = request.POST.get('password')
        if not name :
            messages.success(request,"name is blank")
            return render(request, 'reg.html', ) 
        
        if not password :
            messages.success(request,"password is blank")
            return render(request, 'reg.html', ) 
        
        if len(password) < 6:
            messages.success(request, 'Password too short')
            return render(request, 'reg.html', )


        # myuser = Registration.objects.create_registration(name, password)
        # myuser.save()
        # myuser=Registration(name=name,password=password)
        # contact = Registration(name=name,password=password,date=datetime.today())
        # contact.save()

        Registration.objects.create(name=name,password=password,date=datetime.today())

        # context["name"] = name

        messages.success(request,"Successfully Registered")
        

    return render(request, 'reg.html', ) #context=context
    #return HttpResponse("this is services page")


def login(request):
    return render(request, 'login.html')

 
# def logout(request):
#     pass