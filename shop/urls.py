from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("logout/", views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
]
