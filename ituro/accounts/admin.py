from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'phone', 'school')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'phone', 'school', 'is_staff', 'is_active')
    search_fields = ('name', 'email', 'phone', 'school')
    ordering = ('id',)


admin.site.register(CustomUser, CustomUserAdmin)
