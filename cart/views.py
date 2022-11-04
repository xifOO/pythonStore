from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart
from payment import payment


@login_required(redirect_field_name='accounts/login')
def cart_detail(request):
    """Вывод корзины"""
    cart = Cart(request)
    pay_url = payment.pay(amount=cart.get_total_price())
    return render(request, "cart/cart.html", {"cart": cart, "pay_url": pay_url})


@login_required(redirect_field_name='accounts/login')
def cart_add(request, id):
    """Добавляем товары в корзину по id товара"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(redirect_field_name='accounts/login')
def cart_remove(request, id):
    """Удаляем товары из корзину по id товара"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(redirect_field_name='accounts/login')
def cart_clear(request):
    """Полная очистка корзины"""
    cart = Cart(request)
    cart.clear()
    return redirect(request.META.get('HTTP_REFERER'))



