from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TicketForm, ReviewForm
from .models import Review


@login_required
def feed(request):
    reviews = Review.objects.select_related('ticket', 'user').order_by('-time_created')
    return render(request, 'reviews/feed.html', {'reviews': reviews})


@login_required
def create_review(request):
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
