from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import CustomUser, School


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        school = forms.ModelChoiceField(queryset=School.objects.all())
        fields = ('first_name', 'last_name', 'school', 'username', 'email', 'password1', 'password2')
        