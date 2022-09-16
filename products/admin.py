from django.contrib import admin
from .models import Notebook, Phone, Tablet, Category


admin.site.register(Notebook)
admin.site.register(Phone)
admin.site.register(Tablet)
admin.site.register(Category)