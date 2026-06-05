from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value, Q
from itertools import chain
from .models import Ticket, Review, UserFollows
from .forms import TicketForm, ReviewForm, UserFollowsForm

@login_required
def feed(request):
    # Utilisateurs suivis
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)
    
    # Tickets & Reviews (Moi + Suivis + Réponses à mes tickets)
    tickets = Ticket.objects.filter(
        Q(user__in=followed_users) | Q(user=request.user)
    ).annotate(content_type=Value('TICKET', CharField()))
    
    reviews = Review.objects.filter(
        Q(user__in=followed_users) | Q(user=request.user) | Q(ticket__user=request.user)
    ).annotate(content_type=Value('REVIEW', CharField()))
    
    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'litrevu/feed.html', {'posts': posts})

@login_required
def subscriptions(request):
    form = UserFollowsForm()
    following = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)
    
    if request.method == 'POST':
        # Logique pour suivre un utilisateur...
        pass
        
    return render(request, 'litrevu/subscriptions.html', {
        'form': form, 'following': following, 'followers': followers
    })