from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'app',
        'user',
        'rating',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
