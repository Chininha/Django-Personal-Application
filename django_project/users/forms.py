# forms complementares

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserFields(UserCreationForm):
    email = forms.EmailField(required=False)
    first = forms.CharField(max_length=60)
    last = forms.CharField(max_length=60)

    class Meta: # modelo que o form vai interagir
        model = User
        fields = ['username', 'email', 'first name', 'last name', 'password1', 'password2']