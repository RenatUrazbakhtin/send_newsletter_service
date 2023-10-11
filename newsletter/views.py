from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newsletter.forms import NewsLetterMessageForm, NewsLetterSettingsForm
from newsletter.models import NewsletterMessage, NewsletterLog, NewsletterSettings


# Create your views here.
class NewsletterMessageListView(ListView):
    model = NewsletterMessage

class NewsletterMessageDetailView(DetailView):
    model = NewsletterMessage

class NewsletterMessageCreateView(CreateView):
    model = NewsletterMessage
    form_class = NewsLetterMessageForm
    success_url = reverse_lazy('NewsletterMessage_list')

class NewsletterMessageUpdateView(UpdateView):
    model = NewsletterMessage
    form_class = NewsLetterMessageForm
    def get_success_url(self):
        return reverse('NewsletterMessage_list')

class NewsletterMessageDeleteView(DeleteView):
    model = NewsletterMessage
    success_url = reverse_lazy('NewsletterMessage_list')


# class NewsletterLogListView(ListView):
#     model = NewsletterLog
#
# class NewsletterSettingsListView(ListView):
#     model = NewsletterSettings
#
# class NewsletterSettingsDetailView(DetailView):
#     model = NewsletterSettings
#
# class NewsletterSettingsCreateView(CreateView):
#     model = NewsletterSettings
#     form_class = NewsLetterSettingsForm
#     success_url = reverse_lazy('home')
#
# class NewsletterSettingsUpdateView(UpdateView):
#     model = NewsletterSettings
#     form_class = NewsLetterSettingsForm
#     def get_success_url(self):
#         return reverse('NewsletterMessage_list')
#
# class NewsletterSettingsDeleteView(DeleteView):
#     model = NewsletterSettings
#     success_url = reverse_lazy('NewsletterMessage_list')
