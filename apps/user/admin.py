from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.site_header = "Google Play Store Admin Panel"
admin.site.site_title = "Google Play Store Admin Panel"
admin.site.index_title = "Welcome to Google Play Store Admin Panel!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom User Admin Model
    """

    model = CustomUser # model

    ordering = ('email',) # tartiblash

    search_fields = ( # qidiruv uchun
        'email',
        'phone_number',
        'first_name',
        'last_name',
    )

    list_display = ( # displayda ko'rinish uchun
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'image',
        'is_active',
        'is_superuser',
        'is_staff',
        'last_login',
        'date_joined',
    )

    list_filter = ( # filter uchun
        'is_active',
        'is_superuser',
        'is_staff',
    )

    readonly_fields = ( # readonly uchun
        'id',
        'last_login',
        'date_joined',
    )

    # prepopulated_fields = { # avto to'ldirish uchun
    #     'slug': ('first_name', 'last_name'),
    # }

    fieldsets = ( # bezak uchun
        ('Login', {
            'fields': ('email', 'password',),
            'classes': ('wide',), # wide katta korinish uchun
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'phone_number', 'image', 'bio',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
            'classes': ('wide',),
        }),
        ("Important Dates", {
            'fields': ('date_joined', 'last_login',),
            'classes': ('wide',),
        }),
        ("ID", {
            'fields': ('id',), # bu uchun readonly bolishi kerak
            'classes': ('wide',),
        }),
    )
    add_fieldsets = ( # superuser uchun
        ('Create Super User', {
            'fields': ('email', 'password1', 'password2',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff',),
            'classes': ('wide',),
        }),
    )
