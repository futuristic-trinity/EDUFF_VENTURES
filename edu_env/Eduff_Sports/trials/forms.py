# trials/forms.py
from django import forms
from .models import TrialRegistration

class TrialRegistrationForm(forms.ModelForm):
    class Meta:
        model = TrialRegistration
        fields = [
            'full_name', 'email', 'phone', 'preferred_position',
            'location', 'passport_photo', 'event'
        ]
        widgets = {
            'event': forms.HiddenInput()  # if event is selected from view context
        }
