from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Client


# Create your views here.

def home(request):
    return render(request, 'main/home.html')

class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):
    model = Client

class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'first_name', 'last_name', 'comment']
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['email', 'first_name', 'last_name', 'comment']
    def get_success_url(self):
        return reverse('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')



