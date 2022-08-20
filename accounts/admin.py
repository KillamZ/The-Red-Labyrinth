from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, School

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = (
        'first_name', 'last_name', 'username', 'email', 'school', 'score', 'rank', 'phone_number'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'school', 'phone_number')
        }),
        ('Rank info', {
            'fields': ('score', 'rank')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ( 'first_name', 'last_name', 'email', 'school', 'phone_number')
        }),
        ('Rank Info', {
            'fields': ('score', 'rank')
        })
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(School)