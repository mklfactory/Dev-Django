from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/create/', views.create_ticket, name='create_ticket'),
    path(
        'tickets/<int:ticket_id>/review/create/',
        views.create_review,
        name='create_review',
    ),
    path(
        'ticket-review/create/',
        views.create_ticket_review,
        name='create_ticket_review',
    ),
    path('follows/', views.follows, name='follows'),
    path(
        'follows/<int:user_id>/remove/',
        views.unfollow,
        name='unfollow',
    ),
]
