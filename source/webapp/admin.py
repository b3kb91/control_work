from django.contrib import admin

from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text', 'id', 'status']
    list_filter = ['name', 'email', 'status', 'id']
    list_display_links = ['text', 'name']
    search_fields = ['name', 'status']
    fields = ['name', 'email', 'text', 'id']
    readonly_fields = ['creation_time', 'update_time']


admin.site.register(GuestBook, GuestBookAdmin)
