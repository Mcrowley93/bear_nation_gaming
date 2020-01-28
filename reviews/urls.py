from django.urls import path
from reviews.views import all_reviews, add_a_review, reviews_search

urlpatterns = [
    path('all_reviews/', all_reviews, name='all_reviews'),
    path('add_a_review/', add_a_review, name='add_a_review'),
    path('reviews_search', reviews_search, name='reviews_search'),
]
