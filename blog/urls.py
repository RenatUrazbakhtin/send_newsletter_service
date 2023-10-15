from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

urlpatterns = [
    path('blogs_list/', cache_page(60)(BlogListView.as_view()), name='blogs_list'),
    path('Create_blog/', cache_page(60)(BlogCreateView.as_view()), name='create_blog'),
    path('blog_detail/<int:pk>/', cache_page(60)(BlogDetailView).as_view(), name='blog_detail'),
    path('blog_delete/<int:pk>/', cache_page(60)(BlogDeleteView.as_view()), name='blog_delete'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update')
]