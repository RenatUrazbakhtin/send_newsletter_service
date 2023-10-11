from django.urls import path

from main.views import home
from newsletter.views import NewsletterMessageCreateView, NewsletterMessageUpdateView, NewsletterMessageDeleteView, \
    NewsletterMessageListView, NewsletterSettingsCreateView, NewsletterSettingsUpdateView, NewsletterSettingsDeleteView, \
    NewsletterSettingsDetailView, NewsletterSettingsListView

urlpatterns = [
    path('', home, name='home'),
    path('NewsletterMessage_create/', NewsletterMessageCreateView.as_view(), name='NewsletterMessage_create'),
    path('NewsletterMessage_update/<int:pk>/', NewsletterMessageUpdateView.as_view(), name='NewsletterMessage_update'),
    path('NewsletterMessage_delete/<int:pk>/', NewsletterMessageDeleteView.as_view(), name='NewsletterMessage_delete'),
    path('NewsletterMessage_list/', NewsletterMessageListView.as_view(), name='NewsletterMessage_list'),
    path('NewsletterSettings_create', NewsletterSettingsCreateView.as_view(), name='NewsletterSettings_create'),
    path('NewsletterSettings_update/<int:pk>/', NewsletterSettingsUpdateView.as_view(), name='NewsletterSettings_update'),
    path('NewsletterSettings_delete/<int:pk>/', NewsletterSettingsDeleteView.as_view(), name='NewsletterSettings_delete'),
    path('NewsletterSettings_list', NewsletterSettingsListView.as_view(), name='NewsletterSettings_list'),
    path('NewsletterSettings_detail/<int:pk>/', NewsletterSettingsDetailView.as_view(), name='NewsletterSettings_detail'),

]