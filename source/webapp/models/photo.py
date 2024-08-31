import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/', verbose_name='Фотография', null=False)
    signature = models.CharField(verbose_name='Подпись', max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    album = models.ForeignKey('webapp.Album', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Альбом')
    is_public = models.BooleanField(default=False, verbose_name='Публичная')
    favorite_users = models.ManyToManyField(get_user_model(), related_name='favorite_photos', blank=True,
                                            verbose_name='Избранное')
    token = models.UUIDField(default=None, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if self.token is None:
            self.token = uuid.uuid4()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('webapp:main')
        # return reverse("webapp:detail_photo", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.photo} - {self.author}'
