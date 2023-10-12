from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Client
from newsletter.forms import NewsLetterMessageForm, NewsLetterSettingsForm
from newsletter.models import NewsletterMessage, NewsletterLog, NewsletterSettings


class NewsletterLogListView(ListView):
    model = NewsletterLog

class NewsletterSettingsListView(ListView):
    model = NewsletterSettings
class NewsletterSettingsDetailView(DetailView):
    model = NewsletterSettings
    context_object_name = 'newsletter'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['newsletter_message'] = NewsletterMessage.objects.get(newsletter=self.object)
        context['newsletter_client'] = Client.objects.filter(newslettersettings=self.object)
        return context


class NewsletterSettingsCreateView(CreateView):
    model = NewsletterSettings
    form_class = NewsLetterSettingsForm
    extra_form_class = NewsLetterMessageForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletter_form'] = context['form']
        context['newsletter_message_form'] = self.extra_form_class()
        return context

    def get_queryset(self, **kwargs):
        context = super(Client).get_context_data(**kwargs)
        context['client'] = Client.objects.filter(id=self.kwargs['id'])
        return context

    def form_valid(self, form):
        newsletter = form.save(commit=False)
        extra_form = self.extra_form_class(self.request.POST)
        newsletter.save()

        if extra_form.is_valid():
            newsletter_message = extra_form.save(commit=False)
            newsletter_message.newsletter = newsletter
            newsletter_message.save()

        return super().form_valid(form)

class NewsletterSettingsUpdateView(UpdateView):
    model = NewsletterSettings
    form_class = NewsLetterSettingsForm
    def get_success_url(self):
        return reverse('NewsletterSettings_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newsletter_message = NewsletterMessage.objects.get(newsletter=self.object)
        context['newsletter_message_form'] = NewsLetterMessageForm(instance=newsletter_message)
        return context

    def form_valid(self, form):
        newsletter = form.save(commit=False)
        newsletter.save()

        newsletter_message = NewsletterMessage.objects.get(newsletter=newsletter)
        extra_form = NewsLetterMessageForm(self.request.POST, instance=newsletter_message)
        if extra_form.is_valid():
            extra_form.save()

        return super().form_valid(form)

class NewsletterSettingsDeleteView(DeleteView):
    model = NewsletterSettings
    success_url = reverse_lazy('NewsletterSettings_list')
