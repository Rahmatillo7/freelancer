from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group


# admin.site.register(Group)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_display = ('username', 'email')