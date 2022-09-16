from django.shortcuts import render, get_object_or_404
from .models import Phone, Tablet, Notebook


def phone_category(request):
    phones = Phone.objects.all()
    return render(request, "products/phones.html", {"phones": phones})


def notebook_category(request):
    notebooks = Notebook.objects.all()
    return render(request, "products/notebooks.html", {"notebooks": notebooks})


def tablet_category(request):
    tablets = Tablet.objects.all()
    return render(request, "products/tablets.html", {"tablets": tablets})


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, "products/phone_detail.html", {"phone": phone})


def notebook_detail(request, slug):
    notebook = get_object_or_404(Phone, slug=slug)
    return render(request, "products/notebook_detail.html", {"notebook": notebook})


def tablet_detail(request, slug):
    tablet = get_object_or_404(Tablet, slug=slug)
    return render(request, "products/tablet_detail.html", {"tablet": tablet})