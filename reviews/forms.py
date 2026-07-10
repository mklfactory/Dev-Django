from django import forms
from django.contrib.auth.models import User
from .models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect,
        }


class FollowUserForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")

    def __init__(self, *args, current_user=None, **kwargs):
        self.current_user = current_user
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.")

        if user == self.current_user:
            raise forms.ValidationError("Tu ne peux pas te suivre toi-même.")

        if UserFollows.objects.filter(
            user=self.current_user, followed_user=user
        ).exists():
            raise forms.ValidationError("Tu suis déjà cet utilisateur.")

        self.cleaned_data['user'] = user
        return username
