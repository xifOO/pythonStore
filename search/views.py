from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView


class Search(ListView):
    template_name = "search/search.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get("s"))

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)
