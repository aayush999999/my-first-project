from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Registration,ItemInsert
# from django.contrib.auth.models import User
from django.contrib import messages
# from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login



# Create your views here.

def homepage(request):
    context={
        'variable1':"This is sent",
        'variable2':"Aayush"
    }
    return render(request, 'homepage.html', context)
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
        return redirect ('login')

    return render(request, 'reg.html' ) #context=context
    #return HttpResponse("this is services page")


def login(request):
    if request.method == "POST":
        email =request.POST.get('email')
        password =request.POST.get('password')
        print(request.POST) 
        User=authenticate(request,email=email,password=password) 
        if User is not None:
            login(request,User)
            return redirect('about')
        else:
            messages.warning(request,"Username or Password is incorrect!!")

    return render(request, 'logout.html')

 
# def logout(request):
#     User=authenticate
#     logout(request,User)
#     return render(request, 'homepage.html')


# def logout(request):
# <<<<<<< HEAD
#     # pass
#     logout(request) 
# =======
#     pass
#     logout(request) 



def stock(request):
    return render(request,'stock.html')
 



# 6.11.23
def seller(request):
    # all_objects = ItemInsert.objects.all()
    # #print(all_objects)
    # for it in all_objects:
    #     print(it.item_name)
    # params = {'all_its':all_objects}  
    # return render(request,'seller.html',params)
    
    items = ItemInsert.objects.all()
    # print(items)
    params = {'item': items}
    return render(request, 'seller.html', params)

