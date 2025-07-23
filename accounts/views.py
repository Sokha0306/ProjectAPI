from django.shortcuts import *
from django.http import *
from .models import*
from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.


def IndexTZ(request): 
    return render(request, 'TZ/index.html')

def ShopTZ(request):
    return render(request, 'TZ/shop.html')

def AboutTZ(request):
    return render(request, 'TZ/about.html')

def ProDetailTZ(request):
    return render(request, 'TZ/product_details.html')

def BlogTZ(request):
    return render(request, 'TZ/blog.html')

def BlogDetailTZ(request):
    return render(request, 'TZ/blog-details.html')

def LoginTZ(request):
    return render(request, 'TZ/login.html')

def CartTZ(request):
    return render(request, 'TZ/cart.html')

def ConfirmTZ(request):
    return render(request, 'TZ/confirmation.html')

def CheckoutTZ(request):
    return render(request, 'TZ/checkout.html')

def ContactTZ(request):
    return render(request, 'TZ/contact.html')

