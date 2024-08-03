from django.contrib import admin
from .models import Topic, Answer


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'user']
    search_fields = ['title', 'content']
    list_filter = ['created_at',]


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'created_at', 'topic']
    search_fields = ['content',]
    list_filter = ['created_at', 'topic']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Answer, ReplyAdmin)
