from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username', 'user_type', 'is_premium', 'duration']

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)