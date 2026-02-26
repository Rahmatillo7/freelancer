from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('id', 'service_type', 'client__username')
    list_display = ('id', 'client', 'freelancer', 'service_type', 'price', 'status', 'payment_status', 'created')
    list_filter = ('status', 'payment_status', 'created')
    list_editable = ('status', 'payment_status')
    readonly_fields = ('created', 'updated')