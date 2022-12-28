from math import ceil

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    Products = Product.objects.all()
    print(Products)
    n = len(Products)
    no_of_Slides = n//4 + ceil((n/4)-(n//4))
    dict_for_product = {'no_of_Slides':no_of_Slides, 'range': range(1, no_of_Slides), 'product': Products}
    return render(request, 'shop/index.html', dict_for_product)

def about(request):
    return render(request, 'shop/About.html')

def contact(request):
    return HttpResponse("We are at Contact")

def tracker(request):
    return HttpResponse("We are at Tracker")

def search(request):
    return HttpResponse("We are at Search")

def productview(request):
    return HttpResponse("We are at Product View")

def checkout(request):
    return HttpResponse("We are at Checkout")

