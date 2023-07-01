from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from app.categories.models import Category
from app.core.forms import SignInForm, SignUpForm
from app.products.models import Product
from app.profiles.models import Profile


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

        if not _login(request, form):
            messages.error(request, 'E-mail ou senha incorreta.')
            return render(request, 'sign-in.html', {'form': form})

        return redirect('home')

    return render(request, 'sign-in.html', {'form': SignInForm()})


def _login(request, form):
    user = authenticate(
        request,
        username=form.cleaned_data['email'],
        password=form.cleaned_data['password'])

    if not user:
        return

    login(request, user)
    return user


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'sign-up.html', {'form': form})

        try:
            Profile.create_user(form)

        except:
            messages.error(request, 'Conta já cadastrada.')
            return render(request, 'sign-up.html', {'form': form})

        messages.success(request, 'Conta cadastrada.')
        return redirect('sign-in')

    return render(request, 'sign-up.html', {'form': SignUpForm()})


def sign_out(request):
    logout(request)
    return redirect('home')


def recover_password(request):
    return render(request, 'recover-password.html')
