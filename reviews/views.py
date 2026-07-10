from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TicketForm, ReviewForm
from .models import Review, Ticket


@login_required
def feed(request):
    reviews = (
        Review.objects.select_related('ticket', 'user')
        .order_by('-time_created')
    )
    return render(request, 'reviews/feed.html', {'reviews': reviews})


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
