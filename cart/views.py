from django.shortcuts import render
from .cart import Cart
from shop.models import Product
from django.shortcuts import redirect

# Create your views here.

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("Shop")

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product=product)
    return redirect("Shop")

def subtract_product(request, product_id):
    cart=Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product=product)
    return redirect("Shop")

def clean_all_cart(request):
    cart = Cart(request)
    cart.clean_cart()
    return redirect("Shop")
