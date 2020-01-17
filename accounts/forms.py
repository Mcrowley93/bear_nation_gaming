from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# Code for the forms was reused and adapted from the CI e-commerce mini-project

# User Login - Form for login page
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput
                               (attrs={'placeholder': 'username/email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


# User Registration - Form to allow accounts to register
class UserRegistrationForm(UserCreationForm):
    """ UserCreationForm already comes with username and email, the below password fields were then added to that """
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError('Please confirm your password')

        if password1 != password2:
            raise ValidationError("Passwords must match!")

        return password2
