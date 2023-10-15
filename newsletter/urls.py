from django.urls import path

from main.views import HomeView
from newsletter.views import NewsletterSettingsCreateView, NewsletterSettingsUpdateView, NewsletterSettingsDeleteView, \
    NewsletterSettingsDetailView, NewsletterSettingsListView

urlpatterns = [
    path('', HomeView.as_view, name='home'),
    path('NewsletterSettings_create', NewsletterSettingsCreateView.as_view(), name='NewsletterSettings_create'),
    path('NewsletterSettings_update/<int:pk>/', NewsletterSettingsUpdateView.as_view(), name='NewsletterSettings_update'),
    path('NewsletterSettings_delete/<int:pk>/', NewsletterSettingsDeleteView.as_view(), name='NewsletterSettings_delete'),
    path('NewsletterSettings_list', NewsletterSettingsListView.as_view(), name='NewsletterSettings_list'),
    path('NewsletterSettings_detail/<int:pk>/', NewsletterSettingsDetailView.as_view(), name='NewsletterSettings_detail'),

]