from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect(reverse('index'))

            else:
                return render(request, 'login.html', {'form': form, 'message': 'Wrong password. Please try again.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
