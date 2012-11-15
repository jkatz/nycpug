from django import forms

from models import Conference, Proposal

class ProposalForm(forms.ModelForm):

    conference = forms.ModelChoiceField(
        queryset=Conference.objects.filter(active=True),
        required=False
    )

    def save(self, *args, **kwargs):
        if Conference.objects.filter(active=True).exists():
            self.instance.conference = Conference.objects.filter(active=True).latest('id')
        super(ProposalForm, self).save(*args, **kwargs)

    class Meta:
        model = Proposal
        fields = (
            'name',
            'email',
            'proposal_name',
            'proposal_length',
            'description',
            'other',
            'conference',
        )