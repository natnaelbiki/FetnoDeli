# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationAdminForm, CustomUserChangeAdminForm
from .models import CustomUser

class AdminCustomUser(admin.ModelAdmin):
    add_form = CustomUserCreationAdminForm
    form = CustomUserChangeAdminForm
    model = CustomUser
    list_display =['username', 'first_name', 'last_name', 'role']

admin.site.register(CustomUser, AdminCustomUser)