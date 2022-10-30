from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart


@login_required(redirect_field_name='accounts/login')
def cart_detail(request):
    """Вывод корзины"""
    cart = Cart(request)
    return render(request, "cart/cart.html", {"cart": cart})


def cart_add(request, product_id):
    """Добавляем товары в корзину по id товара"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    """Удаляем товары из корзину по id товара"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_clear(request):
    """Полная очистка корзины"""
    cart = Cart(request)
    cart.clear()
    return redirect(request.META.get('HTTP_REFERER'))



