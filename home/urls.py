from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",        views.homepage, name='home'),
    path("about",   views.about,    name='about'),
    path("aboutpost/<int:id>",   views.aboutpost,    name='aboutpost'),
    path("contact", views.contact,  name='contact'),
    path("reg",     views.reg,      name='reg'),
    path("login",   views.login,    name='login'),
    path("logout",  views.logout,   name='logout'),
    path("stock",   views.stock,    name='stock'),
    path("practice",  views.practice,   name='practice'),
    path("cart",    views.cart,     name='cart'),
    path("tracker", views.tracker,  name='tracker'),
    path("search",  views.search,   name='search'),
    path("checkout",views.checkout, name='checkout'),
    path("productview",views.productview, name='prodView'),
    path("seller",views.seller, name='seller'),
]

