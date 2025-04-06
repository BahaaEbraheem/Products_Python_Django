from django.shortcuts import render
from .models import Product

def products(request):
    pro=Product.objects.all()
    x= {'pro':pro.order_by('price')}
    return render(request,'products/products.html',x)


def product(request):
    return render(request,'products/product.html')
