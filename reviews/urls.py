from django.urls import path
from . import views

urlpatterns = [
    path('all_reviews/', views.reviews, name='all_reviews'),

]
