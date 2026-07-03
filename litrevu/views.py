from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import TicketForm, ReviewForm
from .models import Review

def home(request):
    if request.user.is_authenticated:
        return redirect('feed')
    return redirect('login')

@login_required
def feed(request):
    reviews = Review.objects.select_related('ticket', 'user').order_by('-time_created')
    return render(request, 'feed.html', {'reviews': reviews})

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

    return render(request, 'review_form.html', {
        'ticket_form': ticket_form,
        'review_form': review_form,
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('feed')
    
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feed')
    
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('feed')
    
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')