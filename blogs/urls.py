from django.urls import path
from blogs.views import all_posts

urlpatterns = [
    path('blogs/', all_posts, name='all_posts'),
]
