"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/user_management/admin.py
    Description: This module contains all admin page definitions for the user_management application.
--------------------------------------------------------------------------------------------------
"""
from django.contrib import admin
from .models import User
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    search_fields = ['employee', 'username']

    add_form = UserAdminCreationForm
    form = UserAdminChangeForm

    list_display = ('username', 'employee', 'admin', 'staff', 'active')
    list_filter = ('admin', 'staff', 'active')

    fieldsets = (
                    (None, {'fields': ('username', 'employee', 'password')}),
                    ('Permissions', {'fields': ('admin', 'staff', 'active', 'groups', 'user_permissions')}),
                    ('Change Password', {'fields': ('password1', 'password2')})
                )

    add_fieldsets = (
                        (None, {
                                    'classes': ('wide',),
                                    'fields': ('username',
                                               'employee',
                                               'password1',
                                               'password2',
                                               'admin',
                                               'staff',
                                               'active',
                                               'groups'
                                               )
                               }
                         ),
                    )
    ordering = ('employee',)


admin.site.register(User, UserAdmin)
