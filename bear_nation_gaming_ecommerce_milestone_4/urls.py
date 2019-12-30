from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('products/', include('products.urls')),
    # path('blogs/', include('blogs.urls')),
    # path('reviews/', include('reviews.urls')),
    # path('cart/', include('cart.urls')),
    # path('checkout/', include('checkout.urls')),
]
