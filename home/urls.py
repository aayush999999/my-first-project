from django.contrib import admin
from django.urls import path
from home import views
from .views import logout_user
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",        views.homepage, name='home'),
    path("about",   views.about,    name='about'),
    path("aboutpost/<int:id>",   views.aboutpost,    name='aboutpost'),
    path("contact", views.contact,  name='contact'),
    path("reg",     views.reg,      name='reg'),
    path("login",   views.login_view,    name='login'),
    path("logout",  views.logout_user,   name='logout'),
    path("stock",   views.stock,    name='stock'),
    path("practice",  views.practice,   name='practice'),
    path("cart",    views.cart,     name='cart'),
    path("tracker", views.tracker,  name='tracker'),
    path("search",  views.search,   name='search'),
    path("checkout",views.checkout, name='checkout'),
    path("seller",views.seller, name='seller'),
    # path("handlerequest",views.handlerequest, name='handlerequest'),
    path('logout', login_required(logout_user), name='logout'),

]

