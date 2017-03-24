from django.contrib.auth.models import User
from django import forms
from .models import ExtendedUser
from django.core import validators
from django.forms import ModelForm

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_repeat_password(self):

        if self.cleaned_data['password'] != self.cleaned_data['repeat_password']:
            raise validators.ValidationError('Passwords arent the same!')
        return self.repeat_password

class ExtendedUserInformationForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['index_number', 'year']

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username:")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)


