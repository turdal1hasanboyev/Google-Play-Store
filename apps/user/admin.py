from django.contrib import admin

from .models import CustomUser


admin.site.site_header = "Google Play Store Admin Panel"
admin.site.site_title = "Google Play Store Admin Panel"
admin.site.index_title = "Welcome to Google Play Store Admin Panel!"


admin.site.register(CustomUser)
