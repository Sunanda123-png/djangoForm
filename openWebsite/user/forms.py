from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password',)
