from django.shortcuts import render
from .models import Product
# Create your views here.

def show_more(request, pk):
    product = Product.objects.get(pk=pk)

    return render(request, 'More.html', {'product': product})