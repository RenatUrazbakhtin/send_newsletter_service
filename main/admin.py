from django.contrib import admin

from main.models import Client, NewsletterSettings, NewsletterMessage, NewsletterLog


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'fullname', 'comment',)
    list_filter = ('email', 'fullname',)
    search_fields = ('email', 'fullname',)

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