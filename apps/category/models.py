from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
