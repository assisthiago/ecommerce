from django.shortcuts import render

from app.categories.models import Category
from app.products.models import Product

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context=context)
