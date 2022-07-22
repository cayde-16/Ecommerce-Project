from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import datetime 


# Create your views here.

def main(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()[0:3]
    latest_products = Product.objects.all().reverse()[3:9]


    context = {'latest_products':latest_products,'products': products, 'cartItems':cartItems, 'items':items}
    return render(request, 'base/main.html', context)

   
    


def product(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']


    context = {'cartItems':cartItems, 'products':products}
    return render(request,'base/products.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {"items":items, "order":order, 'cartItems':cartItems}
    return render(request, 'base/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    if request.method == 'POST':
        return redirect('main')


    context = {'cartItems':cartItems, 'order':order, 'items':items}
    return render(request, 'base/checkout.html', context)

def details(request, pk):
    product = Product.objects.get(id=pk)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {'order':order, 'items':items, 'product':product, 'cartItems':cartItems}
    return render(request, 'base/details.html', context)

def login_user(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {'order':order, 'items':items,'cartItems':cartItems}
    return render(request,'base/login.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
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


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
    else:
        prin('User is not logged in')
    return JsonResponse('Payment Complete!', safe=False)
