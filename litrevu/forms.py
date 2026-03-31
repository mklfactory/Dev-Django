from django import imports
from django import forms
from .models import Ticket, Review, UserFollows

class TicketForm(forms.Model_Form):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(6)])
        }

class UserFollowsForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=150)