from django.db import models

from ckeditor.fields import RichTextField

from django.contrib.auth.models import AbstractUser

from apps.user.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True, default='img/default_user_image.png')
    bio = RichTextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.email}"
