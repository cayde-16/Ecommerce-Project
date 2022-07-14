from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checktout, name="checkout"),
    path("product/", views.product, name="product")
    
]