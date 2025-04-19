from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel
from apps.category.models import Category
from apps.user.models import CustomUser


class App(BaseModel):
    title = models.CharField(max_length=300, unique=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    logo = models.ImageField(upload_to='app_logos/', null=True, blank=True, default='img/default_image.png')
    apk_file = models.FileField(upload_to='apk_files/', blank=True, null=True)
    developer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='app_developer')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='app_category')
    version = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    downloads = models.IntegerField(default=0)
    is_free = models.BooleanField(default=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'

    def __str__(self):
        return f"{self.title}"
