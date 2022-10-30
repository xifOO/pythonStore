from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("shop.urls")),
    path("category/", include(("products.urls", "products"), namespace="products_urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include(('register.urls', "register"), namespace="register")),
    path("mailing/", include(("mailing.urls", "mailing"), namespace="mailing")),
    path('search/', include(('search.urls', 'search'), namespace='search')),
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)