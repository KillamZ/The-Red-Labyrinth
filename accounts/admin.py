from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Player, School

# Register your models here.
class PlayerAdmin(UserAdmin):
    list_display = (
        'first_name', 'last_name', 'username', 'email', 'school', 'score', 'phone_number'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'school', 'phone_number')
        }),
        ('Score', {
            'fields': ('score',)
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ( 'first_name', 'last_name', 'email', 'school', 'phone_number')
        }),
        ('Score Info', {
            'fields': ('score',)
        })
    )
admin.site.register(Player, PlayerAdmin)
admin.site.register(School)