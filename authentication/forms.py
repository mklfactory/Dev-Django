from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

INPUT_CLASSES = (
    "w-full border border-gray-300 rounded-lg px-3 py-2 "
    "focus:outline-none focus:ring-2 focus:ring-blue-500"
)


class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_CLASSES


class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_CLASSES
