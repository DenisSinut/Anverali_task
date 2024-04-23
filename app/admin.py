from django.contrib import admin

from app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'type']
    fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'type', 'experience']

