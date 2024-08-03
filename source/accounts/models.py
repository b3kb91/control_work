from django.contrib.auth.models import AbstractUser
from django.db import models


class UserForum(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=False, null=False)
