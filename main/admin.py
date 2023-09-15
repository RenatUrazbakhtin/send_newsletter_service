from django.contrib import admin

from main.models import Client, NewsletterSettings, NewsletterMessage, NewsletterLog


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'comment',)
    list_filter = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)

@admin.register(NewsletterSettings)
class NewsletterSettingsAdmin(admin.ModelAdmin):
    list_display = ('newsletter_time_from', 'newsletter_time_to', 'periodicity', 'status')
    list_filter = ('status',)
    search_fields = ('periodicity', 'subject',)

@admin.register(NewsletterMessage)
class NewsletterMessageAdmin(admin.ModelAdmin):
    list_display = ('title','body',)
    list_filter = ('title',)
    search_fields = ('title','body',)

@admin.register(NewsletterLog)
class NewsletterLogAdmin(admin.ModelAdmin):
    list_display = ('last_attempt_time','feedback','attempt_status',)
    list_filter = ('attempt_status',)
    search_fields = ('last_attempt_time',)