from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("cart/", views.cart, name="cart"),
    path("login/", views.login_user, name='login'),
    path("product/", views.product, name="product"),
    path("details/", views.details, name="details"),
    path('checkout/', views.checkout, name="checkout")
    
]