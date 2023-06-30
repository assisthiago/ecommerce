from django.shortcuts import redirect, render

from app.categories.models import Category
from app.core.forms import SignInForm
from app.products.models import Product


def home(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }

    return render(request, 'index.html', context=context)


def sign_in(request):
    if request.method == 'POST':
        return redirect('home')

    return render(request, 'sign-in.html', {'form': SignInForm()})


def sign_up(request):
    return render(request, 'sign-up.html')


def sign_out(request):
    return redirect('home')


def recover_password(request):
    return render(request, 'recover-password.html')
