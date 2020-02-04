from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('blogs/', include('blogs.urls')),
    path('reviews/', include('reviews.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('accounts/', include('accounts.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]

handler404 = 'home.views.error_404_view'
