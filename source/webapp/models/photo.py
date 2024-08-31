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

    def get_absolute_url(self):
        return reverse('webapp:main')
        # return reverse("webapp:detail_photo", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.photo} - {self.author}'
