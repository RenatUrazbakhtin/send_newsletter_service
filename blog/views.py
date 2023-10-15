import random

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, DetailView, UpdateView

from blog.forms import BlogForm
from blog.models import Blog
from main.models import Client
from newsletter.models import NewsletterSettings


# Create your views here.

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs_list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs_list')

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    queryset = Blog.objects.filter(is_published=True).order_by('created_date')

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    queryset = Blog.objects.filter(is_published=True)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.add_view()
        return self.object

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.save()
        return super().form_valid

