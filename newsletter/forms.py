from django import forms

from newsletter.models import NewsletterMessage, NewsletterSettings


class NewsLetterMessageForm(forms.ModelForm):
    class Meta:
        model = NewsletterMessage
        fields = ('title', 'body')

class NewsLetterSettingsForm(forms.ModelForm):
    newsletter_time_from = forms.DateTimeField(widget=forms.widgets.TimeInput(attrs={'type': 'datetime-local'}))
    newsletter_time_to = forms.DateTimeField(widget=forms.widgets.TimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = NewsletterSettings
        fields = ('periodicity', 'status', 'newsletter_time_from', 'newsletter_time_to', 'client')