"""Authentication forms styled with the project's Tailwind input classes."""

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

INPUT_CLASSES = (
    "w-full border border-gray-300 rounded-lg px-3 py-2 "
    "focus:outline-none focus:ring-2 focus:ring-blue-500"
)


class StyledAuthenticationForm(AuthenticationForm):
    """Login form with Tailwind classes applied to every field widget."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_CLASSES


class StyledUserCreationForm(UserCreationForm):
    """Registration form with Tailwind classes applied to every field widget."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_CLASSES
