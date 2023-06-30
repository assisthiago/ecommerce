from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
        form = SignInForm(request.POST)
        if not form.is_valid():
            return render(request, 'sign-in.html', {'form': form})

        user = authenticate(
            request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password'])

        if not user:
            messages.error(request, 'E-mail ou senha incorreta.')
            return render(request, 'sign-in.html', {'form': form})

        login(request, user)
        return redirect('home')

    return render(request, 'sign-in.html', {'form': SignInForm()})


def sign_up(request):
    return render(request, 'sign-up.html')


def sign_out(request):
    logout(request)
    return redirect('home')


def recover_password(request):
    return render(request, 'recover-password.html')
