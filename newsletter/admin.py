from django.contrib import admin

from newsletter.models import NewsletterSettings, NewsletterMessage, NewsletterLog


# Register your models here.
@admin.register(NewsletterSettings)
class NewsletterSettingsAdmin(admin.ModelAdmin):
    list_display = ('newsletter_time_from', 'newsletter_time_to', 'periodicity', 'status',)
    list_filter = ('status',)
    search_fields = ('periodicity', 'subject',)

@admin.register(NewsletterMessage)
class NewsletterMessageAdmin(admin.ModelAdmin):
    list_display = ('title','body',)
    list_filter = ('title',)
    search_fields = ('title','body',)

@admin.register(NewsletterLog)
class NewsletterLogAdmin(admin.ModelAdmin):
    list_display = ('last_attempt_time','feedback','attempt_status','newsletter',)
    list_filter = ('attempt_status',)
    search_fields = ('last_attempt_time',)