from django.shortcuts import render
from .models import Product


def index_view(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})
