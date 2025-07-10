from django import forms
from trials.models import TrialEvent
class TrialEventForm(forms.ModelForm):
    class Meta:
        model = TrialEvent
        fields = ['title', 'location', 'date', 'description', 'banner_image', 'registration_link']




#REPLY MESSAGES FORM
class ReplyMessageForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=150)
    body = forms.CharField(label='Message Body', widget=forms.Textarea(attrs={'rows': 6}))
