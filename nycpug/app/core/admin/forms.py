from django import forms

from nycpug.app.account.models import User
from nycpug.app.core.models import Opinion

__all__ = [
    'OpinionForm',
]

class OpinionForm(forms.ModelForm):
    """track opinions"""
    class Meta:
        model = Opinion
