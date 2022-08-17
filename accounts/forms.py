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
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )
        

    # def clean_email(self):
    #     email = self.cleaned_data['email'].lower()
    #     try:
    #         account = Account.objects.get(email=email)
    #     except Exception as e:
    #         raise
    #     raise forms.ValidationError(f"Email {email} already exists")

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         account = Account.objects.get(username=username)
    #     except Exception as e:
    #         raise
    #     raise forms.ValidationError(f"username {username} already exists")