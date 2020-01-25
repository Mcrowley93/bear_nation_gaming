from django.urls import path
from blogs.views import all_posts, post_detail, posts_search

urlpatterns = [
    path('all_posts/', all_posts, name='all_posts'),
    # the post_detail urlpattern begins with post/ we then use <int:pk>/ so that django expects an integer value
    # it will then transfer it to the post_detail view as a variable called pk
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('posts_search', posts_search, name='posts_search'),

]
