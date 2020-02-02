from django.urls import path
from reviews.views import all_reviews, add_a_review, reviews_search, read_review, edit_a_review, remove_review

urlpatterns = [
    path('all_reviews/', all_reviews, name='all_reviews'),
    path('add_a_review/', add_a_review, name='add_a_review'),
    path('reviews_search', reviews_search, name='reviews_search'),
    path('read_review/<int:pk>/', read_review, name='read_review'),
    path('review/<int:pk>/edit/', edit_a_review, name='edit_a_review'),
    path('review/<pk>/remove/', remove_review, name='remove_review'),

]
