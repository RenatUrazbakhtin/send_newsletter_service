from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'created_date', 'views_count', 'is_published')
    list_filter = ('title', 'created_date',)
    search_fields = ('title', 'body', 'created_date',)
