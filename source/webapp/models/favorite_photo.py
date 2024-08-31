from django.db import models
from django.contrib.auth.models import User


class FavoritePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='favorite_photos')
    photo = models.ForeignKey("webapp.Photo", on_delete=models.CASCADE, verbose_name='Фотография')

    def __str__(self):
        return f"{self.user} - {self.photo}"
