from django import forms

from newsletter.models import NewsletterMessage, NewsletterSettings


class NewsLetterMessageForm(forms.ModelForm):
    class Meta:
        model = NewsletterMessage
        fields = ('title', 'body')

class NewsLetterSettingsForm(forms.ModelForm):
    class Meta:
        model = NewsletterSettings
        fields = ('__all__')