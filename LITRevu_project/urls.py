from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('ticket/add/', views.create_ticket, name='create_ticket'),
    path('review/add/', views.create_review_no_ticket, name='create_review'),
    path('review/reply/<int:ticket_id>/', views.reply_to_ticket, name='reply_to_ticket'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('posts/', views.my_posts, name='my_posts'),
]