from django.shortcuts import render

# Create your views here.

def main(request):
    context = {}
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