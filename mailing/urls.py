from django.urls import path
from . import views


urlpatterns = [
    path('feedbacks', views.feedback, name='feedback'),
    path('mailing', views.mailing, name='mail_send'),
]