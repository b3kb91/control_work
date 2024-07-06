from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=500, null=False, blank=False, verbose_name='Текст записи')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=100, null=False, blank=False, choices=status_choices,
                              default='active', verbose_name='Статус')

    def __str__(self):
        return f'{self.name} {self.email} {self.text} {self.status}'

    class Meta:
        db_table = 'GuestBooks'
        verbose_name = 'Гостевая книга'
        verbose_name_plural = 'Гостевые книги'
