from django.db import models
from django.contrib.auth.models import User

from webapp.models import Photo


class FavoritePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name='Фотография')

    def __str__(self):
        return f"{self.user} - {self.photo}"
