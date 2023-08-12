from itertools import chain

from django.shortcuts import render
from .models import ProductRight
from left.models import Product

# Create your views here.


def display_both(request):
    products1 = Product.objects.all()
    products2 = ProductRight.objects.all()
    context = {'left': products1, 'right': products2}
    return render(request, 'index.html', context=context)


def show_more(request, pk):
    product = ProductRight.objects.get(pk=pk)

    return render(request, 'More.html', {'product': product})