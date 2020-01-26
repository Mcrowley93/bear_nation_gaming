from django.urls import path
from blogs.views import all_posts, post_new, post_edit, post_remove, post_detail, posts_search

urlpatterns = [
    path('all_posts/', all_posts, name='all_posts'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<pk>/remove/', post_remove, name='post_remove'),
    # the post_detail urlpattern begins with post/ we then use <int:pk>/ so that django expects an integer value
    # it will then transfer it to the post_detail view as a variable called pk
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('posts_search', posts_search, name='posts_search'),

]
