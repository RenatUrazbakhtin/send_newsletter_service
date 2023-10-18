from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    """
    Форма для создания блога
    """

    class Meta:
        model = Blog
        fields = ['title', 'body', 'image', 'is_published',]