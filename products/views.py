from django.shortcuts import render
from products.models import Product, ProductCategory

# Create your views here.
# функции = контроллеры = вьюхи


def index(request):
    context = {
        'title': 'Test Title',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


