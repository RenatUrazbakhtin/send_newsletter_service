
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from blog.forms import BlogForm
from blog.models import Blog



# Create your views here.

class BlogCreateView(CreateView):
    """
    Отображение для создания блога
    """
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs_list')

class BlogDeleteView(DeleteView):
    """
    Отображение для удаления блога
    """

    model = Blog
    success_url = reverse_lazy('blogs_list')

class BlogListView(ListView):
    """
    Отображение для списка блогов
    """

    model = Blog
    context_object_name = 'blogs'
    queryset = Blog.objects.filter(is_published=True).order_by('created_date')

class BlogDetailView(DetailView):
    """
    Отображение для отдельного блога
    """

    model = Blog
    context_object_name = 'blog'
    queryset = Blog.objects.filter(is_published=True)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.add_view()
        self.object.save()
        return self.object

class BlogUpdateView(UpdateView):
    """
    Отображение для редактирования блога
    """

    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.save()
        return super().form_valid

