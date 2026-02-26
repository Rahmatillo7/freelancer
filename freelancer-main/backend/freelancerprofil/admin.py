from django.contrib import admin
from .models import FreelancerProfile


@admin.register(FreelancerProfile)
class FreelancerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'price', 'rating', 'status', 'created')
    list_filter = ('status', 'created', 'service_type')
    search_fields = ('user__username', 'service_type', 'experience')
    readonly_fields = ('rating', 'created', 'updated')
    list_editable = ('status', 'price')