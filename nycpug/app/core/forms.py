import re
from django import forms

from .models import Proposal

class ProposalForm(forms.Form):
    """creates a proposal + bio info"""
    PROPOSAL_FIELDS = ['title', 'description', 'format', 'other']
    PROFILE_FIELDS = ['profile_company', 'profile_title', 'profile_description', 'twitter', 'irc']
    title = forms.CharField(
        label='Title',
        max_length=255,
    )
    format = forms.ChoiceField(
        label='Format',
        choices=Proposal.FORMATS,
    )
    description = forms.CharField(
        label='Abstract',
        widget=forms.widgets.Textarea(attrs={ 'cols': 80, 'rows': 8 }),
    )
    other = forms.CharField(
        label='Additional Information for Reviewer (optional)',
        widget=forms.widgets.Textarea(attrs={ 'cols': 80, 'rows': 8 }),
        required=False,
    )
    profile_company = forms.CharField(
        label='Company',
        max_length=255,
    )
    profile_title = forms.CharField(
        label='Position',
        max_length=255,
    )
    profile_description = forms.CharField(
        label='Bio',
        widget=forms.widgets.Textarea(attrs={ 'cols': 80, 'rows': 8 }),
    )
    twitter = forms.CharField(
        label='Twitter',
        max_length=20,
        required=False,
    )
    irc = forms.CharField(
        label='IRC',
        required=False,
    )

    def clean_twitter(self):
        if self.cleaned_data.get('twitter'):
            return re.sub(r'^@' , '', self.cleaned_data.get('twitter'))

    def save(self, *args, **kwargs):
        """save the proposal info, update user profile"""
        if self.instance: # updating proposal
            for key in self.PROPOSAL_FIELDS:
                self.instance.__setattr__(key, self.cleaned_data.get(key))
            self.instance.save()
        else: # creating new proposal
            self.instance = self.request.user.proposals.create(
                conference=self.request.conference,
                title=self.cleaned_data.get('title'),
                description=self.cleaned_data.get('description'),
                other=self.cleaned_data.get('other'),
            )
        # update profile info
        for key in self.PROFILE_FIELDS:
            self.request.user.profile.__setattr__(key.replace('profile_', ''), self.cleaned_data.get(key))
        self.request.user.profile.save()
        return self.instance

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        self.request = kwargs.pop('request')
        super(ProposalForm, self).__init__(*args, **kwargs)
        if self.instance:
            for key in self.PROPOSAL_FIELDS:
                self.fields.get(key).initial = self.instance.__getattribute__(key)
        for key in self.PROFILE_FIELDS:
            self.fields.get(key).initial = self.request.user.profile.__getattribute__(key.replace('profile_', ''))
