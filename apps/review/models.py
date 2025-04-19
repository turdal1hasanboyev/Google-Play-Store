from django.db import models

from ckeditor.fields import RichTextField

from django.core.validators import MinValueValidator, MaxValueValidator

from apps.common.models import BaseModel


class Review(BaseModel):
    app = models.ForeignKey(
        'app.App', on_delete=models.CASCADE, related_name='review_app')
    user = models.ForeignKey(
        'user.CustomUser', on_delete=models.CASCADE, related_name='review_user')
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.user.email} - {self.app.title}"
