from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор альбома')
    is_public = models.BooleanField(default=False, verbose_name='Публичный')
    favorite_users = models.ManyToManyField(get_user_model(), related_name='favorite_albums', blank=True,
                                            verbose_name='Избранное')

    def __str__(self):
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        return reverse('webapp:main')
        # return reverse("webapp:detail_album", kwargs={"pk": self.pk})

    def get_photos(self):
        return self.photo_set.filter(is_public=True).order_by('-created_at')

    def save(self, *args, **kwargs):
        if not self.is_public:

            if self.pk and Album.objects.get(pk=self.pk).is_public:
                self.photo_set.update(is_public=False)
        super().save(*args, **kwargs)
