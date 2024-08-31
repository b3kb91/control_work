from django.db import models
from django.contrib.auth.models import User

from webapp.models import Album


class FavoriteAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом')

    def __str__(self):
        return f"{self.user} - {self.album}"
