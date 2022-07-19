from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json

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

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'order':order, 'items':items, 'product':product}
    return render(request, 'base/details.html', context)

def login_user(request):
    context = {}
    return render(request,'base/login.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quanity = (orderItem.quanity + 1)
    elif action == 'remove':
        orderItem.quanity = (orderItem.quanity - 1)

    orderItem.save()
    if orderItem.quanity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)