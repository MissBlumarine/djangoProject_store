from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from users.models import User

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
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

