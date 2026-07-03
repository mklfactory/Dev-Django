from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('review/create/', views.create_review, name='create_review'),
]
