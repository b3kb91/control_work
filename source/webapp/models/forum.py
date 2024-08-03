from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название')
    content = models.TextField(max_length=300, blank=False, null=False, verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("webapp:main")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

