from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import phone_category, tablet_category, notebook_category, phone_detail, tablet_detail, notebook_detail


urlpatterns = [
    path("phones", phone_category, name="phones"),
    path("tablets", tablet_category, name="tablets"),
    path("notebooks", notebook_category, name="notebooks"),
    path("phone/<str:slug>/", phone_detail, name="phone_detail"),
    path("tablet/<str:slug>/", tablet_detail, name="tablet_detail"),
    path("notebook/<str:slug>/", notebook_detail, name="notebook_detail"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)