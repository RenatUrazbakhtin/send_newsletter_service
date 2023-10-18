from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django_apscheduler.jobstores import DjangoJobStore

from main.models import Client
from newsletter.forms import NewsLetterMessageForm, NewsLetterSettingsForm
from newsletter.models import NewsletterMessage, NewsletterLog, NewsletterSettings
from newsletter.services import get_schedule

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()


class NewsletterLogListView(LoginRequiredMixin, ListView):
    model = NewsletterLog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset().filter(newsletter_id=self.kwargs.get('pk'))
        queryset = queryset.order_by('-pk')
        return queryset


class NewsletterSettingsListView(LoginRequiredMixin, ListView):
    model = NewsletterSettings

    def get_context_data(self, **kwargs):
        object_list = NewsletterSettings.objects.all()
        context_data = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context_data['object_list'] = object_list
        else:
            context_data['object_list'] = object_list.filter(creator=self.request.user)

        return context_data


class NewsletterSettingsDetailView(LoginRequiredMixin, DetailView):
    model = NewsletterSettings
    context_object_name = 'newsletter'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['newsletter_message'] = NewsletterMessage.objects.get(newsletter=self.object)
        context['newsletter_client'] = Client.objects.filter(newslettersettings=self.object)
        return context


class NewsletterSettingsCreateView(LoginRequiredMixin, CreateView):
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
        newsletter.status = 'CR'
        extra_form = self.extra_form_class(self.request.POST)
        newsletter.creator = self.request.user
        newsletter.save()

        if extra_form.is_valid():
            newsletter_message = extra_form.save(commit=False)
            newsletter_message.newsletter = newsletter
            newsletter_message.save()

            NewsletterLog.objects.create_log(newsletter.status, newsletter)

            if newsletter.newsletter_time_from <= now() <= newsletter.newsletter_time_to:
                newsletter.status = 'LD'
                get_schedule(scheduler)
            elif newsletter.newsletter_time_to <= now():
                newsletter.status = 'ED'
                NewsletterLog.objects.create_log(newsletter.status, newsletter)

            newsletter.save()

        return super().form_valid(form)


class NewsletterSettingsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsletterSettings
    form_class = NewsLetterSettingsForm

    def test_func(self):
        if self.request.user.is_staff and not self.request.user.is_superuser:
            return False
        else:
            return True

    def get_success_url(self):
        return reverse('NewsletterSettings_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newsletter_message = NewsletterMessage.objects.get(newsletter=self.object)
        context['newsletter_message_form'] = NewsLetterMessageForm(instance=newsletter_message)
        return context

    def form_valid(self, form):
        newsletter = form.save(commit=False)
        newsletter_message = NewsletterMessage.objects.get(newsletter=newsletter)
        extra_form = NewsLetterMessageForm(self.request.POST, instance=newsletter_message)

        if extra_form.is_valid():
            if newsletter.newsletter_time_from <= now() <= newsletter.newsletter_time_to:
                newsletter.status = 'LD'
                get_schedule(scheduler)

            elif newsletter.newsletter_time_to <= now():
                newsletter.status = 'завершена'
                NewsletterLog.objects.create_log(newsletter, newsletter.status)

        extra_form.save()
        return super().form_valid(form)


class NewsletterSettingsDeleteView(LoginRequiredMixin, View):
    model = NewsletterSettings

    def get(self, request, id):
        model = get_object_or_404(NewsletterSettings, id=id)
        task_id = model.task_id
        if task_id:
            scheduler.remove_job(task_id)
            model.task_id = None
            model.save()
        model.delete()
        return redirect('NewsletterSettings_list')


def change_newsletter_activity(*args, **kwargs):
    """
    Изменение активности рассылки
    """
    newsletter = get_object_or_404(NewsletterSettings, pk=kwargs.get('pk'))
    if newsletter.is_active:
        newsletter.is_active = False
    else:
        newsletter.is_active = True
    newsletter.save()

    return redirect(reverse_lazy('NewsletterSettings_list'))
