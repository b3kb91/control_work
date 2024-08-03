from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models import Topic


class Answer(models.Model):
    topic = models.ForeignKey(Topic, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Комментарий', null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("webapp:main")

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'Answer'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
