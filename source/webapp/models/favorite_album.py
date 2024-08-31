from django.db import models
from django.contrib.auth.models import User


class FavoriteAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    album = models.ForeignKey("webapp.Album", on_delete=models.CASCADE, verbose_name='Альбом')

    def __str__(self):
        return f"{self.user} - {self.album}"
