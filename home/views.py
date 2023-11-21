from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Registration,ItemInsert
# from django.contrib.auth.models import User
from django.contrib import messages
# from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login
from math import ceil


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
        
        Registration.objects.create(name=name,password=password,date=datetime.today())

        # context["name"] = name

        messages.success(request,"Successfully Registered")
        return redirect ('login')

    return render(request, 'reg.html' ) #context=context



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




#   Stock Display
def stock(request): 
    # iteminserts = ItemInsert.objects.all()
    # n = len(iteminserts)
    # nSlides= n//4 + ceil((n/4) - (n//4))

    allitems = []

    descitems = ItemInsert.objects.values('item_desc')
    print(descitems)
    descs = {item['item_desc'] for item in descitems }
    for desc in descs:
        itm = ItemInsert.objects.filter( item_desc = desc)
        n = len(itm)
        nSlides= n//4 + ceil((n/4) - (n//4))
        allitems.append([itm, range(1, nSlides), nSlides])

    params = {'allitems':allitems}
    return render(request, 'stock.html', params)





def seller(request):
    item=ItemInsert.objects.all()
    return render(request, 'seller.html',{'item':item})