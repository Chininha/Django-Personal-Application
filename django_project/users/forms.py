# forms complementares

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class NewUserFields(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta: # modelo que o form vai interagir
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#model form -> form que interage com um modelo de database
class UserUpdateForm(forms.ModelForm): # para atualizar o nome e email
    email = forms.EmailField(required=False)

    class Meta: # modelo que o form vai interagir
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm): # para atualizar a imagem de perfil
    class Meta:
        model = Profile
        fields = ['image']