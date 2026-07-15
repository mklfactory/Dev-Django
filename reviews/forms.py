"""Forms for creating/editing tickets, reviews, and following other users."""

from django import forms
from django.contrib.auth.models import User
from .models import Ticket, Review, UserFollows

INPUT_CLASSES = (
    "w-full border border-gray-300 rounded-lg px-3 py-2 "
    "focus:outline-none focus:ring-2 focus:ring-blue-500"
)
FILE_INPUT_CLASSES = (
    "block w-full text-sm text-gray-600 "
    "file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 "
    "file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
)


class TicketForm(forms.ModelForm):
    """Create or edit a `Ticket` (title, description, optional image)."""

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES, "rows": 4}),
            "image": forms.ClearableFileInput(attrs={"class": FILE_INPUT_CLASSES}),
        }


class ReviewForm(forms.ModelForm):
    """Create or edit a `Review` (headline, rating, body)."""

    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]
        widgets = {
            "headline": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "rating": forms.RadioSelect,
            "body": forms.Textarea(attrs={"class": INPUT_CLASSES, "rows": 4}),
        }


class FollowUserForm(forms.Form):
    """Look up a user by username and validate that they can be followed."""

    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "ex : alice"}),
    )

    def __init__(self, *args, current_user=None, **kwargs):
        self.current_user = current_user
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.") from None

        if user == self.current_user:
            raise forms.ValidationError("Tu ne peux pas te suivre toi-même.")

        if UserFollows.objects.filter(user=self.current_user, followed_user=user).exists():
            raise forms.ValidationError("Tu suis déjà cet utilisateur.")

        self.cleaned_data["user"] = user
        return username
