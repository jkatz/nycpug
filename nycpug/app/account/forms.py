from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

__all__ = [
    'LoginForm',
    'SignupForm',
]

class LoginForm(forms.Form):
    """form for logging in"""
    email = forms.EmailField(
        label='Email',
        max_length='255'
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
    )

    def clean_email(self):
        # make sure email address is lowercase
        if self.cleaned_data.get('email'):
            return self.cleaned_data.get('email').lower().strip()

class SignupForm(forms.Form):
    """form for a user signup"""
    name = forms.CharField(
        label='Name',
        max_length=255,
    )
    email = forms.EmailField(
        label='Email',
        max_length='255'
    )
    password = forms.CharField(
        min_length=6,
        max_length=32,
        label='Password',
        widget=forms.PasswordInput(),
    )

    def clean_email(self):
        # make sure email address is lowercase
        if self.cleaned_data.get('email'):
            email = self.cleaned_data.get('email').lower().strip()
            # see if this exists in a user account
            try:
                get_user_model().objects.get(email=email)
                raise forms.ValidationError('"%s" is already registered.  Please use a different email address' % email)
            except ObjectDoesNotExist: # this is good!
                return email
