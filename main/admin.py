from django.contrib import admin

from main.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'comment',)
    list_filter = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)

