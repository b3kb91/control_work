from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор альбома')
    is_public = models.BooleanField(default=False, verbose_name='Публичный')

    def __str__(self):
        return f'{self.title} - {self.author}'
