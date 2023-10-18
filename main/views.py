import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Blog
from main.models import Client
from newsletter.models import NewsletterSettings


# Create your views here.

class HomeView(TemplateView):
    """
    Отображение для домашней страницы
    """

    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        """
        Выборка количества рассылок, количества активных рассылок, количества уникальных клиентов
        """
        context = {}
        blogs = Blog.objects.all()
        if blogs:
            random_numbers = random.sample(range(len(blogs)), min(3, len(blogs)))
            random_blogs = [blogs[i] for i in random_numbers]
            context['blogs'] = random_blogs
        context['newsletter_count'] = NewsletterSettings.objects.count()
        context['newsletter_active'] = NewsletterSettings.objects.filter(status__in=['CR', 'LD']).count()
        clients_objects = NewsletterSettings.client.through.objects.all()
        list = []
        for item in clients_objects:
            list.extend(str(item.client_id))
        context['unique_clients'] = len(set(list))
        return context

class ClientListView(LoginRequiredMixin, ListView):
    """
    Отображение для списка клиентов
    """
    model = Client

class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Отображение для отдельного клиента
    """
    model = Client

class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Отображение для создания клиента
    """
    model = Client
    fields = ['email', 'first_name', 'last_name', 'comment']
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        """
        Запись в поле creator при валидности формы создания клиента
        """
        client = form.save(commit=False)
        client.creator = self.request.user
        client.save()

        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """
    Отображение для редактирования клиента
    """

    model = Client
    fields = ['email', 'first_name', 'last_name', 'comment']
    def get_success_url(self):
        return reverse('client_list')

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Отображение для удаления клиента
    """
    model = Client
    success_url = reverse_lazy('client_list')



