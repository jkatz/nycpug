from django import forms

from models import Proposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = (
            'name',
            'email',
            'proposal_name',
            'proposal_length',
            'description',
            'other',
        )