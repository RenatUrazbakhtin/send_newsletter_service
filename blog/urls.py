from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

urlpatterns = [
    path('blogs_list/', BlogListView.as_view(), name='blogs_list'),
    path('Create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update')
]