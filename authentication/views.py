"""Views for user registration and logout."""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import StyledUserCreationForm


def register_view(request):
    """Register a new user account and log them in immediately."""
    if request.user.is_authenticated:
        return redirect("feed")

    form = StyledUserCreationForm()
    if request.method == "POST":
        form = StyledUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")

    return render(request, "authentication/register.html", {"form": form})


def logout_view(request):
    """Log the current user out and redirect to the home page."""
    logout(request)
    return redirect("home")
