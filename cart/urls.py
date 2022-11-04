from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name="cart"),
    path('clear', views.cart_clear, name="clear_cart"),
    path('add/<int:id>', views.cart_add, name="add_to_cart"),
    path("remove/<int:id>", views.cart_remove, name="remove_from_cart")
]