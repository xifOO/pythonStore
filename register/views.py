import copy
from cart.logic import Cart
from config.settings import CART_SESSION_ID
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseBadRequest


def register(request):
    """Регистрация"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data.get("username")
                password1 = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=password1)
                login(request, user)
                return redirect('/')
            except Exception as e:
                return HttpResponseBadRequest("Попробуйте снова!")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def logout_user(request):
    """Сохраняем глубокую копию корзины по сессии и выходим"""
    try:
        cart = copy.deepcopy(Cart(request).cart)
        logout(request)
        session = request.session
        session[CART_SESSION_ID] = cart
        session.modified = True
        return redirect("/")
    except Exception as e:
        return HttpResponseBadRequest("Попробуйте снова!")