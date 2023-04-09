from django.shortcuts import render

from cart.cart import Cart


# Create your views here.

def home(request):
    cart = Cart(request)
    return render(request, "webapp/home.html")