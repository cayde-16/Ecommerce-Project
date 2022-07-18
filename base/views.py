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

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {"items":items, "order":order}
    return render(request, 'base/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'base/checkout.html', context)
    
def details(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'base/details.html', context)

def login_user(request):
    context = {}
    return render(request,'base/login.html', context)