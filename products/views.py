from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def phone_category(request):
    "Вывод товара по категории"
    phones = Product.objects.filter(category=Category.objects.get(name="Phone"))
    return render(request, "products/phones.html", {"phones": phones})


def notebook_category(request):
    "Вывод товара по категории"
    notebooks = Product.objects.filter(category=Category.objects.get(name="Notebook"))
    return render(request, "products/notebooks.html", {"notebooks": notebooks})


def tablet_category(request):
    "Вывод товара по категории"
    tablets = Product.objects.filter(category=Category.objects.get(name="Tablet"))
    return render(request, "products/tablets.html", {"tablets": tablets})


def phone_detail(request, slug):
    """Вывод определенного товара по slug"""
    phone = get_object_or_404(Product, slug=slug)
    context = {
        "phone": phone
    }
    return render(request, "products/phone_detail.html", context=context)


def notebook_detail(request, slug):
    """Вывод определенного товара по slug"""
    notebook = get_object_or_404(Product, slug=slug)
    context = {
        "notebook": notebook
    }
    return render(request, "products/notebook_detail.html", context=context)


def tablet_detail(request, slug):
    """Вывод определенного товара по slug"""
    tablet = get_object_or_404(Product, slug=slug)
    context = {
        "tablet": tablet
    }
    return render(request, "products/tablet_detail.html", context=context)