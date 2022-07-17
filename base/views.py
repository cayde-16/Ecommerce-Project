from django.shortcuts import render
from . models import *

# Create your views here.

def main(request):
    products = Product.objects.all()[0:3]
    latest_products = Product.objects.all().reverse()[3:9]
    context = {'latest_products':latest_products,'products': products}
    return render(request, 'base/main.html', context)


def product(request):
    context = {}
    return render(request,'base/products.html', context)


def cart(request):
    context = {}
    return render(request, 'base/cart.html', context)


def details(request):
    context = {}
    return render(request, 'base/details.html', context)

def login_user(request):
    context = {}
    return render(request,'base/login.html', context)