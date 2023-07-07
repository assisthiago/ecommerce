from django.shortcuts import get_object_or_404, render

from app.products.models import Product


def detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "detail.html", {"product": product})
