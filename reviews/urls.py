from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('posts/', views.my_posts, name='my_posts'),
    path('tickets/create/', views.create_ticket, name='create_ticket'),
    path(
        'tickets/<int:ticket_id>/edit/',
        views.edit_ticket,
        name='edit_ticket',
    ),
    path(
        'tickets/<int:ticket_id>/delete/',
        views.delete_ticket,
        name='delete_ticket',
    ),
    path(
        'tickets/<int:ticket_id>/review/create/',
        views.create_review,
        name='create_review',
    ),
    path(
        'reviews/<int:review_id>/edit/',
        views.edit_review,
        name='edit_review',
    ),
    path(
        'reviews/<int:review_id>/delete/',
        views.delete_review,
        name='delete_review',
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
