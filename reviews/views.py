from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import TicketForm, ReviewForm, FollowUserForm
from .models import Review, Ticket, UserFollows


@login_required
def feed(request):
    followed_ids = request.user.following.values_list(
        'followed_user_id', flat=True
    )
    visible_user_ids = list(followed_ids) + [request.user.id]

    reviews = Review.objects.filter(
        user_id__in=visible_user_ids
    ).select_related('ticket', 'user')

    tickets = Ticket.objects.filter(
        user_id__in=visible_user_ids, reviews__isnull=True
    ).select_related('user')

    feed_items = sorted(
        chain(reviews, tickets),
        key=lambda item: item.time_created,
        reverse=True,
    )
    return render(request, 'reviews/feed.html', {'feed_items': feed_items})


@login_required
def ticket_list(request):
    tickets = (
        Ticket.objects.select_related('user')
        .prefetch_related('reviews')
        .order_by('-time_created')
    )
    return render(request, 'reviews/ticket_list.html', {'tickets': tickets})


@login_required
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_list')

    return render(request, 'reviews/ticket_form.html', {'form': form})


@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if ticket.reviews.exists():
        messages.info(request, "Ce ticket a déjà une critique.")
        return redirect('ticket_list')

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('feed')

    return render(request, 'reviews/review_only_form.html', {
        'form': form,
        'ticket': ticket,
    })


@login_required
def create_ticket_review(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect('feed')

    return render(request, 'reviews/review_form.html', {
        'ticket_form': ticket_form,
        'review_form': review_form,
    })


@login_required
def follows(request):
    form = FollowUserForm(current_user=request.user)
    if request.method == 'POST':
        form = FollowUserForm(request.POST, current_user=request.user)
        if form.is_valid():
            UserFollows.objects.create(
                user=request.user,
                followed_user=form.cleaned_data['user'],
            )
            return redirect('follows')

    following = UserFollows.objects.filter(
        user=request.user
    ).select_related('followed_user')
    followers = UserFollows.objects.filter(
        followed_user=request.user
    ).select_related('user')

    return render(request, 'reviews/follows.html', {
        'form': form,
        'following': following,
        'followers': followers,
    })


@require_POST
@login_required
def unfollow(request, user_id):
    UserFollows.objects.filter(
        user=request.user, followed_user_id=user_id
    ).delete()
    return redirect('follows')
