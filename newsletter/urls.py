from django.urls import path

from main.views import HomeView
from newsletter.views import NewsletterSettingsCreateView, NewsletterSettingsUpdateView, NewsletterSettingsDeleteView, \
    NewsletterSettingsDetailView, NewsletterSettingsListView, NewsletterLogListView, change_newsletter_activity

urlpatterns = [
    path('', HomeView.as_view, name='home'),
    path('NewsletterSettings_create', NewsletterSettingsCreateView.as_view(), name='NewsletterSettings_create'),
    path('NewsletterSettings_update/<int:pk>/', NewsletterSettingsUpdateView.as_view(), name='NewsletterSettings_update'),
    path('NewsletterSettings_delete/<int:id>//', NewsletterSettingsDeleteView.as_view(), name='NewsletterSettings_delete'),
    path('NewsletterSettings_list', NewsletterSettingsListView.as_view(), name='NewsletterSettings_list'),
    path('NewsletterSettings_detail/<int:pk>/', NewsletterSettingsDetailView.as_view(), name='NewsletterSettings_detail'),
    path('NewsletterLog_list/<int:pk>/', NewsletterLogListView.as_view(), name='NewsletterLog_list'),
    path('change_newsletter_activity/<int:pk>/', change_newsletter_activity, name='change_newsletter_activity'),
]