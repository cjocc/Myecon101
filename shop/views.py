from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    n_slides = n//4 + ceil((n/4)-(n//4))
    params = {'no_slides': n_slides, 'range': range(1, n_slides), 'product': products}

    return render(request, 'shop/Index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Contact us")


def tracking(request):
    return HttpResponse("Track order")


def product(request):
    return render(request, 'Product View')


def checkout(request):
    return HttpResponse("Check out")


def search(request):
    return HttpResponse("Search")
