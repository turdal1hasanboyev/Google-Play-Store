from django.db import models


class BaseModel(models.Model):
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Model'
