from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Replace with your actual model name if different

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Optionally customize the admin display
    list_display = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
