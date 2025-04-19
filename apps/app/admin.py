from django.contrib import admin

from .models import App


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'logo',
        'apk_file',
        'developer',
        'category',
        'version',
        'size',
        'downloads',
        'review_count',
        'is_free',
        'price',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_free',
        'is_active',
    )
    search_fields = (
        'title',
        'version',
        'size',
        'downloads',
        'price',
    )

    def review_count(self, obj):
        return obj.review_app.count()
    
    review_count.short_description = 'Reviews Count'
