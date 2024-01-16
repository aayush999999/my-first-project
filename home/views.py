from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Registration,ItemInsert,Contact,Checkout,OrderUpdate,Blogpost
from django.contrib import messages
from django.contrib.auth.models import Registration
from math import ceil
import json
# from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError




# Create your views here.

def homepage(request):
    context={
        'variable1':"This is sent",
        'variable2':"Aayush"
    }
    return render(request, 'homepage.html', context)
    #return HttpResponse("this is homepage")


def about(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'aboutpost.html',{'myposts':myposts})


def aboutpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'about.html', {'post':post})


def contact(request):
    thank=False
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        mobile=request.POST.get('mobile', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, mobile=mobile, desc=desc)
        contact.save()
        thank=True
        # print(name,email,mobile, desc )
    return render(request, "contact.html", {'thank':thank})


def reg(request):
    if request.method == "POST":
        # print(request.POST)
        name = request.POST.get('name')
        password = request.POST.get('password')
        if not name :
            messages.warning(request,"name is blank")
            return render(request, 'reg.html', ) 
        
        if not password :
            messages.warning(request,"password is blank")
            return render(request, 'reg.html', ) 
        
        if len(password) < 6:
            messages.warning(request, 'Password too short')
            return render(request, 'reg.html', )
        
        Registration.objects.create(name=name,password=password,date=datetime.today())
        messages.success(request,"Successfully Registered")
        return redirect('login')
    else:
        return render(request,'404 Not Found')


def login(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(request.POST) 
        User=authenticate(request,email=email,password=password) 
        if User is not None:
            login(request,User)
            return redirect('about')
        else:
            messages.warning(request,"Username or Password is incorrect!!")

    return render(request, 'login.html')

 
def logout(request):
    User=authenticate
    logout(request,User)
    return render(request, 'homepage.html')


#   Stock Display
def stock(request): 
    # iteminserts = ItemInsert.objects.all()
    # n = len(iteminserts)
    # nSlides= n//4 + ceil((n/4) - (n//4))

    allitems = []

    descitems = ItemInsert.objects.values('item_desc','id')
    print(descitems)
    descs = {item['item_desc'] for item in descitems }
    for desc in descs:
        itm = ItemInsert.objects.filter( item_desc = desc)
        n = len(itm)
        nSlides= n//4 + ceil((n/4) - (n//4))
        allitems.append([itm, range(1, nSlides), nSlides])

    params = {'allitems':allitems}
    return render(request, 'stock.html', params)
 

def search(request):
    query = request.POST.get('search')
    if len(query)>78:
        item = ItemInsert.objects.none()
    else:
        itemItem_desc= ItemInsert.objects.filter(item_desc__icontains=query)
        itemItem_group= ItemInsert.objects.filter(item_group__icontains=query)
        item= itemItem_desc.union(itemItem_group)
    if item.count() == 0:
        messages.warning(request, "No Search result found. Please refine your query ")    
    params={'item': item, 'query': query}
    return render(request, 'search.html', params)


#    CART VIEW
def cart(request):
    return render(request, 'homepage.html')


def practice(request):
    item=ItemInsert.objects.all()
    return render(request, 'practice.html',{'item':item})


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Checkout.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success","updates":updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, "tracker.html")  


def checkout(request):
    if request.method=="POST":
        print(request)
        items_json = request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        addr=request.POST.get('addr', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        number=request.POST.get('number', '')
        checkout = Checkout(items_json=items_json, amount=amount, name=name, email=email, addr=addr, city=city, state=state, zip_code=zip_code, number=number)
        checkout.save()
        update= OrderUpdate(order_id= checkout.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=checkout.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
        # print(name,email,addr, city, state, zip, number )
        # Request Paytm to transfer the amount to your account after payment by user
        # param_dict = {
        #     'MID': 'WorldP64425807474247',
        #     'ORDER_ID': 'checkout.order_id',
        #     'TXN_AMOUNT': '1',
        #     'CUST_ID': 'email',
        #     'INDUSTRY_TYPE_ID': 'Retail',
        #     'WEBSITE': 'WEBSTAGING',
        #     'CHANNEL_ID': 'WEB',
        #     'CALLBACK_URL':'http://127.0.0.1:8000/home/handlepayment/',
        # }
        # return  render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, "checkout.html")


# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     pass


def seller(request):
    if request.method=="POST":
        print(request)
        image=request.FILES['image']
        item_desc=request.POST.get('item_desc', '')
        item_group=request.POST.get('item_group', '')
        item_rate=request.POST.get('item_rate', '')
        stock_qty=request.POST.get('stock_qty', '')
        itemInsert = ItemInsert(image=image, item_desc=item_desc, item_group=item_group, item_rate=item_rate, stock_qty=stock_qty, item_date=datetime.today())
        itemInsert.save()
    return render(request, "seller.html") 