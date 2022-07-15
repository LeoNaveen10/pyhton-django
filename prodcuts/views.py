from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request,'index.html' ,{'products' : products})


def newProdcuts(request):
    return HttpResponse('New product page')
    