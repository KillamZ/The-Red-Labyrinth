from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        school = forms.Select()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        