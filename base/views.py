from django.shortcuts import render

# Create your views here.

def main(request):
    context = {}
    return render(request, 'base/main.html', context)

    
def store(request):
    context = {}
    return render(request,'base/store.html', context)

def cart(request):
    context = {}
    return render(request, 'base/cart.html', context)


def checktout(request):
    context = {}
    return render(request, "base/checkout.html", context)