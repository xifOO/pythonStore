from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def phone_category(request):
    phones = Product.objects.filter(category=Category.objects.get(name="Phones"))
    return render(request, "products/phones.html", {"phones": phones})


def notebook_category(request):
    notebooks = Product.objects.filter(category=Category.objects.get(name="Notebooks"))
    return render(request, "products/notebooks.html", {"notebooks": notebooks})


def tablet_category(request):
    tablets = Product.objects.filter(category=Category.objects.get(name="Tablets"))
    return render(request, "products/tablets.html", {"tablets": tablets})


def phone_detail(request, slug):
    phone = get_object_or_404(Product, slug=slug)
    context = {
        "phone": phone
    }
    return render(request, "products/phone_detail.html", context=context)


def notebook_detail(request, slug):
    notebook = get_object_or_404(Product, slug=slug)
    context = {
        "notebook": notebook
    }
    return render(request, "products/notebook_detail.html", context=context)


def tablet_detail(request, slug):
    tablet = get_object_or_404(Product, slug=slug)
    context = {
        "tablet": tablet
    }
    return render(request, "products/tablet_detail.html", context=context)