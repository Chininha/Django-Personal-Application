# forms complementares

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserFields(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta: # modelo que o form vai interagir
        model = User
        fields = ['username', 'email', 'password1', 'password2']