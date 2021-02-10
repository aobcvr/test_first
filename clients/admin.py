from django.contrib import admin
from .models import Client
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(Client)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'is_active', 'is_staff', 'last_login', 'date_joined',
    )
    fieldsets = (
        (None, {'fields': ('email', 'spent_money')}),
        (_('Personal info'), {'fields': ('username',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1',
                       'password2')}
         ),
    )
