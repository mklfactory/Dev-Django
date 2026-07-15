from django.shortcuts import render, redirect
from django.contrib.auth import login
from authentication.forms import StyledAuthenticationForm


def home(request):
    if request.user.is_authenticated:
        return redirect("feed")

    form = StyledAuthenticationForm()
    if request.method == "POST":
        form = StyledAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("feed")

    return render(request, "home/home.html", {"form": form})
