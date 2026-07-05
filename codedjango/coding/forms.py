from django import forms
from .models import CodingChallenge

class CodingChallengeForm(forms.Form):
    code_challenge = forms.ModelChoiceField(queryset=CodingChallenge.objects.all(), label="Select Coding Challenge")
